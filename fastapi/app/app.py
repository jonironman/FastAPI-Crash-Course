from  fastapi  import FastAPI

app = FastAPI()
todos = [
    {
        "id": "1",
        "activity": "do it 1"
    },
    {
        "id": "2",
        "activity": "do it 2"
    }
]

#miniaml app - get request
@app.get("/", tags=['R00T'])
async def root() -> dict:
    return {"ping": "pong"}

# Get
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return { "data": todos}

# Post
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {"data": "a todo has been added !" }


# Put
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todo['acitvity'] = body['activity']
            return {"data": f"Todo with id {id} has been update !" }
    return {
        "data": f"Todo with id {id} not FOUND!"
    }


# Delete
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {"data": f"Todo with id {id} has been delete !" }
    return {
        "data": f"Todo with id {id} not FOUND!"
    }
