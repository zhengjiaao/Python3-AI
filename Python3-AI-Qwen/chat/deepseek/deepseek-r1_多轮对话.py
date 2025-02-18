import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    # api_key=os.getenv("DASHSCOPE_|API_KEY"),
    api_key="sk-796c2eb58df24dccb67c5892a9107810",
    # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 通过 messages 数组实现上下文管理
messages = [
    {'role': 'user', 'content': '你好'}
]

completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=messages
)

print("=" * 20 + "第一轮对话" + "=" * 20)
# 通过reasoning_content字段打印思考过程
print("=" * 20 + "思考过程" + "=" * 20)
print(completion.choices[0].message.reasoning_content)
# 通过content字段打印最终答案
print("=" * 20 + "最终答案" + "=" * 20)
print(completion.choices[0].message.content)

messages.append({'role': 'assistant', 'content': completion.choices[0].message.content})
messages.append({'role': 'user', 'content': '你是谁'})
print("=" * 20 + "第二轮对话" + "=" * 20)
completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=messages
)
# 通过reasoning_content字段打印思考过程
print("=" * 20 + "思考过程" + "=" * 20)
print(completion.choices[0].message.reasoning_content)
# 通过content字段打印最终答案
print("=" * 20 + "最终答案" + "=" * 20)
print(completion.choices[0].message.content)
