import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
database_url = "postgresql://postgres:1@localhost:5432/qa"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
   __tablename__ = 'student'

   user_id = Column(Integer, primary_key=True)
   level = Column(String)

# Test for adding a student
def test_add_student():
    session = Session()
    student = Student(user_id=1, level="Elementary")
    session.add(student)
    session.commit()

    saved = session.query(Student).filter_by(user_id=1).first()
    assert saved.level == "Elementary"

    session.delete(saved)
    session.commit()
    session.close()

# Test for updating a student
def test_update_student():
    session = Session()
    student = Student(user_id=1, level="Elementary")
    session.add(student)
    session.commit()

    student.level = "Upper-Intermediate"
    session.commit()

    updated = session.query(Student).filter_by(user_id=1).first()
    assert updated.level == "Upper-Intermediate"

    session.delete(updated)
    session.commit()
    session.close()

# Test for deleting a subject
def test_delete_student():
    session = Session()
    student = Student(user_id=1, level="Elementary")
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(Student).filter_by(user_id=1).first()
    assert deleted is None

    session.close()