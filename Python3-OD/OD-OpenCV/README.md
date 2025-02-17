# OD-OpenCV

    OpenCV 

## 安装

```shell
pip3 install opencv-python
```

为了确保 OpenCV 正确安装，我们可以运行以下示例来展示如何读取和显示图像

```python
import cv2 as cv

# 将path/to/image改为图片的真实路径，然后运行此 demo
img = cv.imread("path/to/image")

cv.imshow("Display window", img)
k = cv.waitKey(0)  # Wait for a keystroke in the window 等待窗口中的按键
```