__author__ = 'srv'

import pymongo
import json


class Demographic(object,):
    def __init__(self):
        self.json_array = []
        self.connection_string = "mongodb://arm:uc458FJ3@50.84.62.186/arm"
        self.connection = pymongo.MongoClient(self.connection_string)
        self.database = self.connection.arm

    def get_data(self):
        collection = self.database.association_definition
        demo_data = collection.find({},{"_id":0})

        for data in demo_data:
            self.json_array.append(data)

    def get_json(self):
        return json.dumps(self.json_array)


if __name__ == '__main__':
    demographic_obj = Demographic()
    demographic_obj.get_data()
    print demographic_obj.get_json()
