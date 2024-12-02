import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('transformed_pincode.csv')

# Example visualization: Histogram of a column (e.g., 'pincode')
plt.figure(figsize=(10, 6))
sns.histplot(df['pincode'], bins=30, kde=True)
plt.title('Distribution of Pincodes')
plt.xlabel('Pincode')
plt.ylabel('Frequency')
plt.show()

# Example visualization: Scatter plot of two columns (e.g., 'pincode' vs 'delivery')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pincode', y='delivery', data=df)
plt.title('Pincode vs Delivery')
plt.xlabel('Pincode')
plt.ylabel('Delivery')
plt.show()

# Example visualization: Pie chart of deliveries by district
district_delivery_counts = df.groupby('district')['delivery'].sum()
plt.figure(figsize=(10, 6))
district_delivery_counts.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Deliveries by District')
plt.ylabel('')  # Hide the y-label
plt.show()