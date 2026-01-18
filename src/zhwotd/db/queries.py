# db/queries.py (optional helper module)
from zhwotd.models.word import DB_Word
from zhwotd.models.wotd import DB_WOTD

def query_word_by_text(text):
    def _query(db):
        return db.query(DB_Word).filter(DB_Word.word == text).first()
    return _query
