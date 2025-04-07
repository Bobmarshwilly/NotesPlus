import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URL = os.path.join(os.path.dirname(BASE_DIR), "notes.db")

engine = create_engine(f"sqlite:///{DATABASE_URL}")

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
