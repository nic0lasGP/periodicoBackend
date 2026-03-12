from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials,OAuth2PasswordBearer
SECRET_KEY = "tokenpayo"  # cámbiala por una segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
bearer_scheme = HTTPBearer() 

def createAccessToken(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    

    return token


def getCurrentUser(token: str = Depends(bearer_scheme)):
    
    token_use = token.credentials   
    try:
        payload = jwt.decode(token_use, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail="e")

def requireAdmin(current_user: dict = Depends(getCurrentUser)):
    if not current_user.get("admin"):
        raise HTTPException(status_code=403, detail="Se requieren permisos de administrador")
    return current_user