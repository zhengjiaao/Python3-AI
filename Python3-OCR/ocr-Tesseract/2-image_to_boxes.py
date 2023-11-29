import pytesseract
from pytesseract import Output

try:
    from PIL import Image
except ImportError:
    import Image

print("=========获取文字位置信息:=========")

print(pytesseract.image_to_boxes(Image.open('data/zh.png'), output_type=Output.STRING, lang='chi_sim'))
print("#" * 30)
print(pytesseract.image_to_data(Image.open('data/zh.png'), output_type=Output.STRING, lang='chi_sim'))
