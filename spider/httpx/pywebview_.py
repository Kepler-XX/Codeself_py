"""
pywebview是一个Python库，用于以GUI形式显示HTML、CSS、和JavaScript内容。
这意味着使用这个库，你可以在桌面应用程序中显示网页。



# 安装pywebview
pip install pywebview -i https://mirror.baidu.com/pypi/simple/

"""

import webview

window = webview.create_window(
    title='百度一下,全是广告',
    url='http://www.baidu.com',
    width=850,
    height=600,
    resizable=False,    # 固定窗口大小
    text_select=False,   # 禁止选择文字内容
    confirm_close=True   # 关闭时提示
)
webview.start()