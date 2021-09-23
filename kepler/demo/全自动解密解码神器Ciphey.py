"""
Ciphey 是一个使用自然语言处理和人工智能的全自动解密/解码/破解工具。

简单地来讲，你只需要输入加密文本，它就能给你返回解密文本。就是这么牛逼。

有了Ciphey，你根本不需要知道你的密文是哪种类型的加密，你只知道它是加密的，那么Ciphey就能在3秒甚至更短的时间内给你解密，返回你想要的大部分密文的答案

Ciphey 支持解密的密文和编码多达51种，下面列出一些基本的选项

基本密码：

Caesar Cipher

ROT47 (up to ROT94 with the ROT47 alphabet)

ASCII shift (up to ROT127 with the full ASCII alphabet)

Vigenère Cipher

Affine Cipher

Binary Substitution Cipher (XY-Cipher)

Baconian Cipher (both variants)

Soundex

Transposition Cipher

Pig Latin

现代密码学：

Repeating-key XOR

Single XOR

编码：

Base32

Base64

Z85 (release candidate stage)

Base65536 (release candidate stage)

ASCII

Reversed text

Morse Code

DNA codons (release candidate stage)

Atbash

Standard Galactic Alphabet (aka Minecraft Enchanting Language)

Leetspeak

Baudot ITA2

URL encoding

SMS Multi-tap

DMTF (release candidate stage)

UUencode

Braille (Grade 1)
"""

# 1.安装
# pip install -U ciphey

# 2. 基本使用
"""
1. 文件输入：

ciphey -f encrypted.txt
# 或
python -m ciphey -f encrypted.txt

2.不规范的方法：

ciphey -- "Encrypted input"
# 或
python -m ciphey -- "Encrypted input"


3.正常方式

ciphey -t "Encrypted input"
# 或
python -m ciphey -t "Encrypted input"



要去除进度条、概率表和所有噪音，请使用安静模式：

ciphey -t "encrypted text here" -q
"""

# 3.python调用Ciphey
"""
from ciphey.__main__ import main, main_decrypt, make_default_config
main_decrypt(make_default_config("SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl"))


不想输出概率表，只想要解密内容，代码需要这么写
from ciphey.__main__ import main, main_decrypt, make_default_config
config = make_default_config("SGVsbG8gbXkgbmFtZSBpcyBiZWUgYW5kIEkgbGlrZSBkb2cgYW5kIGFwcGxlIGFuZCB0cmVl")
config["grep"] = True
main_decrypt(config)
"""
