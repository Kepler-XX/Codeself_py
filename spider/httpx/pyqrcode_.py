"""
二维码简称QR Code(Quick Response Code)，学名为快速响应矩阵码，是二维条码的一种。由日本的Denso Wave公司于1994年发明。

现随着智能手机的普及，已广泛应用于平常生活中，例如商品信息查询、社交好友互动、网络地址访问等等。

pyqrcode模块则是一个QR码生成器，使用简单，用纯python编写

# 安装pyqrcode
pip install pyqrcode -i https://mirror.baidu.com/pypi/simple/

"""

import pyqrcode
import png
from pyqrcode import QRCode


inpStr = "www.baidu.com"
qrc = pyqrcode.create(inpStr)
qrc.png("baidu.png", scale=6)