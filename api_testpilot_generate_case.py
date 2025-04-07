import os
from typing import Generator, Optional
from modelscope import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import TextIteratorStreamer
from threading import Thread

class ChatBotEngine:
    def __init__(
        self,
        model_path: str,
        max_tokens: int = 10240,
        temperature: float = 0.1,
        device: str = "cuda:0"
    ):
        os.environ["CUDA_VISIBLE_DEVICES"] = device.split(":")[-1]
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, 
            trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.float16,
            trust_remote_code=True
        ).eval()
        
        self.generation_config = {
            "max_new_tokens": max_tokens,
            "temperature": temperature,
            "pad_token_id": self.tokenizer.eos_token_id
        }

    def _build_prompt(self, messages: list) -> str:
        prompt = ""
        for msg in messages:
            if msg["role"] == "system":
                prompt += f"<|system|>\n{msg['content']}</s>\n"
            elif msg["role"] == "user":
                prompt += f"<|user|>\n{msg['content']}</s>\n"
            elif msg["role"] == "assistant":
                prompt += f"<|assistant|>\n{msg['content']}</s>\n"
        prompt += "<|assistant|>\n"
        return prompt

    def _identity_check(self) -> str:
        messages = [{"role": "user", "content": "你是谁？"}]
        return self._generate(messages)

    def _generate(self, messages: list) -> str:
        prompt = self._build_prompt(messages)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                **self.generation_config
            )
        response = self.tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], 
                                       skip_special_tokens=True)
        return response.strip()

    def stream_chat(self, messages: list) -> Generator[str, None, None]:
        identity_response = self._identity_check()
        yield f"\n{identity_response}\n\n" + "=" * 40 + "\n\n"

        prompt = self._build_prompt(messages)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        streamer = TextIteratorStreamer(
            self.tokenizer, 
            skip_prompt=True, 
            skip_special_tokens=True
        )
        
        gen_kwargs = dict(
            **inputs,
            streamer=streamer,
            **self.generation_config
        )
        
        thread = Thread(target=self.model.generate, kwargs=gen_kwargs)
        thread.start()
        
        for new_token in streamer:
            yield new_token

class ChatClient:
    @staticmethod
    def run(engine: ChatBotEngine, api_desc):
        messages = [
            {"role": "system", "content": "你是一名软件测试工程师。你的任务是根据接口文档内容生成接口测试用例。"},
            {"role": "user", "content": api_desc}
        ]

        for chunk in engine.stream_chat(messages):
            print(chunk, end="", flush=True)
        print('\n')

if __name__ == "__main__":
    bot_engine = ChatBotEngine(
        model_path="/root/.cache/modelscope/hub/models/walker001/api-testpilot-model", #模型下载路径，一般不用修改，报错可以修改为模型实际下载路径
        max_tokens=10240,
        temperature=0.1
    )

    api_desc = """
删除部门
最后更新：2020/03/30
请求方式：GET（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=ACCESS_TOKEN&id=ID
 
参数说明 ：
 
权限说明：
应用须拥有指定部门的管理权限。
第三方仅通讯录应用可以调用。
返回结果：
{
   "errcode": 0,
   "errmsg": "deleted"
}
参数说明：

参数	必须	说明
access_token	是	调用接口凭证
id	是	部门id。（注：不能删除根部门；不能删除含有子部门、成员的部门）
参数	说明
errcode	返回码
errmsg	对返回码的文本描述内容
"""

    ChatClient.run(bot_engine, api_desc)
