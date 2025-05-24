# Dataloading 
import os
import pandas as pd 

s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
print('From URL:',s)

df = pd.read_csv(s,
                header=None,
                encoding = 'utf-8')
print(df.tail(5))