from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):

    name: str

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=72
    )

    role: str = "Viewer"