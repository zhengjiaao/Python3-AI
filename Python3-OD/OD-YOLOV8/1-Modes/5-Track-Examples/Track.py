from ultralytics import YOLO

# 跟踪模式用于使用YOLOv8 模型实时跟踪物体。在该模式下，模型从检查点文件加载，用户可以提供实时视频流来执行实时物体跟踪。
# 该模式适用于监控系统或自动驾驶汽车等应用。

# Load a model
# model = YOLO("yolov8n.pt")  # load an official detection model
model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.pt")
# model = YOLO("yolov8n-seg.pt")  # load an official segmentation model
# model = YOLO("path/to/best.pt")  # load a custom model

# Track with the model
# results = model.track(source="D:\\temp\\yolov8\\data\\mp4\\pedestrian.mp4")
results = model.track(source="D:\\temp\\yolov8\\data\\mp4\\pedestrian.mp4",
                      show=True)  # show=True 在执行跟踪的同时，会实时显示视频画面，包含跟踪结果
# results = model.track(source="D:\\temp\\yolov8\\data\\mp4\\pedestrian.mp4",
#                       show=True,
#                       save=True)  # save: 是否保存跟踪结果
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True) # 使用默认追踪器进行追踪
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml") # 使用ByteTrack追踪器进行追踪

# 更多参考：https://docs.ultralytics.com/zh/modes/track/

# 参数细节：
# source: 输入视频路径，可以是本地路径、网络路径、摄像头ID等。支持的网络格式：mp4、avi、mov、mkv、webm、m4v、mpeg、mpg、wmv、flv、m3u8等。
# stream: 是否为流模式，默认为False。设置为True时，将使用cv2.VideoCapture()函数打开视频流，而不是读取本地文件。
# show: 是否显示跟踪结果，默认为False。设置为True时，将显示跟踪结果。
# save: 是否保存跟踪结果，默认为False。设置为True时，将保存跟踪结果到本地文件。
# persist: 是否持续跟踪，默认为False。设置为True时，将持续跟踪。
