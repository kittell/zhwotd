import json
import os
from pathlib import Path
import sqlite3
from sqlalchemy import create_engine, text
from zhwotd.gui import GUI



class Application:
    def __init__(self):
        self.config = self._load_config()
        self.dbm = DatabaseManager(self.config)
        return
    
    def _load_config(self):
        config = dict()
        f_dir = os.path.dirname(__file__)
        f_name = 'config.json'
        f_fullpath = os.path.join(f_dir, f_name)
        with open(f_fullpath, 'r') as f: 
            config = json.load(f)
        return config

    def start(self):
        self.dbm.connect()
        gui = GUI(self, self.config)
        return
    

class DatabaseManager:
    """Handle operations involving the entire database and its structure
    """
    def __init__(self, config):
        self.config = config
        return
    
    def connect(self):
        db_type = self.config['database']['type']
        db_name = self.config['database']['name']
        script_dir = Path(__file__).resolve().parent
        db_path = script_dir / db_name
        self.db_url = db_type + ':///' + str(db_path)

        self.engine = create_engine(self.db_url)
        if self.db_url.is_file() == False:
            self.create_new_db(self.db_url)

        return

    def create_new_db(self):
        
        schema = self._load_schema(self.config['schema_path'], self.config['use_version'])
        with self.engine.connect() as conn:
            # Creates database file if it doesn't exist
            for table_name, table_def in schema['tables'].items():
                columns_sql = []

                for col_name, col_def in table_def['columns'].items():
                    col_parts = [col_name, col_def['type']]
                    
                    if col_def.get('primary_key'):
                        col_parts.append('PRIMARY KEY')
                    # TODO: restart from here


        return
    
    def _load_schema(self, schema_path: str, version: int):
        path = Path(schema_path).resolve()
        with path.open('r', encoding='utf-8') as f:
            data = json.load(f)
        
        if str(version) in data['versions']:
            schema = data['versions'][str(version)]
        
        # TODO: else condition

        return schema
    
    
    def backup_db(self):
        # TODO: create copy of db file with current date time appended
        return
    
    def modify_db(self):
        # TODO: fuzzy... how to make changes to db structure from within program
        return
