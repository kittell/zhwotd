from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Path to your SQLite database file
db_url = "sqlite:///./zhwotd.db"

# Create a SQLAlchemy Core engine
engine = create_engine(
    db_url,
    connect_args={"check_same_thread": False}  # required for SQLite + threads
)

# Create a Core-compatible session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
