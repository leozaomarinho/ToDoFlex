# app/routers/task_routes.py
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from app.schemas import Task, TaskCreate, TaskUpdate
from app.services import (

    create_task,
    get_task,

    update_task,
    delete_task,
    get_task_by_id,

)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@router.get("/", response_model=List[Task])
def read_tasks(task_id: int = None, db: Session = Depends(get_db)):
    tarefa = get_task(db, task_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Task not found")
    return tarefa

@router.post("/", response_model=Task)
def create_new_task(task_id: int, dados:TaskUpdate, db: Session = Depends(get_db)):
   tarefa = update_task(db, task_id, dados)
   if not tarefa:
       raise HTTPException(status_code=404, detail="Task not found")
   return tarefa