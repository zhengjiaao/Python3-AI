# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import requests
from http import HTTPStatus

import dashscope
from dashscope.audio.asr import Recognition

# 使用同步接口进行文件转写
# 以下示例展示使用语音识别同步API接口进行文件转写，对于对话聊天、控制口令、语音输入法、语音搜索等较短的准实时语音识别场景可考虑采用该接口进行语音识别。

# dashscope.api_key = 'your-dashscope-api-key'
dashscope.api_key = "sk-796c2eb58df24dccb67c5892a9107810"

r = requests.get(
    'https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_female2.wav'
)
with open('asr_example.wav', 'wb') as f:
    f.write(r.content)

recognition = Recognition(model='paraformer-realtime-v2',
                          format='wav',
                          sample_rate=16000,
                          callback=None)
result = recognition.call('asr_example.wav')


print(
    '[Metric] requestId: {}, first package delay ms: {}, last package delay ms: {}'
    .format(
        recognition.get_last_request_id(),
        recognition.get_first_package_delay(),
        recognition.get_last_package_delay(),
    ))

if result.status_code == HTTPStatus.OK:
    with open('asr_result.txt', 'w+') as f:
        for sentence in result.get_sentence():
            print(sentence['text'])
            f.write(str(sentence) + '\n')
    print('Recognition done!')
else:
    print('Error: ', result.message)