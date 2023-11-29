import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

# 列出支持的语言
print(pytesseract.get_languages(config=''))

# 正确识别中英文
print("=========文字识别小例子:=========")
print(pytesseract.image_to_string(Image.open('data/en.png'), lang='eng'))
print(pytesseract.image_to_string(Image.open('data/zh.png'), lang='chi_sim'))
print(pytesseract.image_to_string(Image.open('data/en_zh.png'), lang='chi_sim+eng'))