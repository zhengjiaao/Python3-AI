# Qwen

- [阿里百炼大模型 官网](https://bailian.console.aliyun.com/)
- [阿里百炼大模型 创建 API_KEY](https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key)
- [阿里百炼大模型 API 文档](https://help.aliyun.com/zh/model-studio/developer-reference/use-qwen-by-calling-api?spm=a2c4g.11186623.0.0.53971d1cbmDiEX)
- [阿里百炼大模型 模型列表](https://help.aliyun.com/zh/model-studio/getting-started/models)

## 安装Python依赖

确保你已经安装了Python 3.8或更高版本。你可以从[Python官方](https://www.python.org/downloads/)网站下载并安装。

```shell
pip3 install openai
pip3 install dashscope
pip3 install pyaudio
# or
pip install -r requirements.txt
```

## Qwen API 示例

简单示例-场景：对话

```python
import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    # api_key=os.getenv("DASHSCOPE_API_KEY"), # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    api_key="sk-796c2eb58df24dccb67c5892a9107654", # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}
    ]
)
print(completion.choices[0].message.content)
```