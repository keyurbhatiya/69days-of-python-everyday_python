# FastAPI Tutorial: Build Your First Web API in 5 Minutes! 🚀 (Day 46)

# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "Message" : "Welcome to Day 46, Sir!",
        "Framework" : "FastAPI",
        "Status": "Running"
    }

@app.get("/greet/{name}")
def greet_user(name:str):
    return {
        "Greeting" : f"Hello {name}!",
        "Note" : "This API was Built in 5 Minutes."
    }

# to run uvicorn main:app --reload