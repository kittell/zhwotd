import json
import os
from zhwotd.gui import GUI
from zhwotd.db.manager import DatabaseManager
from zhwotd.models.word import word_table
from zhwotd.models.wotd import wotd_table
from zhwotd.domain.word import Word
from zhwotd.domain.wotd import WOTD


class Application:
    def __init__(self):
        self.config = self._load_config()
        self.dbm = DatabaseManager(self.config['database'])
        return
    
    def _load_config(self):
        config = dict()
        f_dir = os.path.dirname(__file__)
        f_name = 'config.json'
        f_fullpath = os.path.join(f_dir, f_name)
        with open(f_fullpath, 'r') as f: 
            config = json.load(f)
        return config

    
    def run(self):
        self.gui = GUI(self, self.config['gui'])
        return
    
    def find_word(self, simplified: str):
        """Return dict or None."""
        return self.dbm.get_word(simplified)

    def add_word(self, word_data: dict):
        """Insert a new word and return the inserted row as dict."""
        return self.dbm.insert_word(word_data)
    
    