# from pydantic import BaseModel
# from enum import Enum

# class TaskStatus(str, Enum):
#     pending = "Pending"
#     in_progress = "In Progress"
#     completed = "Completed"

# class TaskPriority(str, Enum):
#     high = "High"
#     medium = "Medium"
#     low = "Low"

# class TaskCreate(BaseModel):
#     title: str
#     description: str | None = None
#     status: TaskStatus = TaskStatus.pending
#     priority: TaskPriority = TaskPriority.medium

# class TaskResponse(TaskCreate):
#     id: int
#     is_deleted: bool

#     class Config:
#         from_attributes = True




from pydantic import BaseModel
from enum import Enum

# ===========================
# Task Schemas
# ===========================

class TaskStatus(str, Enum):
    pending = "Pending"
    in_progress = "In Progress"
    completed = "Completed"


class TaskPriority(str, Enum):
    high = "High"
    medium = "Medium"
    low = "Low"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium


class TaskResponse(TaskCreate):
    id: int
    is_deleted: bool

    class Config:
        from_attributes = True


# ===========================
# User Schemas
# ===========================

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# ===========================
# JWT Token Schema
# ===========================

class Token(BaseModel):
    access_token: str
    token_type: str