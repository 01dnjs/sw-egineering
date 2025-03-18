from abc import ABC, abstractmethod


class BaseQuizModel(ABC):
    def __init__(self, db):
        parsed_db = self.__parse_db(db)
        QAHpairs = self.__create_pairs(db)

    @abstractmethod
    def __parse_db(self, db):
        pass

    @abstractmethod
    def __create_pairs(self, parsed_db):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass