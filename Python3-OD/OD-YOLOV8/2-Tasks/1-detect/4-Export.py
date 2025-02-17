from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load an official model 加载官方模型模型
# model = YOLO("path/to/best.pt")  # load a custom trained model 加载自定义模型

# Export the model  导出模型
model.export(format="onnx")