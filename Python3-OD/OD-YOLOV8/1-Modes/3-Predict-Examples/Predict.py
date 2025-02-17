import cv2
from PIL import Image

from ultralytics import YOLO

# 预测
# 预测模式用于使用训练有素的YOLOv8 模型对新图像或视频进行预测。在该模式下，模型从检查点文件加载，用户可以提供图像或视频来执行推理。
# 模型会预测输入图像或视频中物体的类别和位置。

# model = YOLO("yolov8n.pt")
# model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.pt")
# model = YOLO("D:\\temp\\yolov8\\models\\best.pt")
# model = YOLO("D:\\temp\\yolov8\\models\\sparrow.pt")
# model = YOLO("D:\\temp\\yolov8\\models\\pigeon.pt")
model = YOLO("D:\\temp\\yolov8\\models\\birdtype.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0") # 用于对不同类型的输入进行预测，包括摄像头（"0"）、文件夹、图片、视频等
# results = model.predict(source="folder", show=True)  # Display preds. Accepts all YOLO predict arguments 显示预览。接受所有YOLO预测论点

# 定义感兴趣的类别列表，例如只保留'person'类别，假设'person'的类别ID为0
classes = [0]  # 假设0代表'person'类别，根据实际情况调整

# from PIL
# im1 = Image.open("bus.jpg")
# im1 = Image.open("D:\\temp\\yolov8\\data\\images\\bus.jpg")
# im1 = Image.open("D:\\temp\\yolov8\\data\\images\\sparrow.jpg")
# results1 = model.predict(source=im1, save=True)  # save plotted images 保存图像(检测结果)
path_dir = "D:\\temp\\yolov8\\data\\images\\"
results1 = model.predict(source=path_dir, save=True)  # save plotted images 保存图像(检测结果)
# results1 = model.predict(source=im1, save=True, classes=classes)  # 保存图像并仅包含指定类别的检测结果
# results1 = model.predict(source=im1, save=True, classes=classes, conf=0.8)  # 保存图像并仅包含指定类别和大于指定置信度的检测结果

# from ndarray
# im2 = cv2.imread("D:\\temp\\yolov8\\data\\images\\bus.jpg")
# results2 = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels 将预测另存为标签

# from list of PIL/ndarray
# results3 = model.predict(source=[im1, im2])

# 输出结果
print(results1)
# for r in results1:
#     boxes = r.boxes  # Boxes object for bbox outputs
#     masks = r.masks  # Masks object for segment masks outputs
#     probs = r.probs  # Class probabilities for classification outputs
#     print("boxes = \n")
#     print(boxes)
#     print("masks = \n")
#     print(masks)
#     print("probs = \n")
#     print(probs)


# 更多参考：https://docs.ultralytics.com/zh/modes/predict/

# 参数细节：
# source: str, Path, list, tuple, ndarray, torch.Tensor, PIL.Image, None = None,
#     输入源，可以是图像路径、视频路径、摄像头ID、图像列表、图像元组、图像数组、图像张量、PIL图像或None。
#     如果为None，则使用摄像头。
# stream: bool = False,
#     如果为True，则将source视为流并返回一个生成器。
#     如果为False，则将source视为静态图像并返回一个列表。
# predictor:Predictor = None, 预测器，用于执行推理。
# show: bool = False,
#     如果为True，则显示预测结果。
#     如果为False，则不显示预测结果。
# save: bool = False,
#     如果为True，则保存预测结果。
#     如果为False，则不保存预测结果。
# save_txt: bool = False,
#     如果为True，则保存预测结果的标签文件。
#     如果为False，则不保存预测结果的标签文件。
# save_conf: bool = False,
#     如果为True，则保存预测结果的置信度。
#     如果为False，则不保存预测结果的置信度。
# save_crop: bool = False,
#     如果为True，则保存预测结果的裁剪图像。
#     如果为False，则不保存预测结果的裁剪图像。
# save_dir: str = 'inference/output',
#     保存预测结果的目录。
# conf: float = 0.25,
#     置信度阈值，用于过滤弱预测。
# iou: float = 0.45,
#     IOU阈值，用于过滤弱预测。
# agnostic_nms: bool = False,
#     如果为True，则执行非极大值抑制（NMS）以过滤弱预测。
#     如果为False，则不执行NMS。
# classes: list = None,
#     类别列表，用于过滤预测结果。
