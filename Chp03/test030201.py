import pandas as pd          # pip install pandas

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])

# print("s Series :\n", s)
s.name = "MY_SERIES"

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX'

# print("s Series added index + index name :\n", s)

s[5.9] = 5.5

# print("s Series added index label + Value :\n", s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
# print("ser Series :\n", ser)

s = s.append(ser)
# print("\ns Series added ser Series :\n", s)
# print("Last Index Label :", s.index[-1])
# print("Series Data Value of Last Index :", s.values[-1])
# print("Series Data Value by Location Indexer :", s.loc[8.0])
# print("\nSeries Data Value by Integer Location Indexer (Integer=3) :", s.iloc[3])
# print("Series Data Value by Integer Location Indexer (Last Index) :", s.iloc[-1])

# print("Series Data Values returned by values :\n", s.values[:])
# print("\nSeries Data Values returned by iloc :\n", s.iloc[:])

# print("\nDelete Series Data Value that has index label 8.0 :\n", s.drop(8.0))

# print("s Series Description :\n", s.describe())

import matplotlib.pyplot as plt
plt.title("ELLIOTT WAVE")
plt.plot(s, 'bs--')
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()