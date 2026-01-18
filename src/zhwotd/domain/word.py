class Word:
    def __init__(self, word, pinyin="", traditional="", definitions=None, examples=None, hsk=0, notes=""):
        self.word = word
        self.pinyin = pinyin
        self.traditional = traditional
        self.definitions = definitions or []
        self.examples = examples or []
        self.hsk = hsk
        self.notes = notes

    def to_simplified(self):
        # example domain logic
        return self.word

    def is_hsk_level(self, level):
        return self.hsk == level
