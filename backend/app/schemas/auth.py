from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    name: str = Field(min_length=2, max_length=100)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=72)  # Min length 1 to be flexible


class AuthResponse(BaseModel):
    user_id: int
    email: str
    token: str
    
    class Config:
        from_attributes = True