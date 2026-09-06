from models import Student

def test_create_student(db_session):
    student = Student(full_name="Иванов Иван", email="ivan.ivanov@example.com")
    db_session.add(student)
    db_session.commit()
    assert student.id is not None
    assert student.full_name == "Иванов Иван"
    db_session.delete(student)
    db_session.commit()
    
def test_update_student(db_session):
    student = Student(full_name="Петров Пётр")
    db_session.add(student)
    db_session.commit()
    student.email = "petr.petrov@example.com"
    db_session.commit()
    updated = db_session.query(Student).filter_by(id=student.id).first()
    assert updated is not None
    assert updated.email == "petr.petrov@example.com"
    db_session.delete(updated)
    db_session.commit()
    
def test_delete_student(db_session):
    student = Student(full_name="Сидоров Сидор")
    db_session.add(student)
    db_session.commit()
    db_session.delete(student)
    db_session.commit()
    deleted = db_session.query(Student).filter_by(id=student.id).first()
    assert deleted is None
