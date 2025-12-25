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