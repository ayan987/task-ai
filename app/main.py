from fastapi import FastAPI, HTTPException
from .schemas import PersonCreate, PersonRead, ProjectCreate, ProjectRead, TaskCreate, TaskRead
from typing import List
import datetime

app = FastAPI()

persons = [
    {"id": 1, "name": "Alice",   "email": "alice@example.com"},
    {"id": 2, "name": "Bob",     "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

projects = [
    {
        "id": 1,
        "title": "Project Alpha",
        "description": "Alpha project description",
        "owner_id": 1,
        "owner": persons[0],
    },
    {
        "id": 2,
        "title": "Project Beta",
        "description": "Beta project description",
        "owner_id": 2,
        "owner": persons[1],
    },
    {
        "id": 3,
        "title": "Project Gamma",
        "description": "Gamma project description",
        "owner_id": 3,
        "owner": persons[2],
    },
]

tasks = [
    {
        "id": 1,
        "title": "Initial Meeting",
        "due": datetime.utcnow(),
        "owner_id": 1,
        "project_id": 1,
        "owner": persons[0],
        "project": projects[0],
    },
    {
        "id": 2,
        "title": "Beta Kickoff",
        "due": datetime.utcnow(),
        "owner_id": 2,
        "project_id": 2,
        "owner": persons[1],
        "project": projects[1],
    },
    {
        "id": 3,
        "title": "Gamma Review",
        "due": datetime.utcnow(),
        "owner_id": 3,
        "project_id": 3,
        "owner": persons[2],
        "project": projects[2],
    },
]

# Update counters
person_id_counter = 4
project_id_counter = 4
task_id_counter = 4

@app.post("/persons/", response_model=PersonRead)
def create_person(person: PersonCreate):
    global person_id_counter
    new_person = person.dict()
    new_person["id"] = person_id_counter
    persons.append(new_person)
    person_id_counter += 1
    return new_person

@app.get("/persons/{person_id}", response_model=PersonRead)
def read_person(person_id: int):
    for p in persons:
        if p["id"] == person_id:
            return p
    raise HTTPException(status_code=404, detail="Person not found")

@app.post("/projects/", response_model=ProjectRead)
def create_project(project: ProjectCreate):
    global project_id_counter
    # Validate owner exists
    owner = next((p for p in persons if p["id"] == project.owner_id), None)
    if not owner:
        raise HTTPException(status_code=400, detail="Owner not found")
    new_project = project.dict()
    new_project["id"] = project_id_counter
    new_project["owner"] = owner
    projects.append(new_project)
    project_id_counter += 1
    return new_project

@app.get("/projects/{project_id}", response_model=ProjectRead)
def read_project(project_id: int):
    for proj in projects:
        if proj["id"] == project_id:
            return proj
    raise HTTPException(status_code=404, detail="Project not found")

@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate):
    global task_id_counter
    # Validate owner and project exist
    owner = next((p for p in persons if p["id"] == task.owner_id), None)
    project = next((pr for pr in projects if pr["id"] == task.project_id), None)
    if not owner:
        raise HTTPException(status_code=400, detail="Task owner not found")
    if not project:
        raise HTTPException(status_code=400, detail="Related project not found")
    due_time = task.due or datetime.datetime.utcnow()
    new_task = task.dict()
    new_task["id"] = task_id_counter
    new_task["due"] = due_time
    new_task["owner"] = owner
    new_task["project"] = project
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=TaskRead)
def read_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")
