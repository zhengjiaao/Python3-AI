from ultralytics import Explorer

# 资源管理器应用程序接口（Explorer API）可用于探索具有高级语义、矢量相似性和 SQL 搜索等功能的数据集。
# 它还能利用 LLM 的强大功能，根据图像内容使用自然语言搜索图像。
# 探索者应用程序接口允许您编写自己的数据集探索笔记本或脚本，以深入了解您的数据集。

# create an Explorer object
exp = Explorer(data="coco8.yaml", model="yolov8n.pt")
exp.create_embeddings_table()

similar = exp.get_similar(img="https://ultralytics.com/images/bus.jpg", limit=10)
print(similar.head())

# Search using multiple indices
similar = exp.get_similar(
    img=["https://ultralytics.com/images/bus.jpg", "https://ultralytics.com/images/bus.jpg"], limit=10
)
print(similar.head())


# 参数细节：
# - img: 要搜索的图像路径或 URL。
# - limit: 返回相似图像的数量。
# - index: 使用的索引。默认为 "embeddings"。
# - model: 用于计算相似度的模型。默认为 "yolov8n.pt"。
# - device: 用于计算相似度的设备。默认为 "cpu"。
# - batch_size: 用于计算相似度的批大小。默认为 1。
# - verbose: 是否打印进度。默认为 False。
# - show_progress: 是否显示进度条。默认为False。
