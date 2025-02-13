from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = {}  # Store users in memory

class User(BaseModel):
    id: str
    name: str
    age: int

@app.post("/users")
def add_user(user: User):
    users[user.id] = user.dict()
    return {"message": "User added successfully"}

@app.get("/users")
def get_users():
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001)
