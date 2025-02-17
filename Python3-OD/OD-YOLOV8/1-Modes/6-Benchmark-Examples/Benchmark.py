from ultralytics.utils.benchmarks import benchmark

# 基准模式用于分析YOLOv8 中各种导出格式的速度和准确性。
# 基准模式提供的信息包括导出格式的大小、其 mAP50-95 指标（用于物体检测和分割）或 accuracy_top5 度量（用于分类），以及不同导出格式（如ONNX,OpenVINO,TensorRT 等）下每幅图像的推理时间（以毫秒为单位）。
# 这些信息可以帮助用户根据他们对速度和准确性的要求，为他们的特定使用案例选择最佳的导出格式。

# Benchmark
# benchmark(model="yolov8n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)
benchmark(model="D:\\temp\\yolov8\\models\\yolov8n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)

# 参数细节：
# 1. model：要评估的模型路径或名称。
# 2. data：用于评估的数据集路径或名称。
# 3. imgsz：输入图像的大小。
# 4. half：是否使用半精度浮点数。
# 5. device：要使用的设备。 可以是整数（表示GPU编号）或字符串（表示设备名称）。
