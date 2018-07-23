import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3],
                  'D':[3,6,9]})

print(df)

# axis=0 is rows, axis=1 is columns
df.dropna() # axis=0 by default
df.dropna(axis=1)

len(df)          # number of cases
cols = len(df.columns)  # number of columns

# don't keep those with less than 80% of valid data
threshold = int(cols*0.8)
df.dropna(thresh=threshold)

# fill NA with plausible data
df['A'].fillna(value=df['A'].mean(),inplace=True)
print(df)
