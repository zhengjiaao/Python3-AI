from funasr import infer

# 非实时语音识别


# 注：model_hub：表示模型仓库，ms为选择modelscope下载，hf为选择huggingface下载。
p = infer(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc", model_hub="ms")

res = p("wav/zh.wav", batch_size_token=5000)
print(res)
