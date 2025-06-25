from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.schemas.auth_schema import LoginData, Token
from app.services.auth_service import authenticate_user
from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login", response_model=Token)
def login(
    login_data: LoginData,
    db: Session = Depends(get_db)
):
  #Endpoint para autenticar o usuário e gerar um token JWT.
    user = authenticate_user(db,login_data.username,login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=30)
    access_token = user.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", expires_in=access_token_expires.total_seconds())
