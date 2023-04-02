import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_SERVER']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"

Base = declarative_base()

class Database:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_db(self):
        session = self._SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

db = Database(DATABASE_URL)
