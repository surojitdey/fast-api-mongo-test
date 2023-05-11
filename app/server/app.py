from fastapi import FastAPI
from .routes.cources import router as CourseRouter

app = FastAPI()

app.include_router(CourseRouter, tags=["Course"], prefix="/course")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to KIMO Courses!"}