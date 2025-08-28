from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database, models

router = APIRouter(tags=["Scores"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/{student_id}/scores/")
def add_score(student_id: str, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.add_score(db, student_id, score)
