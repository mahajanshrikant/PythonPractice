from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint")
async def first_Api():
    return {"hello": "world"}

