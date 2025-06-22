from pydantic import BaseModel,EmailStr

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
