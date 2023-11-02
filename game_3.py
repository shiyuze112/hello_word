import pyqrcode
# 设置二维码信息
s = "https://www.bilibili.com"
# 生成二维码
url = pyqrcode.create(s)
# 保存二维码
url.svg("哔哩哔哩.svg", scale=8)