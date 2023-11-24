import whisper

# 识别语音文件

# 模型：越往后的模型，对硬件的要求越高，识别精度越高，当然了，速度也越慢。
# 模型下载路径：C:\Users\Administrator\.cache\whisper ，不想用了，删掉 *.pt* 文件就行。
# [--model {tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}]

# 实例1：识别mp3语音文件，中文内容。使用模型了medium
model = whisper.load_model("base")  # 注：模型会自动下载，位置：C:\Users\{Administrator}\.cache\whisper
result = model.transcribe("mp3/audio.mp3")
print(result["text"])  # 输出结果：歌曲内容很多
