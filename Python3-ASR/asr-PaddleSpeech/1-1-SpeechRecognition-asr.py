import paddle
from paddlespeech.cli.asr.infer import ASRExecutor

# 语音识别：中文语音识别。

# 安装 注意版本
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

asr_executor = ASRExecutor()
result = asr_executor(audio_file="wav/zh.wav", device=paddle.get_device())
print(result)  # 输出结果：我认为跑步最重要的就是给我带来了身体健康
