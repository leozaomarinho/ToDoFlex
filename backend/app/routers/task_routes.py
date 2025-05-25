from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.task_schema import Task, TaskCreate, TaskUpdate
from app.services.task_service import (
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
def read_tasks(db: Session = Depends(get_db)):
    return get_task(db)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    tarefa = get_task_by_id(db, task_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Task not found")
    return tarefa

@router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.put("/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    tarefa = update_task(db, task_id, task)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Task not found")
    return tarefa

@router.delete("/{task_id}", response_model=Task)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    tarefa = delete_task(db, task_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Task not found")
    return tarefa