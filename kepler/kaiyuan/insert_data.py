import uuid

from pymysql import cursors

from kepler.kaiyuan.db_connect import get_intranet_db
from kepler.kaiyuan.get_data import get_outside_db

intranet_db = get_intranet_db()


def insert_intranet_all(params):
    # insert
    try:
        for param in params:
            id = int(uuid.uuid4())
            cursor = intranet_db.cursor(cursor=cursors.DictCursor)
            cursor.execute('insert into  user_people value(%s,%s,%s,%s,%s)',
                           (id, param['name'], param['age'],param['info'], param['remark']
                            ))
    except Exception as e:
        intranet_db.rollback()
        return False
    else:
        intranet_db.commit()
        return True


if __name__ == '__main__':
    params = get_outside_db()
    insert_intranet_all(params)