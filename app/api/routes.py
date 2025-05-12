from fastapi import APIRouter, Request, status, Header
from fastapi.responses import JSONResponse
from app.services.auth import create_token, verify_token

router = APIRouter()


@router.post("/token/{username}")
def login_mock(username: str):
    """
    ## Authenticate a user and return a JWT token

    ### Parameters:
    - `username`: Unique identifier for the user

    ### Returns:
    - JSON object containing the access token
    """
    token = create_token(username=username)
    return JSONResponse(content={"token": token}, status_code=status.HTTP_200_OK)


@router.get("/check/")
def check_mock(request: Request, Token=Header()):
    """
    ## Verify if a token is valid

    ### Security:
    - Requires token in `Token` header

    ### Returns:
    - Success message if token is valid
    - Error message if token is invalid
    """
    user_token = Token
    if not user_token or verify_token(user_token.strip()) is None:
        return JSONResponse(
            content={"message": "invalid token"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return JSONResponse(
        {"message": "authorized content"}, status_code=status.HTTP_200_OK
    )
