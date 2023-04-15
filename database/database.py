from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///database/db.sqlite'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
