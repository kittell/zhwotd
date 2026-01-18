from domain.word import Word
from models.word import DB_Word

def orm_to_domain(orm_obj: DB_Word) -> Word:
    return Word(
        word=orm_obj.word,
        pinyin=orm_obj.pinyin,
        traditional=orm_obj.traditional,
        definitions=orm_obj.definitions,
        examples=orm_obj.examples,
        hsk=orm_obj.hsk,
        notes=orm_obj.notes,
    )

def domain_to_orm(domain_obj: Word) -> DB_Word:
    return DB_Word(
        word=domain_obj.word,
        pinyin=domain_obj.pinyin,
        traditional=domain_obj.traditional,
        definitions=domain_obj.definitions,
        examples=domain_obj.examples,
        hsk=domain_obj.hsk,
        notes=domain_obj.notes,
    )
