from sqlalchemy import Column, Integer, String

from .database import Base


class Zuzublik(Base):
    __tablename__ = 'zuzublik'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    xpath = Column(String)
