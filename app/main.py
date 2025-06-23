from fastapi import FastAPI
from typing import List
from .schemas import PersonRead, ProjectRead

app = FastAPI()

# In-memory storage with dummy data
persons = [
    {"id": 1,  "name": "Alice",   "email": "alice@example.com"},
    {"id": 2,  "name": "Bob",     "email": "bob@example.com"},
    {"id": 3,  "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4,  "name": "David",   "email": "david@example.com"},
    {"id": 5,  "name": "Eve",     "email": "eve@example.com"},
    {"id": 6,  "name": "Frank",   "email": "frank@example.com"},
    {"id": 7,  "name": "Grace",   "email": "grace@example.com"},
    {"id": 8,  "name": "Heidi",   "email": "heidi@example.com"},
    {"id": 9,  "name": "Ivan",    "email": "ivan@example.com"},
    {"id": 10, "name": "Judy",    "email": "judy@example.com"},
]

projects = [
    {
        "id": 1,
        "title": "Project Alpha",
        "description": "Alpha project description",
        "product_owner_id": 1,
        "product_owner": persons[0],
    },
    {
        "id": 2,
        "title": "Project Beta",
        "description": "Beta project description",
        "product_owner_id": 2,
        "product_owner": persons[1],
    },
    {
        "id": 3,
        "title": "Project Gamma",
        "description": "Gamma project description",
        "product_owner_id": 3,
        "product_owner": persons[2],
    },
]

@app.get("/persons", response_model=List[PersonRead])
def get_persons() -> List[PersonRead]:
    return persons

@app.get("/projects", response_model=List[ProjectRead])
def get_projects() -> List[ProjectRead]:
    return projects
