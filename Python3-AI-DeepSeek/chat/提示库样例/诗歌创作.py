from openai import OpenAI

# 让模型根据提示词，创作诗歌
client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="<YOUR_API_KEY>"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "user",
                "content": "模仿李白的风格写一首七律.飞机"
        }
    ]
)

print(completion.choices[0].message.content)