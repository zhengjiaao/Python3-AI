## asr-PaddleSpeech-未成功

- [PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech)
- [PaddleSpeech 语音合成音频示例](https://paddlespeech.readthedocs.io/en/latest/tts/demo.html)

## 安装（win未成功）

> PaddleSpeech 依赖于 paddlepaddle(依赖python)

```shell
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech
```

## 快速开始

> 安装完成后，开发者可以通过命令行或者 Python 快速开始，命令行模式下改变 --input 可以尝试用自己的音频或文本测试，支持 16k
> wav 格式音频。

### 测试音频示例下载

```text
wget -c https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav
wget -c https://paddlespeech.bj.bcebos.com/PaddleAudio/en.wav
```

### 语音识别

> 开源中文语音识别

命令行：

```shell
paddlespeech asr --lang zh --input zh.wav
```

Python API 一键预测：

```python
from paddlespeech.cli.asr.infer import ASRExecutor

asr = ASRExecutor()
result = asr(audio_file="zh.wav")
print(result)
```
