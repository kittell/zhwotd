# src/zhwotd/db/init_db.py
from zhwotd.db.engine import engine
from zhwotd.db.base import Base

# Import models
from zhwotd.models import word
from zhwotd.models import wotd

def init_db():
    Base.metadata.create_all(bind=engine)
