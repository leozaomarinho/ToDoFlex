# app/routers/task_routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "Estudar FastAPI"}]
