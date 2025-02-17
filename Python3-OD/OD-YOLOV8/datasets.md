# datasets 数据集

    datasets 数据集 标注、制作、训练

## 数据集标注

数据集标注工具有很多，下面是推荐一些标注工具：

- [label-studio](https://github.com/HumanSignal/label-studio)
- [labelme](https://github.com/wkentaro/labelme)
- [labelimg 已归档，不维护了](https://github.com/tzutalin/labelImg)

下面使用 `labelme`进行演示：

```shell
#安装 labelme
pip install labelme

#打开工具
labelme
```

标注步骤：打开工具，选择文件夹，选择图片，选择标注类型，点击标注，点击保存。

## 数据集制作

    准备数据集：准备一个适当的标注数据集，确保你的数据集路径和标签格式与YOLOv8的要求相符。

```text
data/
-- train
    -- images
        -- 0001.jpg
        -- 0002.jpg
        -- ...
    -- labels
        -- 0001.txt
        -- 0002.txt
        -- ...
-- val
    -- images
        -- 0001.jpg
        -- 0002.jpg
        -- ...
    -- labels
        -- 0001.txt
        -- 0002.txt
        -- ...
-- test
    -- images
        -- 0001.jpg
        -- 0002.jpg
        -- ...
    -- labels
        -- 0001.txt
        -- 0002.txt
        -- ...
```

```text
data/
-- images
    -- train
        -- 0001.jpg
        -- 0002.jpg
        -- ...
    -- val
        -- 0001.jpg
        -- 0002.jpg
        -- ...
    -- test
        -- 0001.jpg
        -- 0002.jpg
        -- ...
-- labels
    -- train
        -- 0001.txt
        -- 0002.txt
        -- ...
    -- val
        -- 0001.txt
        -- 0002.txt
        -- ...
    -- test
        -- 0001.txt
        -- 0002.txt
        -- ...
```

## 使用数据集训练模型

### 1.训练一个新模型

### 2.基于现有模型再训练

