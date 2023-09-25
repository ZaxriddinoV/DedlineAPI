from fastapi import FastAPI, Body
from sqlalchemy.testing.suite.test_reflection import users

from auth_bearer import JWTBearer
app = FastAPI()
from models import  UserSchema, UserLoginSchema
from auth_handler import signJWT

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    user.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

