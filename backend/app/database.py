# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./todoflex.db"  
# SQLite database file

# Conexao com o banco de dados
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criando sessoes no banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para os modelos
Base = declarative_base()