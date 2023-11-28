import paddle
from paddlespeech.cli.asr import ASRExecutor

# 语音识别：中文语音识别。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

asr_executor = ASRExecutor()
text = asr_executor(
    model='conformer_talcs',
    lang='zh_en',
    sample_rate=16000,
    config=None,
    ckpt_path=None,
    audio_file="wav/zh.wav",
    codeswitch=True,
    force_yes=False,
    device=paddle.get_device())

print('ASR Result: \n{}'.format(text))

# ASR Result:
# 我认为跑步最重要的就是给我带来了身体健康
