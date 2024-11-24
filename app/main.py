from fastapi import FastAPI, Response, status
from pydantic import BaseModel

# Create Key-Value Pair
class keyValue(BaseModel):
    key: str
    value: str

app = FastAPI()

# In-memory store
store = {}

@app.get("/")
async def root():
    return {"message": "Welcome to the Key-Value Store. Make sure to check the docs at /docs to see what you can do."}

@app.get("/value/{key}", status_code=status.HTTP_200_OK)
async def getValue(key: str, response: Response):
    if key in store:
        return {"value": store[key]}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Key not found."}


@app.post("/value/", status_code=status.HTTP_201_CREATED)
async def addKeyValue(keyvalue: keyValue, response: Response):
    if keyvalue.key not in store:
        store[keyvalue.key] = keyvalue.value
        return {"message": "Key-Value pair added"}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {"message": "Key already exists. Stay tuned for the PUT method to update the value."}

@app.delete("/value/{key}", status_code=status.HTTP_200_OK)
async def deleteKeyValue(key: str, response: Response):
    if key in store:
        del store[key]
        return {"message": "Key-Value pair deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Key not found"}