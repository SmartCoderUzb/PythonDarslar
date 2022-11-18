from utils.db import User

def user_serializer(user:User) -> dict:
    result = {}
    result[user.user_id]={}
    for key,value in user.__dict__.items():
        if not key.startswith('__'):
            result[user.user_id][key]=value
    return result