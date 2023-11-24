from paddlespeech.cli.asr.infer import ASRExecutor

# todo 未成功，complex 存在版本问题

# 语音识别：中文语音识别。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

# model_type = "transformer"
# input = "wav/zh.wav"

asr_executor = ASRExecutor()
result = asr_executor(input="wav/zh.wav")
print(result)
