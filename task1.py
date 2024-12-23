# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Step 1: Load the Dataset
# Replace 'student_performance.csv' with your dataset file
data = pd.read_csv("D:/.vscode/task/student_performance.csv")
print("Dataset Preview:")
print(data.head())

# Step 2: Understand the Dataset
print("\nColumns in the dataset:")
print(data.columns)

print("\nDataset Info:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Handle Missing Values
print("\nMissing Values Before Handling:")
print(data.isnull().sum())

# Fill missing values (example: fill with mean for numerical columns)
for col in data.select_dtypes(include=[np.number]).columns:
    data[col] = data[col].fillna(data[col].mean())

# Drop rows with missing values (if necessary)
# data = data.dropna()

print("\nMissing Values After Handling:")
print(data.isnull().sum())

# Step 4: Remove Duplicates
print(f"\nNumber of Duplicate Rows: {data.duplicated().sum()}")
data = data.drop_duplicates()
print(f"Number of Duplicate Rows After Removal: {data.duplicated().sum()}")

# Step 5: Encode Categorical Variables
# Identify categorical columns
categorical_cols = data.select_dtypes(include=['object']).columns
print(f"\nCategorical Columns: {categorical_cols}")

# Encode each categorical column
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

print("\nData After Encoding:")
print(data.head())

# Step 6: Scale Numerical Variables
numerical_cols = data.select_dtypes(include=[np.number]).columns
scaler = StandardScaler()
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

print("\nData After Scaling:")
print(data.head())

# Step 7: Data Visualization (Optional)
# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 8: Split Data for Model Training
# Define Features (X) and Target (y)
target_column = 'Test_Score'  # Set your target column here

if target_column not in data.columns:
    raise KeyError(f"Target column '{target_column}' not found in the dataset.")

X = data.drop([target_column, 'Name'], axis=1)  # Drop the target and irrelevant columns
y = data[target_column]  # Define the target variable

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTrain-Test Split Completed.")
print(f"Training Data Size: {X_train.shape}")
print(f"Testing Data Size: {X_test.shape}")

# Save Processed Dataset
data.to_csv("D:/.vscode/task/processed_data.csv", index=False)
print("Processed dataset saved successfully.")

