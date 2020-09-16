from pymongo import MongoClient
from news_service.config import CONF
from bson.json_util import dumps
from bson.json_util import loads


class PyMongo:
    __conn = None

    @staticmethod
    def getConn():
        if PyMongo.__conn is None:  # Read only once, lazy.
            PyMongo.__conn =MongoClient('mongodb://%s:%s@127.0.0.1' % (CONF.DB_UNAME, CONF.DB_PWD))
        return PyMongo.__conn

    @staticmethod
    def getData(table, key, value):
        cursor = PyMongo.getConn()[CONF.DB_NAME][table].find({key: value}, {'_id': False})
        return loads(dumps(cursor))

    @staticmethod
    def getAllData( table):
        cursor = PyMongo.getConn()[CONF.DB_NAME][table].find({}, {'_id': False})
        return loads(dumps(cursor))

    @staticmethod
    def insertData( table, data):
        print(PyMongo.getConn()[CONF.DB_NAME][table].insert(data))

    @staticmethod
    def updateData( table, keyToUpdate, valueToUpdate, searchKey, searchValue, key2, value2):
        PyMongo.getConn()[CONF.DB_NAME][table].update({searchKey:searchValue},{"$set":{keyToUpdate:valueToUpdate,key2:value2}},upsert = True)