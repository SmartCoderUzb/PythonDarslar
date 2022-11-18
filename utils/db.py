from data.conf import *
import json
from utils.generator import id_generator

generator = id_generator()

class Database:
    def __init__(self,path=db_path):
        self.path=path
        self.db = None

    def connect(self, mode):
        self.db = open(self.path,mode)
        return
    def write(self,data):
        json_data = self.read()
        json_data.update(data)
        self.connect('w')
        self.db.write(
            json.dumps(json_data, indent=4)
        )
        self.close()
    def read(self):
        self.connect('r')
        read=json.loads(
            self.db.read()
        )
        self.close()
        return read
    def close(self):
        self.db.close()
    

class User:
    __admin_parol = 3241
    def __init__(self, ism, familiya, parol):
        self.user_id=next(generator)
        self.ism=ism
        self.familiya=familiya
        self.parol=parol
        self.__is_admin = False
    
    def make_admin(self,parol):
        if User.__admin_parol==parol:
            self.__is_admin=True
    
    def __repr__(self):
        return str(self.user_id)
