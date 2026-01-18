import json
import os
from zhwotd.gui import GUI
from zhwotd.db.manager import DatabaseManager
from zhwotd.models.word import DB_Word
from zhwotd.models.wotd import DB_WOTD
from zhwotd.db.queries import query_word_by_text
from zhwotd.domain.word import Word
from zhwotd.domain.wotd import WOTD


class Application:
    def __init__(self):
        self.config = self._load_config()
        self.dbm = DatabaseManager(self.config['database'])
        return
    
    def run(self):
        self.gui = GUI(self, self.config['gui'])
        return
    
    def _load_config(self):
        config = dict()
        f_dir = os.path.dirname(__file__)
        f_name = 'config.json'
        f_fullpath = os.path.join(f_dir, f_name)
        with open(f_fullpath, 'r') as f: 
            config = json.load(f)
        return config

    
    def find_word(self, word: str) -> str:
        """
        Find a word in the database
        """
        # TODO: add another scheme for searching on any attribute, not just the word text
        result = ''
        query_builder = QueryBuilder()
        query = query_builder.find_word(word)
        print('query:', query)
        query_result = self.dbm.execute(query_word_by_text(word))
        # TODO: return a Word object
        print('query_result:', query_result)
        return result

    def add_word(self, word: Word):
        """
        Add a word to the Word database
        """

        return
    

class QueryBuilder:
    """Build queries specific to program function, then handoff to DatabaseManager
    """
    def __init__(self):
        return
    
    def find_word(self, word: str) -> str:
        # TODO: restart here next time
        query = f'''
            SELECT *
            FROM words
            WHERE word = :word
        '''
        return query

