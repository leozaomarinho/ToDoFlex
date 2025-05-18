from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: Optional[bool] = None

class Task(TaskBase):
    id : int
    completed: bool

    class Config:
        orm_mode = True
        # Permite que o Pydantic converta os dados do ORM para o formato esperado