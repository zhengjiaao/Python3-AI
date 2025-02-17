# 训练新模型：基于训练集从头训练一个新模型

# 训练YOLOv8模型以识别新的类别或适应特定场景，你需要从零开始创建一个新的模型配置并准备相应的数据集。

# 1. 安装Ultralytics YOLOv8库：pip install ultralytics

# 2. 准备数据集：按照YOLOv8的数据格式要求准备你的数据集，这通常包括：
# 图像文件：组织在指定的文件夹内。
# 标注文件：每个图像对应一个.txt文件，内容为物体类别ID和边界框坐标。

# 3. 创建数据配置文件，创建一个data.yaml文件来描述你的数据集结构、类别等信息。例如：
"""
# data.yaml 示例
train: path/to/train/images  # 训练图像的目录
val: path/to/validation/images  # 验证图像的目录
nc: 3  # 类别数量
names: ['class1', 'class2', 'class3']  # 类别名称列表
"""

# 4. 加载并训练模型: 使用YOLOv8的load()函数加载预训练的模型，然后使用train()函数进行训练。例如：
import torch
from ultralytics import YOLO

# 初始化模型，选择模型类型，如'yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x'
model = YOLO('yolov8n.yaml')  # 从配置文件初始化模型，而非预训练权重

# 开始训练，指定数据配置文件和训练参数
# results = model.train(data='path/to/data.yaml',
results = model.train(data='D:\\temp\\yolov8\\datasets\\sparrow\\sparrow.yaml',
                      epochs=20,
                      batch=16,
                      imgsz=640,
                      workers=4,
                      project='runs_train',
                      name='my_exp',
                      device='')  # 设定GPU设备，如'0'或'0,1,2,3'用于多GPU训练

# 训练结束后，最佳模型将自动保存在指定的'project/name'目录下
# 注意事项：
# 确保data.yaml文件中的路径正确无误。
# epochs、batch、imgsz等参数需根据你的硬件资源和需求进行调整。
# device参数用于指定训练所用的GPU，留空或设置为device='cpu'可在CPU上训练，但速度会慢很多。
