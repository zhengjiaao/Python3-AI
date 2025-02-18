# DeepSeek

- [DeepSeek](https://www.deepseek.com/)
- [DeepSeek 创建 api_key ](https://platform.deepseek.com/api_keys)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
- [DeepSeek API 文档详情](https://api-docs.deepseek.com/zh-cn/guides/multi_round_chat)
- [DeepSeek 提示库-样例](https://api-docs.deepseek.com/zh-cn/prompt-library/)
- [DeepSeek 其他资源-实用集成](https://github.com/deepseek-ai/awesome-deepseek-integration/tree/main)

## 安装Python依赖

确保你已经安装了Python 3.8或更高版本。你可以从[Python官方](https://www.python.org/downloads/)网站下载并安装。

```shell
pip3 install openai
# or
pip install -r requirements.txt
```

## DeepSeek API 示例

#### 对话 API

简单示例-场景：多轮对话

```python
from openai import OpenAI

# DeepSeek API 是一个“无状态” API，即服务端不记录用户请求的上下文，用户在每次请求时，需将之前所有对话历史拼接好后，传递给对话 API。
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "What's the highest mountain in the world?"}]
# messages = [{"role": "user", "content": "世界上最高的山是什么?"}]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

messages.append(response.choices[0].message)
print(f"Messages Round 1: {messages}")

# Round 2
messages.append({"role": "user", "content": "What is the second?"})
# messages.append({"role": "user", "content": "第二个是什么?"})
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

messages.append(response.choices[0].message)
print(f"Messages Round 2: {messages}")
```

简单示例-场景：个人助手

```python
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
```

#### 推理 API

推理-非流式：

```python
from openai import OpenAI

# client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages
)

reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content

# Round 2
messages.append({'role': 'assistant', 'content': content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages
)
# ...
```

流式-推理：

```python
from openai import OpenAI

# client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=True
)

reasoning_content = ""
content = ""

for chunk in response:
    if chunk.choices[0].delta.reasoning_content:
        reasoning_content += chunk.choices[0].delta.reasoning_content
    else:
        content += chunk.choices[0].delta.content

# Round 2
messages.append({"role": "assistant", "content": content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=True
)
# ...
```


