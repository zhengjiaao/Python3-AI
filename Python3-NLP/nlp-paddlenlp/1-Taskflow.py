from pprint import pprint
from paddlenlp import Taskflow

# todo 未成功，与paddlepaddle和python的版本有关

# 一键UIE预测：
# PaddleNLP提供一键预测功能，无需训练，直接输入数据即可开放域抽取结果。这里以信息抽取-命名实体识别任务，UIE模型为例：

schema = ['时间', '选手', '赛事名称']  # Define the schema for entity extraction

ie = Taskflow('information_extraction', schema=schema)

pprint(ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"))

# 输出结果：
# [{'时间': [{'end': 6,
#             'probability': 0.9857378532924486,
#             'start': 0,
#             'text': '2月8日上午'}],
#   '赛事名称': [{'end': 23,
#                 'probability': 0.8503089953268272,
#                 'start': 6,
#                 'text': '北京冬奥会自由式滑雪女子大跳台决赛'}],
#   '选手': [{'end': 31,
#             'probability': 0.8981548639781138,
#             'start': 28,
#             'text': '谷爱凌'}]}]
