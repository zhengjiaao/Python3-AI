# OD-YOLOV8

* [YOLOV8 官网](https://docs.ultralytics.com/zh)
* [YOLOV8 官网中文](https://docs.ultralytics.com/zh)
* [YOLOV8 官网中文 快速开始](https://docs.ultralytics.com/zh/quickstart/)

## YOLOV8 安装

方式1：pip安装，安装速度快，无法更改源码

```shell
# 从PyPI安装ultralytics包
pip install ultralytics

# or

# 从GitHub安装ultralytics包,如果你想要最新的开发版本
pip install git+https://github.com/ultralytics/ultralytics.git@main
```

方式2：按源码安装，可以更改源码

```shell
# 克隆ultralytics仓库
git clone https://github.com/ultralytics/ultralytics
 
# 进入克隆的目录
cd ultralytics
 
# 为开发安装可编辑模式下的包
pip install -e .
```

## YOLOV8 验证安装成功

```shell
yolo help
yolo checks
yolo version
yolo settings
yolo copy-cfg
yolo cfg
```

## YOLOV8 CLI Examples

- [YOLOv8 CLI Docs](https://docs.ultralytics.com/usage/cli)

```shell
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
# or
yolo predict model=yolov8n.pt imgsz=640 conf=0.25

# Predict 使用经过训练的YOLOv8n模型对图像进行预测
## 使用官方的YOLOv8n模型
yolo detect predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
## 使用自定义模型
yolo detect predict model=path/to/best.pt source='https://ultralytics.com/images/bus.jpg'
```

video

```shell
yolo detect predict model=yolov8x.pt source='input/video_1.mp4' show=True
# or 一样的
yolo task=detect mode=predict model=yolov8x.pt source='input/video_1.mp4' show=True
```

Predict

## YOLOV8 Python Examples

- [YOLOv8 Python Docs](https://docs.ultralytics.com/usage/python)

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco8.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
```

## YOLOV8 模型

- [YOLOV8 模型列表](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models)

### YOLOV8 模型下载

```bash
yolo mode download yolov8n.pt
```

### YOLOV8 模型训练

```bash
yolo mode train data=/home/yang/data/coco128.yaml model=yolov8n.pt epochs=10
```

### YOLOV8 模型预测

```bash
yolo mode predict model=yolov8n.pt source=/home/yang/data/coco128/image/train/
```

### YOLOV8 模型评估

```bash
yolo mode val model=yolov8n.pt data=/home/yang/data/coco128.yaml
```

### YOLOV8 模型导出

```bash
yolo mode export model=yolov8n.pt format=onnx
yolo mode export model=yolov8n.pt format=engine
```

## 代码示例

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(data='coco128.yaml', epochs=10)
results = model.val()
# results = model.predict(source='bus.jpg')
# results = model.export(format='engine')
# results = model.export(format='onnx')
# results = model.export(format='openvino')
# results = model.export(format='coreml')
# results = model.export(format='saved_model')
# results = model.export(format='pb')
# results = model.export(format='tflite')
# results = model.export(format='engine')
```

