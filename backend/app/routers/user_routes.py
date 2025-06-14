from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_username
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    
)

@router.post("/", response_model=UserResponse)
def register_user(
    user: UserCreate, db: Session = Depends(get_db)
):
    """
    Register a new user.
    """
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="O usuário já existe.")
    
    new_user = create_user(db, user)
    return new_user