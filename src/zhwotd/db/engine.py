from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///./zhwotd.db"

engine = create_engine(
    db_url,
    connect_args={"check_same_thread": False}  # only for SQLite
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
