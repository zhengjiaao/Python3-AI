from funasr import infer

# 实时语音识别

# 注：chunk_size为流式延时配置，[0,10,5]表示上屏实时出字粒度为10*60=600ms，未来信息为5*60=300ms。每次推理输入为600ms（采样点数为16000*0.6=960），输出为对应文字，最后一个语音片段输入需要设置is_final=True来强制输出最后一个字。
p = infer(model="paraformer-zh-streaming", model_hub="ms")

chunk_size = [0, 10, 5]  # [0, 10, 5] 600ms, [0, 8, 4] 480ms
param_dict = {"cache": dict(), "is_final": False, "chunk_size": chunk_size, "encoder_chunk_look_back": 4,
              "decoder_chunk_look_back": 1}

import torchaudio

speech = torchaudio.load("asr_example_zh.wav")[0][0]
speech_length = speech.shape[0]

stride_size = chunk_size[1] * 960
sample_offset = 0
for sample_offset in range(0, speech_length, min(stride_size, speech_length - sample_offset)):
    param_dict["is_final"] = True if sample_offset + stride_size >= speech_length - 1 else False
    input = speech[sample_offset: sample_offset + stride_size]
    rec_result = p(input=input, param_dict=param_dict)
    print(rec_result)
