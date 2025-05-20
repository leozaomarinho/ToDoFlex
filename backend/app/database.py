from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./todoflex.db"  

# Conexão com o banco de dados
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criando sessões no banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para os modelos
Base = declarative_base()

# Adicione esta função ESSENCIAL:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db