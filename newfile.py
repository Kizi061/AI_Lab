import numpy as np
import pandas as pd
from scipy import stats

a = [12, 34,24,53,23,43,53,23,32]

print("Mean:", np.mean(a))

data ={
    "Name": ["John", "Eva"],
    "Age": [33,20]
}

dataframe = pd.DataFrame(data)
print(dataframe)

print("Average Age: ", dataframe["Age"].mean())
print("Median Age: ", dataframe["Age"].median())
print("SD Age: ", dataframe["Age"].std())
print("Variance: ", dataframe["Age"].var())

sample = np.random.normal(loc=0,scale=1,size=1000)
print("Sample:", sample)
# print("Mean:", sample.mean(a))
