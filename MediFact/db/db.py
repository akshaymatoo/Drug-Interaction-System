import pymongo

class DbConnection(object):

    def __init__(self):
        self.connection_string = ""
        self.connection = pymongo.MongoClient(self.connection_string)
        self.database = self.connection.arm

    def getConnection(self):
        return self.database

