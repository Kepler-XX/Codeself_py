import pymysql
from Codeself_py.db import config

from flask import g

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host=config['DATABASE_HOST'], port=config['DATABASE_PORT'],
                               user=config['DATABASE_USER'],
                               password=config['DATABASE_PASSWORD'],
                               db=config['DATABASE_DB'], charset=config['DATABASE_CHARSET'])

    return g.db