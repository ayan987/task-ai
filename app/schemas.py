# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class PersonRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        # for Pydantic v2 use from_attributes instead of orm_mode
        orm_mode = True  
        # if you’re on pydantic v2, rename the line above to:
        # from_attributes = True

class ProjectRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    product_owner_id: int
    product_owner: PersonRead

    class Config:
        orm_mode = True  
        # or for v2:
        # from_attributes = True
