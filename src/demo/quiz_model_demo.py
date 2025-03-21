import os
import sys

# base_quiz_gen_class.py 찾기
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "quiz generation"))

sys.path.insert(0, parent_dir)


from base_quiz_gen_class import BaseQuizModel
import pandas as pd

def main():
    # 각 Quiz Model 들은 BaseQuizModel 을 상속하며, 동일한 interface 를 제공함
    # 이 Quiz Model 로부터 (Question, Answer, Hint) pair 를 받아오는 2 가지 예제는 밑의 use case 확인
    class TestQuizModel(BaseQuizModel):
        def __init__(self, db, APIKEY):
            self.__parsed_db: pd.DataFrame = self._parse_db(db)
            self.__pairs = self._create_pairs(self.__parsed_db, APIKEY)

        def _parse_db(self, db):
            # 실제로는 db 를 parsing 하지만, demo 이므로 간단히 구현
            data = [{"Word": "hello", "Meaning": "안녕", "Multiplicity":1},
                    {"Word": "world", "Meaning": "세계", "Multiplicity":5}]

            return pd.DataFrame(data)

        def _create_pairs(self, parsed_db: pd.DataFrame, APIKEY):
            question_template = "다음 의미를 가지는 단어의 뜻은?: {0}"
            default_hint = "Hint"
            return [(question_template.format(row[0]), row[1], default_hint) for row in parsed_db.itertuples(index=False, name=None)]

        def get(self):
            """
            Returns every (Question, Answer, Hint) pairs

            Returns:
                List[Tuple[str,str,str]]: List of (Question, Answer, Hint)
            """
            return self.__pairs
        
        def __iter__(self):
            self.__index = 0
            return self


        def __next__(self):
            if self.__index >= len(self.__pairs):
                raise StopIteration
            
            result = self.__pairs[self.__index]
            self.__index += 1
            return result

    # 실제로는 database 로부터 반환된 변수
    db = "Some DB"

    # API Key 를 사용할지는 개별 quiz model 확인
    quiz_model = TestQuizModel(db, None)

    # Use case 1
    print("=============== Use case 1 ===============")
    pairs = quiz_model.get()

    for pair in pairs:
        print(pair)

    print()

    # Use case 2
    print("=============== Use case 2 ===============")

    for pair in quiz_model:
        print(pair)

if __name__ == "__main__":
    main()