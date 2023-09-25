

from pydantic.v1 import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


# SignUp

class UserSchema(BaseModel):
    fullname: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Zaxriddinov Mexriddin",
                "email": "zaxriddinov1707@gmail.com",
                "password": "17071707"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "zaxriddinov1707@gmail.com",
                "password": "17071707"
            }
        }