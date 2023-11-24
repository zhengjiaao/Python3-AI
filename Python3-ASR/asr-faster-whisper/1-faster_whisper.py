from faster_whisper import WhisperModel

# 识别语音文件

# 模型：越往后的模型，对硬件的要求越高，识别精度越高，当然了，速度也越慢。
# 模型下载路径：C:\Users\Administrator\.cache\huggingface ，不想用了，删掉 *.pt* 文件就行。
# [--model {small, medium, large, large-v2}]

model_size_or_path = "small"  # 模型会自动下载，位置：C:\Users\Administrator\.cache\huggingface
device = "cpu"  # 设备，可以是 cpu, cuda
compute_type = "int8"  # 计算类型，可以是 float, float16, int8, int8_float16

# Run on GPU with FP16
model = WhisperModel(model_size_or_path, device, compute_type="int8")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# audio_file = "audio.mp3"  # 音频文件的路径
# language = "Chinese"  # 语言，可以是任何 whisper 支持的语言
# output_format = "srt"  # 输出格式，可以是 txt, srt, json
# beam_size = 5  # 束搜索大小，越大越准确，但也越慢

# 使用 model.transcribe 方法来对音频文件进行转写。您可以指定音频文件的路径、语言、输出格式、束搜索大小等参数
segments, info = model.transcribe("wav/zh.wav", beam_size=5)  # 该方法会返回一个包含转写结果的 segments 列表，以及一个包含语言信息的 info 对象。

# 打印这些结果
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# todo 若开启打印，则不能输出到文件中
# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

# 也可以将转写结果保存到文件中
output_file = "tmp/output.srt"  # 输出文件的路径

with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))  # 打印这些结果
        f.write(segment.text + "\n")  # 把结果输出到文件
