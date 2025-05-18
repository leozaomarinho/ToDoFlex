from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    #TaskBase: contém os campos básicos (title e description).
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    #TaskCreate: igual ao TaskBase, mas pode ser estendido depois.
    pass

class TaskUpdate(TaskBase):
    #TaskUpdate: inclui completed para permitir atualizações parciais.
    completed: Optional[bool] = None

class Task(TaskBase):
    #Task: usado nas respostas, inclui id e completed.
    id : int
    completed: bool

    class Config:
        # orm_mode = True: permite que o Pydantic converta objetos do ORM (SQLAlchemy) em dicionários JSON.
        orm_mode = True
        # Permite que o Pydantic converta os dados do ORM para o formato esperado