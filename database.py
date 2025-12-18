from sqlalchemy import create_engine
from config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#1. engine생성
engine = create_engine(settings.database_url)

#2. SessinoLocal
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)

#3. Base
Base = declarative_base()

#4. get_db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
