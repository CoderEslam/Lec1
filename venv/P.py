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
