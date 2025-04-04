import os
from typing import Generator, Optional
from swift.llm import PtEngine, RequestConfig, InferRequest
import sys

class ChatBotEngine:
    def __init__(
        self,
        model_path: str,
        max_batch_size: int = 1,
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


# 示例用法 --------------------------------------------------
if __name__ == "__main__":
    
    bot_engine = ChatBotEngine(
        model_path="/root/.cache/modelscope/hub/models/walker001/api-testpilot-model", # 替换成模型下载的地址，替换成模型下载的地址，替换成模型下载的地址
        max_tokens=10240,
        temperature=0.1
    )

    api_desc = """
登录接口
-----------------------
Method: POST
URL: /api/ymlogin/
请求参数:
- username (string) - 用户名（必填）- 限制11位手机号
- password (string) - 密码（必填）- 长度6~12位
返回值:
- code (int) - 状态码（0表示登录成功，其他表示登录失败）
- msg (string) - 操作结果消息
- user (string) - 登录成功后返回的用户名
- error (string) - 错误消息（当发生异常时存在）
HTTP状态码:
- 200 - 请求成功，登录成功
- 403 - 用户名或密码错误
- 404 - 账号已过期
- 500 - 内部服务器错误
使用示例: POST /api/ymlogin/
Content-Type: application/x-www-form-urlencoded
Body: username=user123&password=pass123
注意: 该接口对IP地址进行限制，每个IP每天最多访问30次。用户必须输入有效的用户名和密码才能登录。登录成功后，用户的session会被创建并记录在数据库中。如果登录过程中出现异常，接口将返回错误信息。接口会记录用户的登录行为。

"""

    ChatClient.run(bot_engine, api_desc)
