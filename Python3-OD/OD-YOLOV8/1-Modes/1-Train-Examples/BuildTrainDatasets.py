import json
import os
import shutil
import glob
import math
import yaml


# 构建训练数据集

def copy_and_rename_files(source_directory, target_directory, extension):
    """根据扩展名进行拷贝文件，并重命名"""
    # 确保目标目录存在，如果不存在则创建
    os.makedirs(target_directory, exist_ok=True)

    # 获取源目录下指定扩展名的所有文件，不包括子目录中的文件
    files = glob.glob(os.path.join(source_directory, f'*{extension}'))

    # 对文件进行排序，确保按预期顺序处理
    files.sort()

    for index, file_path in enumerate(files, start=1):
        # 获取文件名和扩展名，这里直接通过传入的extension变量获取，因为已筛选
        new_name = f"{index}{extension}"
        new_file_path = os.path.join(target_directory, new_name)

        # 复制文件到目标目录并重命名，保留原文件
        shutil.copy2(file_path, new_file_path)
        print(f"Copied and renamed file '{file_path}' to '{target_directory}/{new_name}'")


def convert_box(img_size, box):
    """坐标转换：将json的坐标转换为yolo的坐标转换后xy为中心点坐标，wh为框的宽和高"""
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 * dw
    y = (box[1] + box[3]) / 2.0 * dh
    w = (box[2] - box[0]) * dw
    h = (box[3] - box[1]) * dh

    return x, y, w, h


def process_json_file(json_file_path, classify_map):
    """处理单个JSON文件并转换为TXT"""
    txt_file_path = os.path.splitext(json_file_path)[0] + ".txt"

    with open(json_file_path, 'r', encoding='utf-8') as json_file:  # 打开json文件
        data = json.load(json_file)

    with open(txt_file_path, 'w') as txt_file:
        h, w = data['imageHeight'], data['imageWidth']  # 获取图片宽高
        for item in data['shapes']:
            classify = classify_map.get(item['label'], 'unknown')
            points = item['points']
            x1, y1 = min(points[0][0], points[1][0]), min(points[0][1], points[1][1])
            x2, y2 = max(points[0][0], points[1][0]), max(points[0][1], points[1][1])
            bbox = convert_box((w, h), (x1, y1, x2, y2))
            txt_file.write(f"{classify} {' '.join(map(str, bbox))}\n")
        print(f"Conversion JSON to TXT：{json_file_path} --> {txt_file_path}")


def json2txt(path, classify_map, extension):
    """遍历目录下的JSON文件并转换为TXT"""
    count = 0
    try:
        files = os.listdir(path)
        for file in files:
            if file.endswith(extension):
                json_file_path = os.path.join(path, file)
                process_json_file(json_file_path, classify_map)
                count += 1
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
    else:
        print(f"共将 {count} 个json文件转成---->txt文件")


def process_data_dir(data_dir, images_extension):
    """
    处理数据目录，将图片和标签文件分别拷贝到images和labels目录
    :param data_dir: 数据目录
    :param images_extension: 图片格式(.jpg/.png/...)
    :return: images_dir, labels_dir
    """
    images_dir = os.path.join(data_dir, 'images')
    labels_dir = os.path.join(data_dir, 'labels')

    print(f"开始拷贝图片 文件到 '{labels_dir}'")
    copy_and_rename_files(data_dir, images_dir, images_extension)

    print(f"开始拷贝TXT 文件到 '{labels_dir}'")
    copy_and_rename_files(data_dir, labels_dir, '.txt')

    return images_dir, labels_dir


def split_dataset(image_filenames, ratios, include_test=True):
    """
    动态分配数据集为训练集、验证集和可选的测试集。

    :param image_filenames: 图像文件名列表
    :param ratios: 数据集分配比例字典，如 {'train': 0.7, 'val': 0.2, 'test': 0.1}
    :param include_test: 是否包含测试集，默认为True
    :return: 分配好的数据集字典
    """
    total_count = len(image_filenames)
    adjusted_ratios = {}

    # 确保训练集和验证集的分配
    # 初始分配，使用math.floor()取整
    adjusted_ratios['train'] = math.floor(total_count * ratios['train'])
    adjusted_ratios['val'] = math.floor(total_count * ratios['val'])

    # 如果包含测试集，直接计算测试集数量
    if include_test:
        adjusted_ratios['test'] = total_count - (adjusted_ratios['train'] + adjusted_ratios['val'])
    else:
        # 如果不包含测试集，先累加训练和验证的分配，然后处理余数
        total_allocated = adjusted_ratios['train'] + adjusted_ratios['val']
        remainder = total_count - total_allocated

        # 分配余数，这里简单平均分配到训练和验证集，根据实际需求可调整策略
        adjusted_ratios['train'] += math.floor(remainder / 2)
        adjusted_ratios['val'] += math.ceil(remainder / 2)  # 确保余数被完全分配

        del ratios['test']

    # 再次检查总和
    assert sum(
        adjusted_ratios.values()) == total_count, "Adjusted dataset counts do not sum up to the total file count."

    return adjusted_ratios


def setup_directories(dir_paths):
    """确保所有指定的目录存在"""
    for dir_path in dir_paths:
        os.makedirs(dir_path, exist_ok=True)


def copy_files(src_path, dst_path):
    """复制单个文件，增加异常处理"""
    try:
        shutil.copy(src_path, dst_path)
        print(f"复制文件 {src_path} 到 {dst_path}")
    except FileNotFoundError:
        print(f"警告：源文件 {src_path} or 目标文件 {dst_path} 未找到，跳过复制。")
    except Exception as e:
        print(f"复制文件时发生错误：{e}")


def assign_files_to_datasets(images_dir, labels_dir, datasets_dir, ratios, images_extension):
    """将图像文件和标签文件分配到不同的数据集"""

    print(f"开始分配文件到数据集")

    # 定义输出目录路径
    output_dirs = {
        'train': {'images': os.path.join(datasets_dir, 'train', 'images'),
                  'labels': os.path.join(datasets_dir, 'train', 'labels')},
        'val': {'images': os.path.join(datasets_dir, 'val', 'images'),
                'labels': os.path.join(datasets_dir, 'val', 'labels')},
        'test': {'images': os.path.join(datasets_dir, 'test', 'images'),
                 'labels': os.path.join(datasets_dir, 'test', 'labels')}
    }

    # 确保所有输出目录存在
    setup_directories([dir_path for sub_dict in output_dirs.values() for dir_path in sub_dict.values()])

    # 定义数据集划分比例 推荐比例：80%训练集，20%验证集 or 70%训练集，20%验证集，10%测试集
    # ratios = {'train': 0.7, 'val': 0.2, 'test': 0.1}
    # 获取所有图像文件名
    image_filenames = [os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith(images_extension)]
    # 动态调整比例以适应实际文件数量，优先保证训练集和验证集，剩余归测试集(忽略测试集时，测试集会归到验证集)
    adjusted_ratios = split_dataset(image_filenames, ratios, include_test=True)  # include_test=False 不包括测试集

    # 遍历所有图像文件，根据索引分配到不同的数据集
    for i, filename in enumerate(image_filenames):
        # 根据当前索引确定数据集类别
        accumulated_count = 0
        for key, count in adjusted_ratios.items():
            accumulated_count += count
            if i < accumulated_count:
                set_key = key
                break

        # 根据set_key复制文件到相应目录，这部分逻辑与您之前的实现类似
        src_image_path = os.path.join(images_dir, filename + images_extension)
        dst_image_path = os.path.join(output_dirs[set_key]['images'], filename + images_extension)
        copy_files(src_image_path, dst_image_path)

        # 检查并复制标签文件
        src_label_path = os.path.join(labels_dir, filename + '.txt')
        if os.path.exists(src_label_path):  # 确保标签文件存在
            dst_label_path = os.path.join(output_dirs[set_key]['labels'], filename + '.txt')
            copy_files(src_label_path, dst_label_path)
        else:
            print(f"警告：找不到对应的标签文件 {src_label_path}")

    print(f"分配文件完成")


def create_yaml_file(datasets_root_dir, classify_map):
    print(f"开始构建配置文件")
    setup_directories([datasets_root_dir])

    names_map = {value: key for key, value in classify_map.items()}

    yaml_config = {
        'path': datasets_root_dir,
        'train': 'train/images',
        'val': 'val/images',
        'test': 'test/images',
        'nc': len(classify_map),
        'names': names_map
    }

    with open(os.path.join(datasets_root_dir, 'data.yaml'), 'w') as f:
        yaml.dump(yaml_config, f)
        print(f"配置文件已保存到 {os.path.join(datasets_root_dir, 'data.yaml')}")
    print(f"构建配置文件完成")


def flip_map(map_to_flip):
    """
    翻转字典中的键和值，并转换为列表，每个元素格式为 "value : key"。

    参数:
    map_to_flip (dict): 需要翻转的字典。

    返回:
    list: 包含翻转后键值对字符串的列表。
    """
    flipped_list = [f"{value}: {key}" for key, value in map_to_flip.items()]
    return flipped_list


def buildDatasets(data_dir, datasets_root_dir, classify_map, ratios, images_extension):
    """
    构建数据集
    :param data_dir: 数据目录
    :param datasets_dir: 数据集目录
    :param classify_map: 类别映射
    :param ratios: 数据集划分比例,推荐比例：80%训练集，20%验证集 or 70%训练集，20%验证集，10%测试集
    :param images_extension: 图片格式（全部图片格式需一致）
    :return:
    """

    print(f"开始构建数据集")

    # 转换json文件为txt文件
    json2txt(data_dir, classify_map, ".json")

    # 拷贝图片和标签文件分别到images、labels目录
    images_dir, labels_dir = process_data_dir(data_dir, images_extension)

    # 构建数据集
    assign_files_to_datasets(images_dir, labels_dir, datasets_root_dir, ratios, images_extension)

    # 构建配置文件
    create_yaml_file(datasets_root_dir, classify_map)

    print(f"数据集构建完成")


# 定义参数

# 定义数据目录
# data_dir = "D:\\temp\\yolov8\\datasets\\sparrow_data"
# data_dir = "D:\\temp\\yolov8\\datasets\\pigeon_data"
data_dir = "D:\\temp\\yolov8\\datasets\\birdtype_data"
# 定义数据集目录
# datasets_root_dir = "D:\\temp\\yolov8\\datasets\\sparrow"
# datasets_root_dir = "D:\\temp\\yolov8\\datasets\\pigeon"
datasets_root_dir = "D:\\temp\\yolov8\\datasets\\birdtype"
# 定义图片格式
images_extension = ".jpg"
# 定义类别映射
classify_map = {
    "sparrow": 0,
    "pigeon": 1
}

# 定义数据集划分比例 推荐比例：80%训练集，20%验证集 or 70%训练集，20%验证集，10%测试集
ratios = {'train': 0.8, 'val': 0.2, 'test': 0.0}

buildDatasets(data_dir, datasets_root_dir, classify_map, ratios, images_extension)

# 训练模型
# def train_model(model_dir, data_dir, epochs, batch_size, lr, weights):
#     print(f"开始训练模型")
#     setup_directories([model_dir])
#     cmd = f"python train.py --data {data_dir} --epochs {epochs} --batch {batch_size} --lr {lr} --weights {weights}"
#     os.system(cmd)
#     print(f"模型训练完成")
#     print(f"模型保存到 {model_dir}")


