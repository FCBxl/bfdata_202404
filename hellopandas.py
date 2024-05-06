import numpy as np
import pandas as pd


s = pd.Series([10,30,np.nan,40,62,18])
print(s)

dates = pd.date_range("2024-4-29", periods=6, freq="h")
s = pd.Series([10,30, np.nan, 40, 62,18], index=dates)
print(s)

# Creation data frame

rnd = np.random.randn(6,4)
print(rnd)

df = pd.DataFrame(rnd, index=dates, columns=["A", "B", "C", "D"])
print(df)
print(df["A"])

print(df[df["A"] > 0])


data = {
    "User": ["user1", "user2", "user3"],
    "Score": [15,75,0]
}

scores = pd.DataFrame(data)
print(scores)