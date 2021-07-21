import uuid

from pymysql import cursors

from kepler.kaiyuan.db_connect import get_outside_db


# 导入get_db方法
outside_db = get_outside_db()


def get_outside_db():
    # get
    # TODO  表名
    cursor = outside_db.cursor(cursor=cursors.DictCursor)
    cursor.execute("select * from user_people") #
    # cursor.execute("select * from person")
    person_info = cursor.fetchall()
    # person_list = cursor.fetchall()
    return person_info

