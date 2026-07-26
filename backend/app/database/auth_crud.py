from sqlalchemy.orm import Session

from app.database.models import User


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(
    db: Session,
    username: str,
    email: str,
    hashed_password: str,
    role: str = "Viewer"
):

    user = User(

        username=username,

        email=email,

        password=hashed_password,

        role=role

    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user