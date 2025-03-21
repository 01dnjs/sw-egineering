import pandas as pd

data = [{"Word": "hello", "Meaning": "안녕", "Multiplicity":1},
        {"Word": "world", "Meaning": "세계", "Multiplicity":5}]

df = pd.DataFrame(data)

print(df)