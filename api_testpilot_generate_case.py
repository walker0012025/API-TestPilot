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
        # 身份输出前换行，之后添加等号分隔符，再换行后开始正式对话
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
        model_path="/root/.cache/modelscope/hub/models/walker001/api-testpilot-model",
        max_tokens=10240,
        temperature=0.1
    )

    api_desc = """
提交学员练习评分接口
-----------------------
Method: POST
URL: /api/subLearnScore/
请求参数
Headers:
- Content-Type: application/x-www-form-urlencoded
Body 参数:
- c_s_id (string) - 课程安排ID（必填）
- code (string) - 学员提交的代码/答案（必填），长度2万个字符
- p_q_co (string) - 实战题目内容（必填，若无则传"null"字符串）
- c_na (string) - 课程名称（必填）
- s_c_na (string) - 小节课程名称（必填）
返回值
- code (int) - 状态码
  - 0: 提交成功
  - 1: 参数缺失
  - 2: 处理AI评分失败
- msg (string) - 操作结果消息
- score (float) - AI评分结果（仅code=0时存在）
- feedback (string) - AI反馈内容（仅code=0时存在）
- error (string) - 错误详情（仅发生异常时存在）
HTTP状态码
- 200 - 请求成功（无论提交是否完成，需结合code字段判断具体结果）
- 401 - 用户未登录
- 400 - 请求参数不合法
- 500 - 内部服务器错误
使用示例
POST /api/subLearnScore/ HTTP/1.1
Content-Type: application/x-www-form-urlencoded

c_s_id=course_123&code=print("hello")&p_q_co=null&c_na=Python基础&s_c_na=变量与数据类型
注意事项
- 登录态校验
  - 用户必须已通过登录接口认证，否则返回401状态码。
  - 请求头需携带有效Session/Cookie。
- 参数必填性
  - 所有参数均需传值，空字符串或null需按规则传递（如p_q_co无实战题目时传"null"）。
- AI评分逻辑
  - 接口会调用智谱AI进行评分，最多重试10次。
  - 若AI处理失败，返回code=2及错误消息。
- 数据记录
  - 评分结果会存入LearnerExerciseScore表。
  - 若同一用户对同一课程安排重复提交，会更新LearnerCourseRating表中的评分。

"""

    ChatClient.run(bot_engine, api_desc)