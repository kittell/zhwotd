import sqlite3
from pathlib import Path
import json
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import Row
from typing import Any, List

from contextlib import contextmanager
from zhwotd.db.engine import SessionLocal

class DatabaseManager:
    """
    Handle operations involving the entire database and its structure
    """
    def __init__(self, config):
        self.config = config
        return

    @contextmanager
    def session(self):
        db = SessionLocal()
        try:
            yield db
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.close()

    def execute(self, fn):
        """
        Run query-building function inside a managed session
        
        :param fn: 
        """
        with self.session() as db:
            return fn(db)
    
    def add(self, obj):
        with self.session() as db:
            db.add(obj)

    def get_all(self, model):
        with self.session() as db:
            return db.query(model).all()

    def get_by_id(self, model, id_):
        with self.session() as db:
            return db.query(model).filter(model.id == id_).first()
    
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
        
        schema = {}
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