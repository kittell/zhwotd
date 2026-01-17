# db/queries.py (optional helper module)
from zhwotd.models.word import Word
from zhwotd.models.wotd import WOTD

def query_word_by_text(text):
    def _query(db):
        return db.query(Word).filter(Word.word == text).first()
    return _query
