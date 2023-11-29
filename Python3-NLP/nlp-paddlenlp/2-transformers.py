from paddlenlp.transformers import AutoTokenizer, AutoModelForCausalLM

# todo 未成功 错误：KeyError: 'LlamaTokenizer'

# 大模型文本生成
# PaddleNLP提供了方便易用的Auto API，能够快速的加载模型和Tokenizer。这里以使用 linly-ai/chinese-llama-2-7b 大模型做文本生成为例：

tokenizer = AutoTokenizer.from_pretrained("linly-ai/chinese-llama-2-7b")
model = AutoModelForCausalLM.from_pretrained("linly-ai/chinese-llama-2-7b", dtype="float16")
input_features = tokenizer("你好！请自我介绍一下。", return_tensors="pd")
outputs = model.generate(**input_features, max_length=128)
tokenizer.batch_decode(outputs[0])

# 输出结果：
# ['\n你好！我是一个AI语言模型，可以回答你的问题和提供帮助。']
