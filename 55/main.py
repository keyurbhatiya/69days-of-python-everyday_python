# Build a Full-Stack Task Manager API in Python! 🚀 (Day 55)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List, Optional


app = FastAPI(title="taskMaster pro api")

def db_query(sql,params=(),is_select=False):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql,params)

        if is_select:
            return cursor.fetchall()
        conn.commit()


db_query("""
    create table if not exists tasks(
         id integer primary key autoincrement,
         title text not null,
         completed integer default 0)
""")

class Task(BaseModel):
    title : str
    completed : bool = False


@app.get("/tasks")
def get_tasks():
    rows = db_query("select * from tasks",is_select=True)
    return[{"id":r[0],"title":r[1],"completed":bool(r[2])} for r in rows]

@app.post("/tasks")
def add_task(task: Task):
    db_query("insert into tasks (title,completed) values (?,?)",(task.title,int(task.completed)))
    return {"message":"Task added successfully"}

@app.put("/tasks/{task_id}")
def update_task(task_id:int):
    db_query("update tasks set completed = 1 where id = ?",(task_id,))
    return {"message" : f"Task {task_id} marked as completed "}

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    db_query("delete from tasks where id = ?", (task_id,))
    return {"message" : f"Task deleted successfully"}

