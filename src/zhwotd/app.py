import json
import os
from zhwotd.gui import GUI
from zhwotd.db.manager import DatabaseManager


class Application:
    def __init__(self):
        self.config = self._load_config()
        self.dbm = DatabaseManager(self.config['database'])
        gui = GUI(self, self.config['gui'])
        return
    
    def _load_config(self):
        config = dict()
        f_dir = os.path.dirname(__file__)
        f_name = 'config.json'
        f_fullpath = os.path.join(f_dir, f_name)
        with open(f_fullpath, 'r') as f: 
            config = json.load(f)
        return config

    
    def find_word(self, word) -> str:
        result = ''
        query_builder = QueryBuilder()
        query = query_builder.find_word(word)
        print('query:', query)
        query_result = self.dbm.execute_query(query)
        print('query_result:', query_result)
        return result
    

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

