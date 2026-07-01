from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy import MetaData 

metadata = MetaData()

class WOTD:
    def __init__(self, d, word):
        self.d = d
        self.word = word
      
metadata = MetaData()

wotd_table = Table(
    "wotd",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("word", String, nullable=False),
    Column("date", Date)
)