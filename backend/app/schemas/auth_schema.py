from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# ==========================================
# REGISTER USER
# ==========================================

class RegisterUser(BaseModel):

    username: str

    email: EmailStr

    password: str

    role: str = "Viewer"