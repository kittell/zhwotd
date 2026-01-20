from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from zhwotd.models import metadata

metadata = MetaData()

wotd_table = Table(
    "wotd",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("word", String, nullable=False),
    Column("date", Date)
)