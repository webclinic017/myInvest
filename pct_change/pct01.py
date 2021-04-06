import pandas as pd

score = pd.Series([10, 20, 50, 55, 70], name='SCORE')
score_pct = score.pct_change(periods=2)

print(score)
print(score_pct)

df = pd.DataFrame({score.name:score, 'PCT':score_pct})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')
print(df)