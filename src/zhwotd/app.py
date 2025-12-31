import json
import os
from pathlib import Path
import sqlite3
from sqlalchemy import create_engine, text
from zhwotd.gui import GUI



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

    def start(self):
        self.dbm.connect()
        gui = GUI(self, self.config['gui'])
        return
    
    def find_word(self, word) -> str:
        result = ''
        query_builder = QueryBuilder()
        query = query_builder.find_word(word)
        print('query:', query)
        query_result = self.dbm.execute(text(query))
        print('query_result:', query_result)
        return result
    

class DatabaseManager:
    """Handle operations involving the entire database and its structure
    """
    def __init__(self, config):
        self.config = config
        return
    
    def connect(self):
        db_type = self.config['type']
        db_name = self.config['name']
        script_dir = Path(__file__).resolve().parent
        db_path = script_dir / db_name
        self.db_url = db_type + ':///' + str(db_path)

        self.engine = create_engine(self.db_url)
        if Path(self.db_url).is_file() == False:
            self.create_new_db()

        return
    
    def execute(self, query: str) -> list:
        results = []
        with self.engine.connect() as conn:
            result = conn.execute(query)
            return result.fetchall()
        return results
        

    def create_new_db(self):
        
        schema = self._load_schema(self.config['schema'], self.config['use_version'])
        with self.engine.connect() as conn:
            # Creates database file if it doesn't exist
            # TODO: don't automatically create database, give popup to create or cancel
            for table_name, table_def in schema['tables'].items():
                columns_sql = []

                for col_name, col_def in table_def['columns'].items():
                    col_parts = [col_name, col_def['type']]
                    
                    if col_def.get('primary_key'):
                        col_parts.append('PRIMARY KEY')
                    if col_def.get('autoincrement'):
                        col_parts.append('AUTOINCREMENT')
                    if col_def.get('unique'):
                        col_parts.append('UNIQUE')
                    if col_def.get('nullable', True):
                        col_parts.append('NOT NULL')

                    columns_sql.append(' '.join(col_parts))

                # Foreign keys
                for fk in table_def.get('foreign_keys', []):
                    fk_sql = f"FOREIGN KEY ({fk['column']}) REFERENCES {fk['references']}({fk['ref_column']})"
                    columns_sql.append(fk_sql)
                create_sql = f'''
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        {', '.join(columns_sql)}
                    );
                '''

                conn.execute(text(create_sql))
        return
    
    def _load_schema(self, schema_path: str, version: int):
        path = Path(__file__).resolve().parent
        path = path / schema_path
        print(path)
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

