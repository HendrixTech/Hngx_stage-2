from fastapi import FastAPI
import person
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(person.router)


@app.get("/")
async def main():
    return {"message": "Welcome here!!!"}
