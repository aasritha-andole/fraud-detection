import pandas as pd

# Load the dataset
df = pd.read_csv("Nigerian_Fraud.csv")  # Replace with your actual file name

# Show the first 5 rows
print("Dataset Preview:")
print(df.head())

# Check data info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check class distribution
print("\nClass Distribution:")
print(df['label'].value_counts())
