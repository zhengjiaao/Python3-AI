# coding=utf-8

import dashscope
from dashscope.audio.tts_v2 import *

# 将合成音频保存为文件（非流式合成）

# dashscope.api_key = "your-dashscope-api-key"
dashscope.api_key = "sk-796c2eb58df24dccb67c5892a9107810"
model = "cosyvoice-v1"
voice = "longxiaochun"


def sample_call():
    synthesizer = SpeechSynthesizer(model=model, voice=voice)

    audio = synthesizer.call("今天天气怎么样？")
    print('requestId: ', synthesizer.get_last_request_id())
    with open('output.mp3', 'wb') as f:
        f.write(audio)


if __name__ == '__main__':
    sample_call()
