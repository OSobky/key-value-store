from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/value")
async def value():
    return {"value": "Looking for the key to get the value"}

@app.post("/value")
async def value():
    return {"value": "Did not post yet looking for the key"}

@app.delete("/value")
async def value():
    return {"value": "Did not delete yet looking for the key"}