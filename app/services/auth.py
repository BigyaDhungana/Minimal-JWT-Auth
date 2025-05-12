from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from app.configs.config import settings


def create_token(username: str):
    """
    Creates a JWT token on the basis of username
    """
    expiry_time = datetime.now(timezone.utc) + timedelta(
        minutes=settings.TOKEN_EXPIRE_IN_MINUTES
    )
    data_to_encode = {"username": username}
    data_to_encode.update({"exp": int(expiry_time.timestamp())})
    return jwt.encode(
        claims=data_to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )


def verify_token(token: str):
    """
    Validates the JWT token
    """
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY)
        return (
            payload  # jose checks for the expired tokens so no need to check manually
        )
    except JWTError:
        return None
