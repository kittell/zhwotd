from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import JSON
from zhwotd.db.base import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    pinyin = Column(String, nullable=True)
    traditional = Column(String, nullable=True)
    definitions = Column(JSON, nullable=False, default=list)
    examples = Column(JSON, nullable=False, default=list)
    hsk = Column(Integer, nullable=False, default=0)
    notes = Column(String, nullable=True)

    def __init__(
        self,
        word: str = '',
        pinyin: str = '',
        traditional: str = '',
        definitions: list[str] | None = None,
        examples: list[str] | None = None,
        hsk: int = 0,
        notes: str = ''
    ):
        
        self.word = word
        self.pinyin = pinyin
        self.traditional = traditional
        self.definitions = definitions or []
        self.examples = examples or []
        self.hsk = hsk
        self.notes = notes
        return
