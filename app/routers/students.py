from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Student)
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

@router.get("/{student_id}", response_model=schemas.Student)
def get_student(student_id: str, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{student_id}")
def remove_student(student_id: str, db: Session = Depends(get_db)):
    if crud.delete_student(db, student_id):
        return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
