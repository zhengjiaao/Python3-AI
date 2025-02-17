from ultralytics import YOLO

# Val 模式用于在YOLOv8 模型训练完成后对其进行验证。在该模式下，模型在验证集上进行评估，以衡量其准确性和泛化性能。
# 该模式可用于调整模型的超参数，以提高其性能。

# Load a YOLOv8 model
# model = YOLO("yolov8n.yaml")
model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.pt")

# Train the model
# model.train(data="coco8.yaml", epochs=5)
model.train(data="D:\\temp\\yolov8\\cfg\\datasets\\coco8.yaml", epochs=5)

# Validate on training data
model.val()

# 参数细节：
# model.val() 函数用于在训练数据集上进行验证。
# 该函数会根据模型在验证集上的表现进行评估，并输出相关的评估指标。
# 评估指标包括：
# - mAP50：平均精度（平均正确率）
# - mAP50-95：平均精度（平均正确率）
# - F1：F1分数
# - Precision：精确率
# - Recall：召回率
# - mAP：平均精度（平均正确率）
# - Class_AP：每个类别的AP
# - Class_F1：每个类别的F1分数
# - Class_Recall：每个类别的召回率
# - Class_Precision：每个类别的精确率
