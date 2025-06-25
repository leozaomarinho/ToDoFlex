from sqlalchemy.orm import Session
from app.models.user_model import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    
    #Verifica se a senha fornecida corresponde à senha criptografada.
  
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    """
    Autentica o usuário com base no email e senha fornecidos.
    Retorna o usuário se a autenticação for bem-sucedida, caso contrário, retorna None.
    """
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user