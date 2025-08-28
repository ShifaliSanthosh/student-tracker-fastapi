from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    dept = Column(String)
    thesis_title = Column(String, nullable=True)
    scores = relationship("Score", back_populates="student")

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"))
    subject = Column(String)
    marks = Column(Float)

    student = relationship("Student", back_populates="scores")
