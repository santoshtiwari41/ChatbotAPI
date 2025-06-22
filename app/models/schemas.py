from pydantic import BaseModel,EmailStr
from datetime import datetime

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    result: str


class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ChatCreate(BaseModel):
    query: str
    response: str
    user_id: int

class ChatRead(BaseModel):
    id: int
    user_id: int
    query: str
    response: str
    created_at: datetime
