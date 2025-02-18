# coding=utf-8

import sys

import dashscope
from dashscope.audio.tts import SpeechSynthesizer

# 将合成音频保存为文件

# dashscope.api_key = 'your-dashscope-api-key'
dashscope.api_key = "sk-796c2eb58df24dccb67c5892a9107810"

result = SpeechSynthesizer.call(model='sambert-zhichu-v1',
                                text='今天天气怎么样',
                                sample_rate=48000)
print('requestId: ', result.get_response()['request_id'])
if result.get_audio_data() is not None:
    with open('output.wav', 'wb') as f:
        f.write(result.get_audio_data())
    print('SUCCESS: get audio data: %dbytes in output.wav' %
          (sys.getsizeof(result.get_audio_data())))
else:
    print('ERROR: response is %s' % (result.get_response()))
