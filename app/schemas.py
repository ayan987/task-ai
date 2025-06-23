from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime

class PersonCreate(BaseModel):
    name: str
    email: EmailStr

class PersonRead(PersonCreate):
    id: int
    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    owner_id: int

class ProjectRead(ProjectCreate):
    id: int
    owner: PersonRead
    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    due: Optional[datetime.datetime] = None
    owner_id: int
    project_id: int

class TaskRead(TaskCreate):
    id: int
    owner: PersonRead
    project: ProjectRead
    class Config:
        orm_mode = True
