import logging
import redis
from elasticsearch import Elasticsearch
from mongoengine import connect
from pymongo import MongoClient
from sqlalchemy import create_engine
import constant
import pymysql

# 开发数据库的配置信息
# 连接mongodb
MongoClient_conn = MongoClient('106.14.206.19', 9060)
# MongoClient_conn = MongoClient('47.103.76.222', 19060)
# 连接ES
es = Elasticsearch('106.14.206.19:9200')
# es = Elasticsearch('47.103.76.222:19070')
# 连接Redis
redis_store = redis.StrictRedis(host='106.14.206.19',
                                port=6379,
                                decode_responses=True,
                                encoding_errors='ignore')
# 连接Mysql
mysql_engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
    'Code', 'Codex', '106.14.206.19', '3306', 'test1'),
                             encoding='utf-8',
                             echo=False,
                             pool_pre_ping=True,
                             pool_recycle=3600)

mysql_db_conf = {
    'host': '106.14.206.19',
    'user': 'kepler',
    'password': '123456',
    'db': 'Codex'
}

# 配置mongoengine连接  模型驱动引擎
connect('scientific_research', host='47.103.69.221', port=19060)  # 开发服务器

_index = "index1"
_type = "index_type1"
template_index = 'index_type1_template'

# 系统默认常量
# 默认分页大小
constant.DEFAULT_PAGE_SIZE = 10
# 默认缓存时间,单位：秒(s)
constant.REDIS_EXP_TIME = 60 * 30



class Config(object):
    """工程配置信息"""
    SECRET_KEY = "e2kTfQUs81VvWECj9TvC/+kq3oEjpNVSNQTyGiujeyCM6xX9Yjq52v54g+HVoknA"
    DEBUG = False
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG
    # 中文输出
    JSON_AS_ASCII = False


class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    LOG_LEVEL = logging.ERROR

"""
import os


class Config(object):
    DEBUG = True
    JWT_ENABLE = True
    JWT_SECRET = "test of kepler copy rights"
    JWT_ALGORITHM = "HS256"
    JWT_EXP_TIME = 60 * 36  # min
    ESCAPE_PATH = ['/api/inneruser/login',
                   '/api/inneruser/auth',
                   '/api/inneruser/code_login',
                   '/api/inneruser/dd_code_login',
                   '/api/monitor/alarm',
                   '/api/monitor/user',
                   '/api/monitor/user/clockin',
                   '/api/monitor/user/query_history',
                   '/api/logs/push',
                   '/api/logalarm/send_alarm_message',
                   '/api/config/create_file',
                   '/api/document/download_attachment',
                   '/api/document/verify',
                   '/api/document/get_share',
                   '/api/alarmnotice/receive',
                   '/api/job/jobs',
                   '/api/job/jobs/delete',
                   '/api/job/jobs/bulk/remove',
                   '/api/server/download_file',
                   '/api/sshlog/clean_log',
                   '/api/git/backups',
                   '/api/apid/download_file',
                   '/api/job/auto_sync_source',
                   '/api/job/auto_elb_source',
                   '/api/job/auto_sync_git_info',
                   '/api/job/auto_save_slow_sql',
                   '/api/job/auto_save_apig_sql',
                   '/api/job/update_jenkins_redis',
                   '/api/job/resource_expiration_alarm',
                   '/api/domain/get_expire_time',
                   '/api/job/auto_save_weblog_sql']
    # LOG_PATH = "/var/log/devops_log/"
    # LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    # LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    # FILE_PATH = "/files/apifiles/"
    JENKINS_JOB_TIME = 5  # 秒
    SOURCE_EXPIRE_DAY = 30  # 秒
    HUAWEICLOUD = {
        1: {
            'ENDPOINT': "cn-north-1",
            'USERNAME': "xiaohei2018",
            'PASSWORD': "P@ssw0rd",
            'PROJECTID': "96b3d3a55d184f23ace3d293a4105109",
            'USERDOMAINID': "90cbc5d6dffb41eebc631a503e3f479a",
            'Key': "VCVE6GQYD6FVVY4C849H",
            'Secret': "LFUHQ5rh8F61uVSZpB2WATPbMIHRt6xRkx8nDjRc"
        },
        2: {
            'ENDPOINT': "cn-north-1",
            'USERNAME': "krsk2021",
            'PASSWORD': "P@ssw0rd",
            'PROJECTID': "0ba4fc4ec70025682f9ac014e8b7eced",
            'USERDOMAINID': "0ba4fc4d0000f5e10f91c014cf536100",
            'Key': "IW2TAHUXUNKM6LZQOCK7",
            'Secret': "1rIqtY3B8GTZ3BJYih5C20L4iZtZnQpCv0GsuHTm"
        }
    }
    QYVX_CORPID = "ww034a686694a8c386"
    QYVX_CORPSECRET = "-acoTrmlEIiwXm7HVuQMcex_nvrqWBJnq1SFOik48Fw"
    QYVX_AGENTID = 1000008
    NA_AGENTID = 1171396979
    ES_HOSTS = {'host': '127.0.0.1', 'port': '9200'}
    ES_LOG_INDEXS = 'logging-*'
    COMMON_AUTH = "Jpc3MiOiJkZXZvcHMiLCJpYXQiOjE1OTgzNjk0MzAsImV4cCI"
    DOCUMENT_ATTACHMENT_SAVE_PATH = '/netdisk/'


class DevConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 3306
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = '111111'
    DATABASE_DB = 'kepler'
    DATABASE_CHARSET = 'utf8'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 14
    REDIS_PASSWORD = 'pass'
    RADISH_URL = 'http://127.0.0.1:9001/kepler/api/'
    MONITOR_URL = 'http://127.0.0.1:8080'


class TestConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 3306
    DATABASE_USER = 'kepler'
    DATABASE_PASSWORD = '123456'
    DATABASE_DB = 'kepler'
    DATABASE_CHARSET = 'utf8'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 12
    REDIS_PASSWORD = '123456'
    RADISH_URL = 'http://127.0.0.1:9001/kepler/api/'
    MONITOR_URL = 'http://127.0.0.1:8080'


class ProdConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = 3306
    DATABASE_USER = 'kepler'
    DATABASE_PASSWORD = '123456'
    DATABASE_DB = 'kepler'
    DATABASE_CHARSET = 'utf8'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 7
    REDIS_PASSWORD = '123456'
    RADISH_URL = 'http://127.0.0.1:9001/kepler/api/'
    MONITOR_URL = 'http://127.0.0.1:8080'


configs = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
"""

#test