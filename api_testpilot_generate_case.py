import os
from typing import Generator
from modelscope import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import TextIteratorStreamer
from threading import Thread

class ChatBotEngine:
    def __init__(
        self,
        model_path: str,
        max_tokens: int = 5120,
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
            "pad_token_id": self.tokenizer.eos_token_id,
            "eos_token_id": [151329, 151336, 151338],
        }

        if temperature == 0:
            self.generation_config.update({
                "num_beams": 5,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            })
        else:
            self.generation_config.update({
                "do_sample": True,
                "top_p": 0.9,
                "early_stopping": False
            })

    def _build_prompt(self, messages: list) -> str:
        prompt = ""
        role_tags = {
            "system": "<|system|>",
            "user": "<|user|>",
            "assistant": "<|assistant|>"
        }
        for msg in messages:
            prompt += f"{role_tags[msg['role']]}\n{msg['content']}</s>\n"
        return prompt + "<|assistant|>\n"

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
        return self.tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], 
                                   skip_special_tokens=True).strip()

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
        
        thread = Thread(target=self.model.generate, kwargs={
            **inputs,
            **self.generation_config,
            "streamer": streamer
        })
        thread.start()
        
        accumulated = 0
        for token in streamer:
            token_len = len(token)
            
            if accumulated >= 5000:
                break
                
            if accumulated + token_len > 5000:
                remain = 5000 - accumulated
                yield token[:remain]
                break
                
            accumulated += token_len
            yield token

class ChatClient:
    @staticmethod
    def run(engine: ChatBotEngine, api_desc: str):
        messages = [
            {"role": "system", "content": "你是一名软件测试工程师。你的任务是根据接口文档内容生成接口测试用例。"},
            {"role": "user", "content": api_desc}
        ]

        for chunk in engine.stream_chat(messages):
            print(chunk, end="", flush=True)
        print('\n')

if __name__ == "__main__":
    bot_engine = ChatBotEngine(
        model_path="/root/.cache/modelscope/hub/models/walker001/api-testpilot-model", #模型下载路径，一般不用修改，报错可以替换为实际模型下载路径
        max_tokens=5120,
        temperature=0.1
    )

    api_desc = """
提交学员练习评分接口
----------------------- 
Method: POST
URL: /api/subLearnScore/
请求参数
Headers:
• Content-Type: application/x-www-form-urlencoded
Body 参数:
• c_s_id (string) - 课程安排ID（必填）
• code (string) - 学员提交的代码/答案（必填），长度2万个字符
• p_q_co (string) - 实战题目内容（必填，若无则传"null"字符串）
• c_na (string) - 课程名称（必填）
• s_c_na (string) - 小节课程名称（必填）
返回值
• code (int) - 状态码
  • 0: 提交成功
  • 1: 参数缺失
  • 2: 处理AI评分失败
• msg (string) - 操作结果消息
• score (float) - AI评分结果（仅code=0时存在）
• feedback (string) - AI反馈内容（仅code=0时存在）
• error (string) - 错误详情（仅发生异常时存在）
HTTP状态码
• 200 - 请求成功（无论提交是否完成，需结合code字段判断具体结果）
• 401 - 用户未登录
• 400 - 请求参数不合法
• 500 - 内部服务器错误
"""

    ChatClient.run(bot_engine, api_desc)
