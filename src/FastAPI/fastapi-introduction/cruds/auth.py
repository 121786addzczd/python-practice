from datetime import datetime, timedelta
import hashlib
import base64
import os
from jose import jwt
from sqlalchemy.orm import Session
from schemas import UserCreate
from models import User


ALGORITHM = "HS256"
# openssl rand -hex 32 コマンドで生成したもの 
SECRET_KEY = "687bbf7126811df4cd1b55ebc8dfe9d6619832830a34a75544e67371c4ba89ad"


def create_user(db: Session, user_create: UserCreate):
    salt = base64.b64encode(os.urandom(32))
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", user_create.password.encode(), salt, 1000
    ).hex()

    new_user = User(
        username=user_create.username,
        password=hashed_password,
        salt=salt.decode()
    )
    db.add(new_user)
    db.commit()

    return new_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None

    hashed_password = hashlib.pbkdf2_hmac(
        "sha256",password.encode(), user.salt.encode(), 1000
    ).hex()
    if user.password != hashed_password:
        return None

    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    expires = datetime.now() + expires_delta
    payload = {"sub": username, "id": user_id, "exp": expires}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)