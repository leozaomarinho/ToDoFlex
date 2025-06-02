from fastapi import FastAPI
from app.routers import task_routes
from app.database import engine, Base
# Importando o banco de dados e o modelo Base

#Criacao das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ToDoFlex API",
    description="API para gerenciar tarefas do ToDoFlex",
    version="1.0.0"

)
# Include routers
app.include_router(task_routes.router)


@app.get("/")
def read_root():
    return{ "message": "Api do ToDoFlex rodando!"}
