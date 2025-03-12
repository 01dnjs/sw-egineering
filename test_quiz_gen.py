import pandas as pd
from quiz_gen import question_from_LLM
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str)

args = parser.parse_args()

if not args.api_key:
    print('api key must be set')

data = [{'Word': 'abundance', 'Meaning': '풍부'}, {'Word': 'basin', 'Meaning': '양푼, (큰강의) 유역'}]
columns = ['Word', 'Meaning']

df = pd.DataFrame(data=data, columns=columns)

q = question_from_LLM(df, columns, "gemini-2.0-flash", args.api_key)

print(q)