from paddlespeech.cli.text.infer import TextExecutor
import paddle

# todo 未成功

# 文本标点恢复：一键恢复文本标点，可与ASR模型配合使用。

# 安装
# pip install paddlepaddle
# pip install pytest-runner
# pip install paddlespeech

# Python应用
text_punc = TextExecutor()
# result = text_punc(text="今天的天气真不错啊你下午有空吗我想约你一起去吃饭")
result = text_punc(text='今天的天气真不错啊你下午有空吗我想约你一起去吃饭', task='punc', model='ernie_linear_p7_wudao',
                   lang='zh', config=None, ckpt_path=None, punc_vocab=None, device=paddle.get_device())
print(result)  # 输出结果：今天的天气真不错啊！你下午有空吗？我想约你一起去吃饭。
