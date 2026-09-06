from models import Subject

def test_create_subject(db_session):
    subject = Subject(name="Математика")
    db_session.add(subject)
    db_session.commit() 
    assert subject.id is not None
    assert subject.name == "Математика"
    db_session.delete(subject)
    db_session.commit()
    
def test_update_subject(db_session):
    subject = Subject(name="Физика")
    db_session.add(subject)
    db_session.commit()
    subject.name = "Физика (обновлённая)"
    db_session.commit()
    updated = db_session.query(Subject).filter_by(id=subject.id).first()
    assert updated is not None
    assert updated.name == "Физика (обновлённая)"
    db_session.delete(updated)
    db_session.commit()
    
def test_delete_subject(db_session):
    subject = Subject(name="Химия")
    db_session.add(subject)
    db_session.commit()
    db_session.delete(subject)
    db_session.commit()
    deleted = db_session.query(Subject).filter_by(id=subject.id).first()
    assert deleted is None
