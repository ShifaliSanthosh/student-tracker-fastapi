from sqlalchemy.orm import Session
from app import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_all_students(db: Session):
    return db.query(models.Student).all()

def delete_student(db: Session, student_id: str):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False

def add_score(db: Session, student_id: str, score: schemas.ScoreCreate):
    db_score = models.Score(student_id=student_id, subject=score.subject, marks=score.marks)
    db.add(db_score)
    db.commit()
    return db_score
