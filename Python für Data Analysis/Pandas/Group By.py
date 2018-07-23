import pandas as pd

data = {'Firma':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

# First group by
gb_firma = df.groupby('Firma')
# then, say what how we are grouping
gb_firma.mean()
gb_firma.sum()
gb_firma.std()
gb_firma.min()
gb_firma.max()
gb_firma.count()

# same as doing all together
print(df.groupby('Firma').describe())


