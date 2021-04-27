import pymongo
from bson import ObjectId
# import dns from dnspython to yuse mongodb+srv URI
import dns
# import os to get env variables
import os
# import dotenv to hide Atlas Credentials
from dotenv import load_dotenv


class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self):
        if not self._id:
            self.collection.insert(self)
        else:
            self.collection.update(
                {"_id": ObjectId(self._id)}, self)
        self._id = str(self._id)

    def reload(self):
        if self._id:
            result = self.collection.find_one({"_id": ObjectId(self._id)})
            if result:
                self.update(result)
                self._id = str(self._id)
                return True
        return False

    def remove(self):
        if self._id:
            resp = self.collection.remove({"_id": ObjectId(self._id)})
            self.clear()
            return resp


class User(Model):
    load_dotenv()  # take environment variables from .env.
    MONGODB_URI = os.environ['MONGODB_URI']

    # print(f'MONGODB_URI: {MONGODB_URI}')

    db_client = pymongo.MongoClient(MONGODB_URI)
    # db name is 'users' and collection name is 'users_list'
    collection = db_client["users"]["users_list"]

    def find_all(self):
        users = list(self.collection.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return users

    def find_by_name(self, name):
        users = list(self.collection.find({"name": name}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
# add find_by_job and find_by_name_and_job for final version

    def find_by_job(self, job):
        users = list(self.collection.find({"job": job}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users

    def find_by_name_and_job(self, name, job):
        users = list(self.collection.find({"name": name, "job": job}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
