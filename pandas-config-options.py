import pandas as pd

# Most useful options to set for pandas

# set max columns
pd.set_option('display.max_columns', 1000)
# set max rows
pd.set_option('display.max_rows', 1000)
# set display width
pd.set_option('display.width', 1000)
# set colwidth
pd.set_option("max_colwidth", 50)
# set info columns
pd.set_option("max_info_columns", 5)
# set the precision for decimals
pd.set_option("precision", 2)
# set colheader name left or right
pd.set_option("colheader_justify", "right")

# check all options here https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options

# Main relevant functions for generic configuration
pd.set_option()         # set a single option
pd.get_option()         # get single option
pd.reset_option()       # resets one or more values
pd.describe_option()    # get the descriptions of one or more configs
pd.option_context()     # execute codeblock and then reset to prior settings
