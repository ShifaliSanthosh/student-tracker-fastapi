from pydantic import BaseModel
from typing import Optional, List

class ScoreCreate(BaseModel):
    subject: str
    marks: float

class StudentBase(BaseModel):
    id: str
    name: str
    dept: str
    thesis_title: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    class Config:
        orm_mode = True

class Score(BaseModel):
    subject: str
    marks: float

    class Config:
        orm_mode = True
