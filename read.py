import pandas as pd
from tabulate import tabulate

# Load the CSV file
df = pd.read_csv('pincode (1).csv')

# Set display options to show the full DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the contents of the CSV file in a tabulated format
print(tabulate(df, headers='keys', tablefmt='psql'))