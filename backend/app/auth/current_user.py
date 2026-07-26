from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import JWTError, jwt

from types import SimpleNamespace

from app.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)

):

    token = credentials.credentials

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        return SimpleNamespace(

            email=payload.get("sub"),

            username=payload.get("username"),

            role=payload.get("role")

        )

    except JWTError:

        raise HTTPException(

            status_code=401,

            detail="Invalid or expired token"

        )