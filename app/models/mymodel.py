from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from .meta import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    mds_number = Column(String(10), unique=True)
    mds_name = Column(String(100))
    assigned_name = Column(String(100))
    book_count = Column(Integer)
    last_updated = Column(DateTime())

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    author = Column(String(50))
    publish_date = Column(DateTime)
    category = Column(Integer)
