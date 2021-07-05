"""
人民网

"""
import uuid
import pymysql


class PeopleWebSpider(object):

    def __init__(self):
        self.db_host = '106.14.206.19'
        self.db_port = 3306
        self.db_username = 'root'
        self.db_password = '123456'
        self.db_db = 'kepler'

    def get_param(self):
        params = {
            "id": str(uuid.uuid4()),
            "name": "kepler",
            "age": 20,
            "info": "111",
            "remark": "222"
        }
        return params

    def connect_db(self):
        db = pymysql.connect(host=self.db_host,
                             port=self.db_port,
                             user=self.db_username,
                             password=self.db_password,
                             db=self.db_db
                             )
        return db

    def add_db(self):
        db = self.connect_db()
        params = self.get_param()
        print(params)
        try:
            cursor = db.cursor()
            cursor.execute('insert into user_people value(%s,%s,%s,%s,%s)',
                           (params['id'], params['name'], params['age'], params['info'], params['remark']))
        except Exception as e:
            print(e)
            db.rollback()
            return False
        else:
            db.commit()
            print("insert success")
            return True


if __name__ == '__main__':
    c = PeopleWebSpider()
    db = c.connect_db()
    c.add_db()
    print(db)
    print("aaa")