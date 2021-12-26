import numpy as np
import pandas as pd
from numpy.random import randn

a = list([5, 6, 9, 5])
b = list([5, 7, 6, 3])

print(a + b)
######################################
a = np.array(a)
b = np.array(b)
print(a)
print(b)
print(a + b)
###########################################

# pandas lib
header = ["Name", "Age", "Weight"]
value = ["Eslam", 25, 72]

mySer = pd.Series(data=value, index=header)
print(mySer)

print("Name of Data = " + mySer["Name"])

sem_1 = pd.Series(data=[25, 66], index=["Math", "Pythices"])
print(sem_1)

sem_2 = pd.Series(data=[64, 36, 66], index=["Math", "CS", "Pythices"])
print(sem_2)

print(sem_1 + sem_2)
############################################
# create data frame
#  random data
df = pd.DataFrame(randn(3, 3), index=['X', 'Y', 'Z'], columns=['C1', 'C2', 'C3'])

print(df)
# get data from spacific col
print(df['C1'])

print(df[['C1', 'C3']])

df['C4'] = df['C1'] + df['C3']

print("The Sum = ", df['C4'])

# to get spacific location row
print(df.loc['Y'])

print(df.iloc[2])
#  get value in 2  col only
print(df.loc[['X', 'Z']])
#  get value in a spacific col with spacific row
print(df.loc[['X', 'Z'], ['C1', 'C3']])

# to drop a column and row
print(df.drop('C4', axis=1))
# but it doen't delete original data
print(df)

# if i want to realy dalet it use inplace=True
df.drop('C4', axis=1, inplace=True)
print(df)
df = pd.DataFrame(randn(5, 3), index=['A', 'B', 'C', 'D', 'E'], columns=['C1', 'C2', 'C3'])
print(df)
print("print filter all columns by true or false")
print(df <= 0)

print("print filter all columns by NaN")

df2 = df[df <= 0]

print(df2)

print("print filter one  column")

df2 = df[df['C2'] <= 0]
print(df2)

print("print filter tow  columns")
df2 = df[(df['C2'] <= 0) | (df['C1'] >= .5)]
print(df2)

df = pd.DataFrame([[15, 25, 66],
                   [np.nan, 88, 102],
                   [np.nan, 99, np.nan]
                   ],
                  index=['A', 'B', 'C'],
                  columns=['C1', 'C2', 'C3'])
print(df)

# to drop missing value
df.dropna()
print(df.dropna())

# to remove column
print(df.dropna(axis=1))

# to remove data if they omre than 2 or equal 2
print(df.dropna(axis=1, thresh=2))


#  to fill data if it's missing
df.fillna(500)
print(df.fillna(500))

print (df.fillna(df['C2'].mean()))





