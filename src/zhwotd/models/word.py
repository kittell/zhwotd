from sqlalchemy import Table, Column, Integer, String, MetaData
from zhwotd.models import metadata

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
