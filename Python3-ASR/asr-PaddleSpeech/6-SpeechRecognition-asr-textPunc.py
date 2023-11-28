import paddle
from paddlespeech.cli.asr import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor

# todo 未成功

# 视频字幕生成：是把语音识别 + 标点恢复同时使用。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用
asr_executor = ASRExecutor()
text_executor = TextExecutor()

text = asr_executor(audio_file='zh.wav', device=paddle.get_device())
result = text_executor(text=text, task='punc', model='ernie_linear_p3_wudao', device=paddle.get_device())
print('Text Result: \n{}'.format(result))
