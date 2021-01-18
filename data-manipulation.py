import pandas as pd
import numpy as np

# create example dataframe
df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])


# -------------------------
#  handle columns

# rename columns
df = df.rename(columns={'num_legs': 'renamed_leg'})

# drop / delete columns
df = df.drop('num_legs', axis=1)
del df['num_wings']

# add new column
color = ['blue', 'red', 'yellow', "green"]
df['new_column'] = color


# -------------------------
#  handle missing values

# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())
df.isna().any()

# Drop missing values
df = df.dropna()

# drop undefined values
df = df[(df['column_name'] != 'undefined')]


# group by column values
df.groupby(['column_name1', 'column_name2', 'column_name3'])

# group and calculate mean / median
df.groupby(['column_name1', 'column_name2', 'column_name3']).mean()
df.groupby(['column_name1', 'column_name2', 'column_name3']).median()
