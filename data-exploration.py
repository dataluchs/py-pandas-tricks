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

# check unique values of column
df['day'].unique()

# print df as nice markdown table # requires package tabulate: https://pypi.org/project/tabulate/
df.to_markdown()
df.to_markdown(tablefmt="grid")

# .loc function
# if index is set, use .loc to explore by index
df.set_index('column_to_index', inplace=True)
df.loc['indexvalue']
df.loc[['indexvalue1', 'indexvalue2']]

# select additionally by column with selected index values
df.loc[['indexvalue1', 'indexvalue2'], ['column_name1', 'column_name2']]
# select column range by selected indexes
df.loc[['indexvalue1', 'indexvalue2'], 'column_name1':'column_name2']
