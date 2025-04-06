import os
from typing import Generator, Optional
from swift.llm import PtEngine, RequestConfig, InferRequest
import sys

class ChatBotEngine:
    def __init__(
        self,
        model_path: str,
        max_batch_size: int = 2,
        max_tokens: int = 10240,
        temperature: float = 0.1,
        device: str = "cuda:0"
    ):
        
        os.environ["CUDA_VISIBLE_DEVICES"] = device.split(":")[-1]
        
        self.model_engine = PtEngine(
            model_path,
            max_batch_size=max_batch_size,
            device_map=device
        )
        
        self.default_config = RequestConfig(
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )

    def _identity_check(self) -> str:
        identity_req = InferRequest(messages=[
            {"role": "user", "content": "你是谁？"}
        ])
        return self._generate(identity_req)

    def _generate(self, request: InferRequest) -> str:
        gen = self.model_engine.infer([request], self.default_config)[0]
        return "".join(
            chunk.choices[0].delta.content 
            for chunk in gen 
            if chunk and chunk.choices
        )

    def stream_chat(self, messages: list) -> Generator[str, None, None]:
        identity_response = self._identity_check()
        yield f"\n{identity_response}\n\n" + "=" * 40 + "\n\n"

        request = InferRequest(messages=messages)
        gen = self.model_engine.infer([request], self.default_config)[0]
        
        for chunk in gen:
            if chunk and chunk.choices:
                yield chunk.choices[0].delta.content

    def chat(self, messages: list) -> str:
        return "".join(self.stream_chat(messages))

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


# 示例用法 --------------------------------------------------
if __name__ == "__main__":
    
    bot_engine = ChatBotEngine(
        model_path="/root/.cache/modelscope/hub/models/walker001/api-testpilot-model", # 一般不用改，报错就替换成模型下载的地址
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
