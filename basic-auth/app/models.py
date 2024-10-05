from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str
    email: str
    name: str

class CreateUserDatabase(BaseModel):
    username: str
    hashed_password: str
    email: str
    name: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None
