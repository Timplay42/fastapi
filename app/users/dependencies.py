from fastapi import Depends, HTTPException, Request
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime
from app.exception import IncorrentTokenFormatExxception, TokenAbsentException, TokenExpiredException

from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_acces_token")
    if not token:
        raise TokenAbsentException
    return token



async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrentTokenFormatExxception
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=401)

    return user