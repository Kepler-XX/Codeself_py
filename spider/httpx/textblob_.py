"""
TextBlob是一个用于处理文本数据的Python库，仅为英文分析。


中文则可以使用SnowNLP，能够方便的处理中文文本内容，是受到了TextBlob的启发而写的。


下面就给英文做一个拼写检查

"""
from textblob import TextBlob

a = TextBlob("I dream about workin with goof company")
a = a.correct()
print(a)

"""
结果如下。
I dream about working with good company
可以看到，句子中的单词被更正了。
"""