# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.dependencies import get_db
# from app.schemas import TaskCreate
# from app import crud

# router = APIRouter(
#     prefix="/tasks",
#     tags=["Tasks"]
# )


# @router.get("/")
# def get_all_tasks(db: Session = Depends(get_db)):
#     return crud.get_tasks(db)


# @router.post("/")
# def create_task(
#     task: TaskCreate,
#     db: Session = Depends(get_db)
# ):
#     return crud.create_task(db, task)


# @router.put("/{task_id}")
# def update_task(
#     task_id: int,
#     task: TaskCreate,
#     db: Session = Depends(get_db)
# ):
#     return crud.update_task(db, task_id, task)


# @router.delete("/{task_id}")
# def delete_task(
#     task_id: int,
#     db: Session = Depends(get_db)
# ):
#     return crud.delete_task(db, task_id)


# # GET BIN TASKS
# @router.get("/bin")
# def get_bin_tasks(
#     db: Session = Depends(get_db)
# ):
#     return crud.get_deleted_tasks(db)


# # RESTORE TASK
# @router.put("/restore/{task_id}")
# def restore_task(
#     task_id: int,
#     db: Session = Depends(get_db)
# ):
#     return crud.restore_task(db, task_id)


# @router.get("/bin")
# def get_deleted_tasks(
#     db: Session = Depends(get_db)
# ):
#     return crud.get_deleted_tasks(db)


# @router.put("/restore/{task_id}")
# def restore_task(
#     task_id: int,
#     db: Session = Depends(get_db)
# ):
#     return crud.restore_task(db, task_id)


# @router.delete("/permanent/{task_id}")
# def permanent_delete_task(
#     task_id: int,
#     db: Session = Depends(get_db)
# ):
#     return crud.permanent_delete_task(db, task_id)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas import TaskCreate
from app.models import User
from app import crud


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# GET ALL TASKS

@router.get("/")
def get_all_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_tasks(
        db,
        current_user.id
    )


# CREATE TASK

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_task(
        db,
        task,
        current_user.id
    )


# UPDATE TASK

@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.update_task(
        db,
        task_id,
        task,
        current_user.id
    )


# MOVE TASK TO BIN

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.delete_task(
        db,
        task_id,
        current_user.id
    )


# GET BIN TASKS

@router.get("/bin")
def get_bin_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_deleted_tasks(
        db,
        current_user.id
    )


# RESTORE TASK

@router.put("/restore/{task_id}")
def restore_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.restore_task(
        db,
        task_id,
        current_user.id
    )


# PERMANENT DELETE

@router.delete("/permanent/{task_id}")
def permanent_delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.permanent_delete_task(
        db,
        task_id,
        current_user.id
    )