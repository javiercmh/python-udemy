import pandas as pd

ser1 = pd.Series([1,2,3,4],index=["USA","Deutschland","Russland","Japan"])

# it should be the same
print(ser1[0] == ser1['USA'])