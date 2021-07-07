from kepler.db.db import get_mongodb

mon = get_mongodb()

# 插入数据
"""
user = {"name": "kepler",
        "age": 20,
        "info": "kepler",
        "remark": "...for my remark"}
mon.insert_one(user)
"""

# 插入多条数据
"""
user_l = [{
        "name": "zhangsan",
        "age": 17,
        "info": "kepler",
        "remark": "...for my remark"
},
    {
        "name": "lisi",
        "age": 21,
        "info": "kepler",
        "remark": "...for my remark"
},
    {
        "name": "wangwu",
        "age": 22,
        "info": "kepler",
        "remark": "...for my remark"
    }
]
mon.insert_many(user_l)
"""
### insert()方法，若新增数据的主键已存在，则会抛出org.springframework.dao.DuplicateKeyException 异常提示主键重复，不保存当前数据。
### 插入数据还有sava()方法，它自身提供插入和更新操作，需要看传入的是什么值
    # 1. 参数不带_id
        # Mongodb插入一条新数据，会自动为你生成一个默认的objectid作为_id
    # 2. 参数带_id, 但是找不到存在的文档
        # Mongodb插入一条新数据，但是不会生成_id
    # 3. 参数带_id,同时有存在的文档
        # Mongodb会更新文档

# 查询数据

nm = mon.estimated_document_count()  # 该表数据总数

mongo_list = mon.find() # 可增加筛选条件
for i in mongo_list:
    print(i)


# 更新数据
"""
mon.update_one({"name":"zhangsan"},{
        "$set":{"age":26}
})
"""


# 删除数据

"""mon.delete_one({"name":"wangwu"}) """
### 在 MongoDB 中，remove 和 deleteOne 以及 deleteMany 都用于删除文档记录。但是，remove 函数返回的删除的结果的 WriteResult，而 delete 函数返回的是 bson 格式。
### 其中 remove 是根据参数 justOne 来判断是删除所有匹配的文档记录还是仅仅删除一条匹配的文档记录，默认是删除所有的匹配的记录。
### deleteOne 函数仅仅删除一条匹配的文档记录，而 deleteMany 函数是删除所有的匹配的文档记录。


# 聚合操作
# if __name__ == '__main__':
#     print(mon)