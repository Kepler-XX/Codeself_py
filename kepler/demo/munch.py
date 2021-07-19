"""
黑魔法库--munch 直接使用 . 操作和访问字典
安装：
pip install munch
"""
from munch import Munch

# 1.example
"""
munch有一个Munch类，它继承自原生字典，使用isinstance可以验证
"""
profile = Munch()
print(isinstance(profile, dict))  # 输出True

profile.name = 'kepler'
profile.age = 20
print(profile)   # Munch({'name': 'kepler', 'age': 20})

print(profile.name)  # kepler 等价于profile['name']
print(profile.age)   # 20   等价于profile['age']

# 2.action
##  新增元素
profile.gender = "man"
print(profile)
##  修改元素
profile.gender = "women"
print(profile)
## 删除元素
# profile.pop("gender")
# print(profile)
# del profile.age
# print(profile)

## keys
print(profile.keys())
print(profile.values())
print(profile.get('name'))


## to_json
import json
munch_obj = Munch(foo=Munch(lol=True), bar=100, msg='hello')
munch_json = json.dumps(munch_obj)
print(f'{type(munch_json)}, {munch_json}')

## to_YAML
import yaml
munch_obj1 = Munch(foo=Munch(lol=True), bar=100, msg='hello')
munch_yml = yaml.dump(munch_obj1)
print(munch_yml)
# 可以用safe_dump去掉!munch.Munch
munch_yml1 = yaml.safe_dump(munch_obj1)
print(munch_yml1)