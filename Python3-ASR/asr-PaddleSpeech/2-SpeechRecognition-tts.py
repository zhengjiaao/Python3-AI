from paddlespeech.cli.tts.infer import TTSExecutor
# import paddle

# 语音合成：中文语音合成，输出 24k 采样率wav格式音频。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

tts = TTSExecutor()
tts(text="今天天气十分不错。", output="output.wav")
