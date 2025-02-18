# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

# client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
client = OpenAI(api_key="sk-62aa54bcf5b2478e88c4bcd4c6d852d1", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        # 系统角色：可以根据系统角色输入的语言，来判断回答的内容是 `英文or中文`
        # {"role": "system", "content": "You are a helpful assistant"},
        {"role": "system", "content": "你是个乐于助人的助手"},

        # 用户角色
        # {"role": "user", "content": "Hello"},
        {"role": "user", "content": "你好"},
    ],
    stream=False
)

print(response.choices[0].message.content)
