from openai import OpenAI

# 提供一个场景，让模型模拟该场景下的任务对话
client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="<YOUR_API_KEY>"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "user",
                "content": "假设诸葛亮死后在地府遇到了刘备，请模拟两个人展开一段对话。"
        }
    ]
)

print(completion.choices[0].message.content)