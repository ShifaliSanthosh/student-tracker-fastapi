from fastapi import FastAPI
from app.routers import students, scores
from app.database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Performance Tracker API")

app.include_router(students.router)
app.include_router(scores.router)