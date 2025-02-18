from openai import OpenAI

# 自定义人设，来与用户进行角色扮演。
client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="<YOUR_API_KEY>"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "system",
                "content": "请你扮演一个刚从美国留学回国的人，说话时候会故意中文夹杂部分英文单词，显得非常fancy，对话中总是带有很强的优越感。"
        },
        {
                "role": "user",
                "content": "美国的饮食还习惯么。"
        }
    ]
)

print(completion.choices[0].message.content)