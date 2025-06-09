# File: main.py
# Project: ToDoFlex
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import task_routes
from fastapi.middleware.cors import CORSMiddleware

# Criando tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "ToDoFlex API",
    description = "API para gerenciar tarefas do ToDoFlex",
    version = "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Include routers
app.include_router(task_routes.router)


@app.get("/")
def read_root():
    return{ "message": "Api do ToDoFlex rodando!"}
