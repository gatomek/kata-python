import pandas as pd

s = pd.Series([14,15,16,17,18])
print( s)

# creating with map
df = pd.DataFrame(
    {'age': 18, 'name': ['Alice', 'Bob', 'Carl'], 'cardio': [60, 70, 80]})
print( df)

# creating
df2 = pd.DataFrame(
    18, ['Alice', 'Bob', 'Carl'], [60, 70, 80])
print( df2)

# importing from file
path = "rsc/test.csv"
df3 = pd.read_csv(path)
print( df3)

# select column
print( df3[ 'age'])
print( df3.age)
print( df3.age[0:1])
print( df3[0:2])
print( df3.iloc[1,1])

# boolean indexing

print(df3[ df.cardio > 60])
print(df3[ [False, False, True]])
print( df3.cardio > 60)
print( df3.loc[:,'name'])
print( df3.loc[:,['name']])
print( df3.loc[:,['name','age']])
df3.age = 12
df3['age'] = 13
print( df3)
df3.loc[0:1, 'age'] = 14
print( df3)

# adding new column by broadcasting
df3.loc[:, 'friend'] = 'Domino'
print( df3)
