# Question Generation（QG），即问题生成，指的是给定一段上下文，自动生成一个流畅且符合上下文主题的问句。问题生成通常可以分为，无答案问题生成和有答案问题生成，这里只关注应用更广的有答案问题生成。
# PaddleNLP提供开箱即用的产业级NLP预置任务能力，无需训练，一键预测。

# todo 未成功

# 支持单条、批量预测

from paddlenlp import Taskflow

# 默认模型为 unimo-text-1.0-dureader_qg
question_generator = Taskflow("question_generation")
# 单条输入
question_generator([
    {
        "context": "奇峰黄山千米以上的山峰有77座，整座黄山就是一座花岗岩的峰林，自古有36大峰，36小峰，最高峰莲花峰、最险峰天都峰和观日出的最佳点光明顶构成黄山的三大主峰。",
        "answer": "莲花峰"}
])
