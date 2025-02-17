from ultralytics import YOLO

# 导出模式用于将YOLOv8 模型导出为可用于部署的格式。在此模式下，模型将转换为其他软件应用程序或硬件设备可以使用的格式。
# 在将模型部署到生产环境时，该模式非常有用。

# model = YOLO("yolov8n.pt")
model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.pt")

# Export to ONNX 创建yolov8n.onnx，导出路径默认是yolov8n.pt路径的同级目录
model.export(format="onnx", dynamic=True)  # 默认为False, True动态模式下，输入大小可以改变，但是速度会慢

# Export to ONNX with GPU
# model.export(format="onnx", device=0)

# Load the exported ONNX model
onnx_model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.onnx")

# Run inference
# results = onnx_model("https://ultralytics.com/images/bus.jpg")
results = onnx_model("D:\\temp\\yolov8\\data\\images\\bus.jpg")
# results = onnx_model(source="D:\\temp\\yolov8\\data\\images\\bus.jpg", save=True)

print(results)

# 参数细节：
# format: 模型导出格式，支持"torchscript", "onnx", "openvino", "engine", "saved_model", "pb", "tflite", "pbtext", "coreml"
# device: 导出模型使用的设备，支持"cpu", "cuda", "ipu", "hpu", "ort", "openvino", "vulkan", "metal", "ideep", "xnnpack"
# half: 是否使用半精度浮点数导出模型，默认为False
# dynamic: 是否使用动态大小导出模型，默认为False
# simplify: 是否使用简化导出模型，默认为False
# opset: 导出模型使用的ONNX操作集版本，默认为12
# optimize: 是否使用优化导出模型，默认为False
