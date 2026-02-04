from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Pydantic Model for Request Body
# This defines exactly what data we expect from the user
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "low"
    is_completed: bool = False

# 2. Path Parameter: Getting a specific item by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"message": f"Fetching data for Task ID: {task_id}"}

# 3. Query Parameter: Filtering data (e.g., /search?q=python)
@app.get("/search")
def search_tasks(q: str, limit: int = 10):
    return {"query": q, "limit_results": limit}

# 4. Request Body: Creating a new task (POST method)
@app.post("/create-task")
def create_task(task: Task):
    return {
        "status": "Success",
        "data_received": task,
        "note": f"Task '{task.title}' has been added to the database."
    }

# Run using: uvicorn main:app --reload