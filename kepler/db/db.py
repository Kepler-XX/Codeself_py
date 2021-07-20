import pymysql
from pymongo import MongoClient


from kepler.db import config


def get_db():
    db = pymysql.connect(host=config.DATABASE_HOST, port=config.DATABASE_PORT,
                         user=config.DATABASE_USER,
                         password=config.DATABASE_PASSWORD,
                         db=config.DATABASE_DB, charset=config.DATABASE_CHARSET)

    return db


def get_mongodb():
    conn = MongoClient(host=config.MONGODB_HOST, port=config.MONGODB_PORT)
    db = conn.kepler  # 创建数据库，如不存在，则自动创建
                        # 创建集合，若不存在，则自动创建

    return db