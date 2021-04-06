import pandas as pd

# df = pd.DataFrame({'KOSPI' : [1915, 1961, 2026, 2467, 2041], 'KOSDAQ' : [542, 682, 631, 798, 675]}, index=[2014, 2015, 2016, 2017, 2018])

# print("KOSPI & KOSDAQ DataFrame\n", df)
# print("KOSPI & KOSDAQ DataFrame Description\n", df.describe())
# print("\nKOSPI & KOSDAQ DataFrame Information\n"); print(df.info())

# kospi = pd.Series([1915, 1961, 2026, 2467, 2041], index=[2014, 2015, 2016, 2017, 2018], name='KOSPI')
# kosdaq = pd.Series([542, 682, 631, 798, 675], index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')

# print("KOSPI Series Data"); print(kospi)
# print("\nKOSDAQ Series Data"); print(kosdaq)

# df = pd.DataFrame({kospi.name : kospi, kosdaq.name : kosdaq})
# print("KOSPI & KOSDAQ DataFrame"); print(df)

myColumns = ['KOSPI', 'KOSDAQ']
myIndex = [2014, 2015, 2016, 2017, 2018]
myRows = []

myRows.append([1915, 542])
myRows.append([1961, 682])
myRows.append([2026, 631])
myRows.append([2467, 798])
myRows.append([2041, 675])

df = pd.DataFrame(myRows, columns=myColumns, index=myIndex)
# print("KOSPI & KOSDAQ DataFrame 2"); print(df)
# print("INDEX KOSPI KOSDAQ")
# for i in df.index:
#     print(i, ' ', df['KOSPI'][i], ' ', df['KOSDAQ'][i])

# for row in df.itertuples(name='KRX'):
#     print(row)

# print("INDEX KOSPI KOSDAQ")
# for idx, row in df.itertuples():
#     print(row[0], '', row[1], '', row[2])

print("INDEX KOSPI KOSDAQ")
for idx, row in df.iterrows():
    print(idx, '', row[0], '', row[1])