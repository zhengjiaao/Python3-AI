import os

# 请确保你的数据集按照Yolo要求的格式进行组织，即所有的图片在一个文件夹内，所有的标签文件与对应的图片文件名相同，且位于一个文件夹内。
# 这段代码将遍历两个数据集的图片和标签，并将它们添加到imgs和labels列表中。
# 然后，你可以根据需要进一步处理这些数据，例如将它们保存到新的文件中，或者用在训练中。

# 假设有两个数据集的路径
dataset_path1 = 'path/to/your/dataset1'
dataset_path2 = 'path/to/your/dataset2'

# 创建用于存储合并后图片和标签的列表
imgs = []
labels = []

# 合并图片和标签
for folder in ['images', 'labels']:
    for root, dirs, files in os.walk(os.path.join(dataset_path1, folder)):
        for file in files:
            img_path = os.path.join(root, file)
            imgs.append(img_path)
            label_name = file.replace('.jpg', '.txt').replace('.png', '.txt')
            label_path = os.path.join(os.path.dirname(root), 'labels', label_name)
            labels.append(label_path)

    for root, dirs, files in os.walk(os.path.join(dataset_path2, folder)):
        for file in files:
            img_path = os.path.join(root, file)
            imgs.append(img_path)
            label_name = file.replace('.jpg', '.txt').replace('.png', '.txt')
            label_path = os.path.join(os.path.dirname(root), 'labels', label_name)
            labels.append(label_path)

# 此时，`imgs` 和 `labels` 包含了来自两个数据集的所有图片和标签路径
# 你可以将它们保存到新的文件中，或者直接用在训练中
