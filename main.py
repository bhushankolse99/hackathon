import pandas as pd

# Extract: Load the CSV file
df = pd.read_csv('pincode.csv')

# Transform: Perform data transformations
# Example transformations:
# - Drop rows with missing values
# - Convert column names to lowercase
# - Filter rows based on a condition

df.dropna(inplace=True)
df.columns = [col.lower() for col in df.columns]
df = df[df['pincode'] > 100000]  # Example condition

# Load: Save the transformed data to a new CSV file
df.to_csv('transformed_pincode.csv', index=False)

# Display the transformed data
print(df.pincode)