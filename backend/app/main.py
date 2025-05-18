from fastapi import FastAPI
from app.routers import task_routes

app = FastAPI()
# Include routers

app.include_router(task_routes.routerclea)


@app.get("/")
def read_root():
    return{ "message": "Api do ToDoFlex rodando!"}
