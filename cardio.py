import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

# Load the dataset
df = pd.read_csv('cardio.csv', delimiter=';')

# Display the size of the dataset
print(f"Dataset Size: {df.shape}")

# Check for missing values
missing_values = df.isnull().sum()
print(f"Missing Values: \n{missing_values}")

# Visualize missing values (if any)
msno.matrix(df)
plt.show()

# Optional: Create a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.show()
