from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
# 加载预训练的COCO模型
model = YOLO("./models/yolov8n.pt")

# Display model information (optional)
# 模型信息
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
# 训练模型在COCO8示例数据集上，共100个周期
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
# 在“bus.jpg”图像上使用YOLOv8n模型运行推理
results = model("./path/to/bus.jpg")
