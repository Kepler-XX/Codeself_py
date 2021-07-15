# encoding: utf-8

# 中英文互译

# 以下是将简单句子从英语翻译中文
from translate import Translator


test = """
pycatia was primarily created to access the CATIA API Measurable object and it’s methods without the need of visual basic / CATScripts. There is further functionaliy available which can be seen by looking at the examples provided and reading the API at pycatia.readthedocs.io.

Some of the methods can be accessed simply using the pywin32 module but further access to methods such as GetCOG do not seem to be accessible using pure python. There are several questions on stack overflow and the pywin32 mailing list regarding this. But, they fail to provide any working examples with the VB Measurable object in python.

pycatia accesses these methods by running VBA scripts using the Dispatch(‘CATIA.Application’).SystemService.Evaluate() function where required and passing a small public function to it. Otherwise, pycatia uses the VB method directly but exposes it within the same python class.

This has currently only been tested in CATIA V5 R21.
"""
translator= Translator(to_lang="chinese")
translation = translator.translate(test)
print(translation)

# 在任何两种语言之间，中文翻译成英文
translator= Translator(from_lang="chinese", to_lang="english")
translation = translator.translate("我想你")
print(translation)


