from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import MetaData 

metadata = MetaData()

class Word:
    def __init__(self, word, pinyin="", traditional="", definitions=None, examples=None, hsk=0, notes=""):
        self.word = word
        self.pinyin = pinyin
        self.traditional = traditional
        self.definitions = definitions or []
        self.examples = examples or []
        self.hsk = hsk
        self.notes = notes

    def to_simplified(self):
        # example domain logic
        return self.word

    def is_hsk_level(self, level):
        return self.hsk == level


metadata = MetaData()

word_table = Table(
    "dictionary",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("simplified", String, nullable=False),
    Column("pinyin", String),
    Column("traditional", String),
    Column("hsk", Integer),
    Column("definition", String),
    Column("example", String),
    Column("notes", String),
)
