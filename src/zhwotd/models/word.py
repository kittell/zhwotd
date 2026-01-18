from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy.types import JSON
from zhwotd.db.base import Base

class DB_Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    word: Mapped[str] = mapped_column(String, nullable=False)
    pinyin: Mapped[str] = mapped_column(String)
    traditional: Mapped[str] = mapped_column(String)
    definitions: Mapped[list[str]] = mapped_column(JSON, default=list)
    examples: Mapped[list[str]] = mapped_column(JSON, default=list)
    hsk: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str] = mapped_column(String)


