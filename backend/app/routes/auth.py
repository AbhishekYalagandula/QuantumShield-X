from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.auth_crud import get_user_by_email, create_user

from app.schemas.user_schema import UserRegister
from app.schemas.auth_schema import LoginRequest, TokenResponse

from app.services.auth_service import (
    hash_password,
    verify_password
)

from app.core.security import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ===========================
# REGISTER USER
# ===========================
@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    hashed_password = hash_password(user.password)

    new_user = create_user(
        db=db,
        username=user.name,
        email=user.email,
        hashed_password=hashed_password
    )

    return {
        "message": "User registered successfully!",
        "username": new_user.username,
        "email": new_user.email
    }


# ===========================
# LOGIN USER
# ===========================
@router.post("/login", response_model=TokenResponse)
def login_user(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email,
            "username": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }