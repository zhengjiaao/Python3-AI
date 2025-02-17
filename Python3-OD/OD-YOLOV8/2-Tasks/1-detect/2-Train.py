from ultralytics import YOLO

# Load a model 加载一个模型模型
model = YOLO("yolov8n.yaml")  # build a new model from YAML 从 YAMLmodel 构建一个新模型
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training) 加载一个预训练模型（推荐用于训练）
model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights 从 YAML 构建并传递权重

# Train the model 训练模型结果
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
