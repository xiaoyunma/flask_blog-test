#encoding:utf-8
# HOST='192.168.1.123:5000'
import os
#URI = 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'
DIALECT='mysql'
DRIVER='pymysql'
USERNAME='root'
PASSWORD='1234'
HOST='127.0.0.1'
PORT='3306'
DATABASE='myblog'
SQLALCHEMY_DATABASE_URI='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,
                                            USERNAME,PASSWORD,HOST,PORT,DATABASE )

SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG=True
SECRET_KEY = os.urandom(24)