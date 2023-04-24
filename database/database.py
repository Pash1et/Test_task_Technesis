from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from loader import (DB_HOST, DB_PORT, POSTGRES_DB,
                    POSTGRES_PASSWORD, POSTGRES_USER)

DB_URL = (f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
          f'{DB_HOST}:{DB_PORT}/{POSTGRES_DB}')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
