from zhwotd.db.engine import engine
from zhwotd.models import metadata

def init_db():
    metadata.create_all(engine)
