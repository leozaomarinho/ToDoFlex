#  services/task_service.py
from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate

#create_task: Cria uma nova tarefa no banco de dados
#get_task: Retorna todas as tarefas
#get_task_by_id: Retorna uma tarefa por ID
#update_task: Atualiza uma tarefa existente
#delete_task: Deleta uma tarefa por ID

def create_task(db: Session, task: TaskCreate):
    # Cria uma nova tarefa no banco de dados
    nova_tarefa = Task(title=task.title, description=task.description)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

def get_task(db: Session):
    # Retorna todas as tarefas do banco de dados
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    # Retorna uma tarefa específica pelo ID
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    # Atualiza uma tarefa existente
    tarefa = db.query(Task).filter(Task.id == task_id).first()
    if tarefa:
        tarefa.title = task_update.title
        tarefa.description = task_update.description
        tarefa.completed = task_update.completed
        db.commit()
        db.refresh(tarefa)
    return tarefa

def delete_task(db: Session, task_id: int):
    # Deleta uma tarefa pelo ID
    tarefa = db.query(Task).filter(Task.id == task_id).first()
    if tarefa:
        db.delete(tarefa)
        db.commit()
    return tarefa