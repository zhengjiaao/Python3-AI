from paddlespeech.cli.vector import VectorExecutor

# 声纹提取：工业级声纹提取工具。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用

vec = VectorExecutor()
result = vec(audio_file="zh.wav")
print(result)  # 187维向量

# 输出结果：
# [ -0.19083306   9.474295   -14.122263    -2.0916545    0.04848729
#    4.9295826    1.4780062    0.3733844   10.695862     3.2697146
#   -4.48199     -0.6617882   -9.170393   -11.1568775   -1.2358263 ...]
