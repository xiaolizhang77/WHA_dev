# -*- coding: utf-8 -*-
from PIL import Image

# 打开 JPEG 图像
jpeg_image = Image.open("logo.jpeg")

# 定义图标的尺寸列表
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# 将图像保存为 ICO 格式，并指定尺寸
jpeg_image.save("logo.ico", format="ICO", sizes=icon_sizes)

print("转换完成：logo.ico")
