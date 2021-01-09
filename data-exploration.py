import pandas as pd
import numpy as np
import seaborn as sns

# seaborn comes with build in datasets which we will use
df = sns.load_dataset('tips')

# show top and bottom of dataset
df.head()
df.tail()

# this shows the shape (number of rows and columns)
df.shape()

# check data types and more
df.info()

# check basic statistics
df.describe()  # analyzes numberic numbers only
# if other data types are there as well you can include it, here with object
df.describe(include=np.object)

# count number of the items of specfic column
df['day'].value_counts()

# # slice dataframe with loc
