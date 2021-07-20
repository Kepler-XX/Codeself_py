from pymysql import cursors

from kepler.db.db import get_db

# 导入get_db方法
db = get_db()

def add_db(params):

    # insert
    try:
        cursor = db.cursor(cursor=cursors.DictCursor)
        cursor.execute('insert into  person value(%s,%s,%s)',
                       (params['id'], params['name'], params['age']
                        ))
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_db(params, id):
    # update
    try:
        cursor = db.cursor(cursor=cursors.DictCursor)
        cursor.execute('update person set name=%s,age=%s where id=%s',
                       (params['name'], params['age'],id
                        ))
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def get_db(id):

    # get
    cursor = db.cursor(cursor=cursors.DictCursor)
    cursor.execute("select * from person where id=%s", id)
    # cursor.execute("select * from person")
    person_info = cursor.fetchone()
    # person_list = cursor.fetchall()
    return person_info


def delete_db(id):
    # delete
    try:
        cursor = db.cursor(cursor=cursors.DictCursor)
        cursor.execute("delete from person where id=%s", id)
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True



def get_all():
    # get
    cursor = db.cursor(cursor=cursors.DictCursor)
    cursor.execute("select * from person where id=%s", id)
    # cursor.execute("select * from person")
    person_info = cursor.fetchall()
    # person_list = cursor.fetchall()
    return person_info




params = get_all()
def insert_all(params):
    # insert
    try:
        for param in params:
            cursor = db.cursor(cursor=cursors.DictCursor)
            cursor.execute('insert into  person value(%s,%s,%s)',
                           (param['id'], param['name'], param['age']
                            ))
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True
