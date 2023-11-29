# ocr-Tesseract

- [tesseract-ocr 官网文档](https://tesseract-ocr.github.io/tessdoc/Installation.html)
- [tesseract-ocr GitHub](https://link.zhihu.com/?target=https%3A//github.com/tesseract-ocr/tesseract)
- [pytesseract python依赖](https://github.com/madmaze/pytesseract)
- [Pillow python依赖](https://github.com/python-pillow/Pillow)
- [pytesseract 集成Tesseract-OCR 引擎](https://zhuanlan.zhihu.com/p/448253254?utm_id=0)

## 安装

1、先下载安装tesseract

* [windows tesseract下载](https://github.com/UB-Mannheim/tesseract/wiki)
* [Mac和Linux tesseract下载](https://tesseract-ocr.github.io/tessdoc/Installation.html)

2、Python安装依赖

```shell
# pip安装pytesseract
pip install pytesseract
# 用于图像处理
pip install Pillow
```

3、检查环境

```shell
tesseract --version
pip show pytesseract
pip show Pillow
```

4、训练数据（可选地）

如果需要其他语言包，可以下载: [训练数据](https://tesseract-ocr.github.io/tessdoc/Data-Files)
Tesseract 提供了三种训练数据：

| 训练数据                                                            | 	训练模型         | 	识别速度 | 	正确率             |
|-----------------------------------------------------------------|---------------|-------|------------------|
| [tessdata](https://github.com/tesseract-ocr/tessdata)           | LSTM          | 	中等   | 略低于tesdata -best |
| [tessdata_best](https://github.com/tesseract-ocr/tessdata_best) | LSTM          | 最慢    | 	最高              |
| [tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast) | Legacy + LSTM | 最快    | 最低               |

将下载的模型文件`traineddata` 文件放在 `C:\Program Files\Tesseract-OCR\tessdata` 目录（Tesseract安装目录）下就可以了。

仅`tessdata_best`
模型可用来再训练字库，训练方法参考文档：[Tesseract-4- 注：5已经弃用了这种训练方式](https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html)

新训练方式参考：[Tesseract5-tesstrain](https://github.com/tesseract-ocr/tesstrain)

## 实例

测试数据下载：[pytesseract tests/data](https://github.com/madmaze/pytesseract/tree/master/tests/data)

### 文字识别小例子

准备一张包含英文字符的图片，下面的代码实现提取图片中的中文和英文字符，并识别为字符串：

```python
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

# 列出支持的语言
print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('en.png'), lang='chi_sim+eng'))
```
