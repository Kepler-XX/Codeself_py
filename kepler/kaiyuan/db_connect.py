import pymysql

from kepler.kaiyuan import config


def get_outside_db():
    outside_d = pymysql.connect(host=config.DATABASE_OUTSIDE_HOST, port=config.DATABASE_OUTSIDE_PORT,
                                user=config.DATABASE_OUTSIDE_USER,
                                password=config.DATABASE_OUTSIDE_PASSWORD,
                                db=config.DATABASE_OUTSIDE_DB, charset=config.DATABASE_OUTSIDE_CHARSET)

    return outside_d


def get_intranet_db():
    intranet_db = pymysql.connect(host=config.DATABASE_INTRANET_HOST, port=config.DATABASE_INTRANET_PORT,
                                  user=config.DATABASE_INTRANET_USER,
                                  password=config.DATABASE_INTRANET_PASSWORD,
                                  db=config.DATABASE_INTRANET_DB, charset=config.DATABASE_INTRANET_CHARSET)

    return intranet_db
