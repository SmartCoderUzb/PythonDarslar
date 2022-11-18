from utils.db import User
from loader import db
from utils.serializer import user_serializer
from data.conf import users


user=User(
        ism=f'ism',
        familiya=f"familiya",
        parol=f"parol"
    )

db.write(user_serializer(user))

