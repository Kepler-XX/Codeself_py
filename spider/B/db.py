from pymysql import cursors

from kepler.db.db import get_db, get_mongodb

db = get_db()
mongo = get_mongodb()
#
# print(f'{db}')
# print(f'{mongo}')


def insert_mon(param):
    try:
        mongo.douban.insert_many(param)
    except Exception as e:
        print(f'{e}')
    else:
        return