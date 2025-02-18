# nlp-paddlenlp-未完成

- [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP)
- [PaddleNLP 一键预测功能：Taskflow API](https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md)

## 安装

#### 环境依赖

* python >= 3.8 参考 [python 官网](https://www.python.org/downloads/)
* paddlepaddle >= 2.6.0
* 如需大模型功能，请使用 paddlepaddle-gpu >= 2.6.0

#### 安装 PaddleNLP

> 请注意，本安装过程假设您已安装好`paddlepaddle-gpu`或`paddlepaddle`（版本大于或等于3.0）。
> 如果您尚未安装 PaddlePaddle，请参考 [飞桨官网](https://www.paddlepaddle.org.cn/) 进行安装。

1. paddlepaddle 安装

```shell
# Windows CPU pip 安装：
python -m pip install paddlepaddle==2.6.2 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
python -m pip install paddlepaddle==3.0.0.dev20250113 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
```

2. paddlenlp 安装

```shell
# 安装最新版本
pip install --upgrade --pre paddlenlp
# or
pip install --upgrade paddlenlp -i https://pypi.org/simple
```

安装参考：

```shell
# 安装 paddlepaddle ，一定要注意paddlepaddle版本,按官方教程2.5.1去做适配的话，会出现识别效果很不理想情况。推荐 paddlepaddle<2.5 版本
pip3 install paddlepaddle==2.5.1
# 安装 paddlepaddle-gpu，若使用大模型功能，例如：Question Generation（QG），即问题生成。
pip3 install paddlepaddle-gpu==2.5.1
# 安装 paddlenlp
pip3 install paddlenlp==2.8.1

```

## 模型了解

* [大模型全流程工具链](https://github.com/PaddlePaddle/PaddleNLP/blob/develop/llm)，包含主流中文大模型的全流程方案。
* [精选模型库](https://github.com/PaddlePaddle/PaddleNLP/blob/develop/model_zoo)，包含优质预训练模型的端到端全流程使用。
* [丰富完备的中文模型库](https://github.com/PaddlePaddle/PaddleNLP#%E4%B8%B0%E5%AF%8C%E5%AE%8C%E5%A4%87%E7%9A%84%E4%B8%AD%E6%96%87%E6%A8%A1%E5%9E%8B%E5%BA%93)

模型默认下载位置：

```text
C:\Users\zhengjiaao\.paddlenlp\models
```

## 实例

### 一键UIE预测

PaddleNLP提供一键预测功能，无需训练，直接输入数据即可开放域抽取结果。这里以信息抽取-命名实体识别任务，UIE模型为例：

```python
from pprint import pprint
from paddlenlp import Taskflow

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

```