class WOTD:
    def __init__(self, word: str, date: str):
        self.word = word
        self.date = date

    # def __repr__(self):
    #     return f"WOTD(word={self.word}, definition={self.definition}, example={self.example})"

class Word:
    def __init__(self, word: str, pinyin: str, traditional: str, definitions: list[str], examples: list[str]=None, hsk: int=0, notes: str=''):
        self.word = word
        self.pinyin = pinyin
        self.traditional = traditional
        self.definitions = definitions
        self.examples = examples
        self.hsk = hsk
        self.notes = notes

class DatabaseManager:
    """Handle operations involving the entire database and its structure
    """
    def __init__(self):
        return
    
    def create_db(self):
        # TODO: to be called from GUI admin page or command line
        # TODO: read schema from json file; consider how to manage different schema versions
        # TODO: provide popup window with text box and keywords if doesn't exist
        return
    
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