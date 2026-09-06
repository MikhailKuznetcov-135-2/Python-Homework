import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from pytest import fixture
from models import Base

TEST_DATABASE_URL = (
    "postgresql://houston42@gmail.com:aragorn@localhost:5432/mydatabase"
)
engine = create_engine(TEST_DATABASE_URL, future=True)
session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Session = scoped_session(session_factory)
@fixture(scope="function")

def db_session():
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    Session.remove()
    transaction.rollback()
    connection.close()
@fixture(scope="session", autouse=True)
def setup_db():
    """
