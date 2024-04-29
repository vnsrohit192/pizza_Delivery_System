from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"Rohit",
                "email":"kathakmadhav@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }



class Settings(BaseModel):
    authjwt_secret_key:str='
eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTcxNDQxNTMxMSwiaWF0IjoxNzE0NDE1MzExfQ.G9UXgYsbc_0XNZaZJw2nmfo6PNMFlAdIopO66iNZepg'


class LoginModel(BaseModel):
    username:str
    password:str



class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }
