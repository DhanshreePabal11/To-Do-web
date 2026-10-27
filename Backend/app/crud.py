# from sqlalchemy.orm import Session
# from app.models import Task
# from app.schemas import TaskCreate


# def create_task(db: Session, task: TaskCreate):
#     db_task = Task(
#         title=task.title,
#         description=task.description,
#         status=task.status,
#         priority=task.priority
#     )

#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)

#     return db_task


# def get_tasks(db: Session):
#     return db.query(Task).filter(
#         Task.is_deleted == False
#     ).all()


# def update_task(db: Session, task_id: int, task: TaskCreate):
#     db_task = db.query(Task).filter(
#         Task.id == task_id
#     ).first()

 
#     if db_task is None:
#         return {"message": "Task not found"}

#     db_task.title = task.title
#     db_task.description = task.description
#     db_task.status = task.status
#     db_task.priority = task.priority

#     db.commit()
#     db.refresh(db_task)

#     return db_task


# def delete_task(db: Session, task_id: int):
#     db_task = db.query(Task).filter(
#         Task.id == task_id
#     ).first()

#     if db_task is None:
#         return {"message": "Task not found"}

#     db_task.is_deleted = True

#     db.commit()

#     return {"message": "Task moved to bin"}


# def get_deleted_tasks(db: Session):
#     return db.query(Task).filter(
#         Task.is_deleted == True
#     ).all()


# def restore_task(db: Session, task_id: int):
#     db_task = db.query(Task).filter(
#         Task.id == task_id
#     ).first()

#     if db_task is None:
#         return {"message": "Task not found"}

#     db_task.is_deleted = False

#     db.commit()

#     return {"message": "Task restored"}


# def permanent_delete_task(db: Session, task_id: int):
#     db_task = db.query(Task).filter(
#         Task.id == task_id
#     ).first()

#     if db_task is None:
#         return {"message": "Task not found"}

#     db.delete(db_task)
#     db.commit()

#     return {"message": "Task permanently deleted"}


# def complete_task(db: Session, task_id: int):
#     db_task = db.query(Task).filter(
#         Task.id == task_id
#     ).first()

#     if db_task is None:
#         return {"message": "Task not found"}

#     db_task.status = "Completed"

#     db.commit()
#     db.refresh(db_task)

#     return db_task

from sqlalchemy.orm import Session

from app.models import Task, User
from app.schemas import TaskCreate, UserCreate
from app.utils.auth import hash_password

# -----------------------------
# Task CRUD Operations
# -----------------------------

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        user_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(
        Task.user_id == user_id,
        Task.is_deleted == False
    ).all()


def update_task(db: Session, task_id: int, task: TaskCreate, user_id: int):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if db_task is None:
        return {"message": "Task not found"}

    db_task.title = task.title
    db_task.description = task.description
    db_task.status = task.status
    db_task.priority = task.priority

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if db_task is None:
        return {"message": "Task not found"}

    db_task.is_deleted = True
    db.commit()

    return {"message": "Task moved to bin"}


def get_deleted_tasks(db: Session, user_id: int):
    return db.query(Task).filter(
        Task.user_id == user_id,
        Task.is_deleted == True
    ).all()


def restore_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if db_task is None:
        return {"message": "Task not found"}

    db_task.is_deleted = False
    db.commit()

    return {"message": "Task restored"}


def permanent_delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if db_task is None:
        return {"message": "Task not found"}

    db.delete(db_task)
    db.commit()

    return {"message": "Task permanently deleted"}


def complete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if db_task is None:
        return {"message": "Task not found"}

    db_task.status = "Completed"

    db.commit()
    db.refresh(db_task)

    return db_task


# -----------------------------
# User CRUD Operations
# -----------------------------

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(
        User.email == email
    ).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user