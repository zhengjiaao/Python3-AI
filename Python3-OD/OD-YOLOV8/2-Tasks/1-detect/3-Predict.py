from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load an official model 加载官方模型模型
# model = YOLO("path/to/best.pt")  # load a custom model 加载自定义模型

# Predict with the model 使用模型结果进行预测
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image 在图像上预测
print(results)
