from ultralytics import YOLO

# 训练
# 训练模式用于在自定义数据集上训练YOLOv8 模型。在该模式下，模型使用指定的数据集和超参数进行训练。
# 训练过程包括优化模型参数，使其能够准确预测图像中物体的类别和位置。

# 加载模型
# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from YAML 从YAML构建一个新模型
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training) 加载预先训练的模型（建议用于训练）
# model = YOLO("yolov8s.yaml").load("yolov8s.pt")  # build from YAML and transfer weights 根据YAML构建并传递权重
# model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights 根据YAML构建并传递权重
# model = YOLO(model="D:\\temp\\yolov8\\models\\yolov8n.pt")  # pass any model type

# 训练模型
# Train the model
# results = model.train(epochs=5)
# results = model.train(data="coco8.yaml", epochs=5)
# results = model.train(data="D:\\temp\\yolov8\\cfg\\datasets\\coco8.yaml", epochs=3)
# results = model.train(data="D:\\temp\\yolov8\\datasets\\sparrow\\data.yaml", epochs=10, batch=2)
# results = model.train(data="D:\\temp\\yolov8\\datasets\\pigeon\\data.yaml", epochs=10, batch=2)
results = model.train(data="D:\\temp\\yolov8\\datasets\\birdtype\\data.yaml", epochs=300, batch=64, device=[0],
                      resume=True)

# 1.单 GPU 和 CPU 训练模型

# 在图像大小为 640 的 COCO8 数据集上对YOLOv8n 进行 100 次训练。可以使用 device 参数。如果没有传递参数，GPU device=0 将被使用，否则 device='cpu' 将被使用。
# 设备自动确定。如果 GPU 可用，则使用 GPU，否则将使用 CPU 开始训练。
# Train the model
# results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
# results = model.train(data="D:\\temp\\yolov8\\cfg\\datasets\\coco8.yaml", epochs=3, imgsz=640)

# 2.多 GPU 训练模型

# 多 GPU 训练通过在多个 GPU 上分配训练负载，可以更有效地利用可用的硬件资源。
# 要启用多 GPU 训练，请指定要使用的 GPU 设备 ID。
# Train the model with 2 GPUs
# results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])
# results = model.train(data="D:\\temp\\yolov8\\cfg\\datasets\\coco8.yaml", epochs=3, imgsz=640, device=[0, 1])

# 3.恢复中断的训练模型
# Resume training
# results = model.train(resume=True)


# 更多参考：https://docs.ultralytics.com/modes/train/

# 参数细节：
# - `epochs`：训练的轮数。默认为 300 轮。训练越长，模型性能越好，但训练时间越长。
# - `batch`：训练时每个批次的大小。默认为 64。训练越小，模型性能越好，但训练时间越短。
# - `imgsz`：输入图像的大小。 默认为 640x640。 训练越小，模型性能越好，但训练时间越短。
# - `data`：数据集的配置文件路径。默认为 "coco128.yaml"。
# - `weights`：预训练模型的权重路径。默认为 "yolov8n.pt"。
# - `device`：训练设备。默认为 "cpu"。 可选值为 "cpu"、"cuda"、"mps"、"ipu"、"hpu"、"tpu"、"auto"。
# - `project`：训练结果的保存路径。 默认为 "runs/train"。
# - `name`：训练结果的保存名称。 默认为 "exp"。
# - `exist_ok`：如果结果目录已存在，是否覆盖。 默认为 False。
# - `resume`：是否从上次中断的地方继续训练。 默认为 False。
# - `save`：是否保存训练结果。 默认为 True。
# - `save_period`：每隔多少轮保存一次训练结果。 默认为 -1，表示每轮保存一次。
# - `save_json`：是否保存JSON格式的评估结果。 默认为 True。
# - `cache`：是否缓存数据集。 默认为 False。
# - `amp`：是否使用自动混合精度训练。 默认为 False。
# - `sync_bn`：是否使用同步BN。 默认为 False。
# - `workers`：加载数据时的工作线程数。 默认为 8。
# - `optimizer`：优化器类型。 默认为 "sgd"。
# - `lr0`：初始学习率。 默认为 0.01。
# - `lrf`：学习率衰减因子。 默认为 1.0。
# - `momentum`：动量。 默认为 0.937。
# - `weight_decay`：权重衰减。 默认为 0.0005。
# - `warmup_epochs`：预热轮数。 默认为 3.0。
# - `warmup_momentum`：预热时的动量。 默认为 0.8。
# - `warmup_bias_lr`：预热时的偏置学习率。 默认为 0.01。
# - `box`：框损失权重。 默认为 0.05。
# - `cls`：类别损失权重。 默认为 0.5。
# - `cls_pw`：类别损失权重的乘积。 默认为 1.0。
# - `obj`：目标损失权重。 默认为 1.0。
# - `obj_pw`：目标损失权重的乘积。 默认为 1.0。
# - `iou_t`：IOU阈值。 默认为 0.5。
# - `anchor_t`：锚点大小阈值。
# - `fl_gamma`：Focal loss gamma。
# - `hsv_h`：HSV颜色空间中的色调变化。
# - `hsv_s`：HSV颜色空间中的饱和度变化。
# - `hsv_v`：HSV颜色空间中的亮度变化。
# - `degrees`：旋转角度变化。 默认为 0.0。
# - `translate`：平移变化。 默认为 0.0。
# - `scale`：缩放变化。 默认为 0.0。
# - `shear`：剪切变化。 默认为 0.0。
# - `perspective`：透视变化。 默认为 0.0。
# - `flipud`：上下翻转概率。 默认为 0.0。
# - `fliplr`：左右翻转概率。 默认为 0.5。
# - `mosaic`：Mosaic数据增强概率。 默认为 1.0。
# - `mixup`：Mixup数据增强概率。 默认为 0.0。
# - `copy_paste`：Copy-Paste数据增强概率。 默认为 0.0。
# - `rect`：是否使用矩形训练。 默认为 False。
# - `patience`：验证集损失停止下降的耐心轮数。 默认为 3。
# - `freeze_epochs`：冻结层的训练轮数。 默认为 1。
# - `freeze_backbone`：是否冻结骨干网络。 默认为 False。
# - `freeze_detect`：是否冻结检测器。 默认为 False。
# - `freeze_norm`：是否冻结BN层。 默认为 False。
# - `freeze_bn`：是否冻结BN层。 默认为 False。
# - `freeze_backbone_norm`：是否冻结骨干网络的BN层。
# - `freeze_backbone_detect`：是否冻结骨干网络的检测器。
# - `freeze_backbone_norm_detect`：是否冻结骨干网络的BN层和检测器。
# - `freeze_backbone_norm_detect_bn`：是否冻结骨干网络的BN层、检测器和BN层。
