from ultralytics import YOLO

# 例如，用户可以加载一个模型，训练它，在验证集上评估它的性能，甚至只需几行代码就可以将其导出为ONNX格式。
# For example, users can load a model, train it, evaluate its performance on a validation set, and even export it to ONNX format with just a few lines of code.

# Load a model 加载模型
model = YOLO("yolov8n.yaml")  # build a new model from scratch 从头开始构建新模型
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training) 加载预先训练的模型（建议用于训练）

# Use the model 使用模型
model.train(data="coco8.yaml", epochs=3)  # train the model 训练模型
metrics = model.val()  # evaluate model performance on the validation set 在验证集上评估模型性能
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image 对图像进行预测
path = model.export(format="onnx")  # export the model to ONNX format 将模型导出为ONNX格式
