import pandas as pd
import numpy as np
import seaborn as sns

# we use the iris dataset from seaborn
df = sns.load_dataset('iris')

# show top and bottom of dataset
df.head()
df.tail()

# this shows the shape (number of rows and columns)
df.shape()

# check basic statistics
df.describe()

# check data types and more
df.info()
