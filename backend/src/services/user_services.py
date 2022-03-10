

from typing import List
from repos.user_db import users_db
from models.user import User

def get_users() -> List[User]:
    return list(users_db.values())

def get_user(id:int) -> User:
    return users_db.get(id, None)

def create_user(name:str) -> User:
    user = User(len(users_db), name)
    users_db[user.id] = user
    return user
