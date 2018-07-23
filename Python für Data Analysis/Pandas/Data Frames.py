import numpy as np
import pandas as pd
from numpy.random import randn  # normal distribution
np.random.seed(101)

# This is how it's done.
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

# print only 'W'
print(df['W'])

# print only columns 'W' and 'Z'. Columns are pd.Series
print(df[['W','Z']])

# adding a new column
df['new'] = pd.Series([1,2,3,4,5],index='A B C D E'.split())

print(df)

# for dropping data from DataFrame, column is 1, row is 0
df.drop('A',axis=0)
df.drop('new',axis=1,inplace=True)
print(df)

# Select rows
df.loc['A']  # row 0
df.iloc[2]   # row 'C'

df.loc['B','Y']  # df.loc[row,col]
df.loc[['A','B'],'Y']

# select only those > 0
df[df>0]
# now those with 'W' > 0 and 'Y' > 0.
df[(df['W']>0) & (df['Y']>0)]   # DO NOT forget parentheses

# An index must be already a series (that can be part of the table)
newind = pd.Series('AA AB AC AD AE'.split())
df.set_index(newind, inplace=True)

print(df.transpose())