from paddlespeech.cli.cls.infer import CLSExecutor

# 声音分类：适配多场景的开放领域声音分类工具，基于 AudioSet 数据集 527 个类别的声音分类模型。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

cls = CLSExecutor()
result = cls(audio_file="zh.wav")
print(result)  # 输出结果：Speech 0.9027186632156372
