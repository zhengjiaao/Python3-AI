# 基于现有的模型再训练模型

# 1. 在Python中基于YOLOv8模型进行再训练

# 1.1 基础环境：安装Ultralytics ： pip install ultralytics

# 1.2 导入必要的库
from ultralytics import YOLO

# 1.3 加载预训练模：加载YOLOv8的预训练模型。这里以YOLOv8n为例，它是YOLOv8系列中较小的一个模型，适合快速实验
model = YOLO('yolov8n.pt')  # 加载预训练模型

# 1.4 准备数据集：准备一个适当的标注数据集，确保你的数据集路径和标签格式与YOLOv8的要求相符。

# 1.5 配置训练参数：在开始训练之前，通过修改模型的参数来定制训练过程，比如学习率、批次大小、迭代次数等。
model.train(data='path/to/your/data.yaml',
            epochs=100,
            batch=16,
            imgsz=640,
            workers=4,
            name='custom_yolov8n')
# data: 数据集配置文件的路径。替换'path/to/your/data.yaml'等占位符为实际的文件路径
# epochs: 训练轮数。
# batch: 批次大小。
# imgsz: 输入图像的大小。
# workers: 加载数据时使用的线程数。
# name: 训练结果的保存名称。

# 1.6 继续训练（可选）：如果你之前已经训练过一个模型，并希望在其基础上继续训练，可以加载之前的最佳权重文件继续训练。
model = YOLO('path/to/previous/best.pt')
model.train(data='path/to/your/data.yaml', epochs=8)

# 1.7 评估和测试模型:训练完成后，你可以使用以下代码来评估模型性能：
results = model.val()

# 1.8 并且可以对单个图片或视频进行推理测试：

# 对图片进行推理
model.predict(source='path/to/image.jpg', save=True)

# 对视频进行推理
model.predict(source='path/to/video.mp4', save=True)
