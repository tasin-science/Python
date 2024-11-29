#### Handling missing data

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n")

### Checking missing datas
print(df.isnull().sum(), "\n")
### Priniting rows which contains missing values
print(df[df.isnull().any(axis=1)], "\n\n")

### Dropping missing values
print(df.dropna(), "\n\n")
print(df.dropna(axis=1), "\n\n")

### filling missing values with a specific value
df['Product_A'] = df['Product_A'].fillna(0)
df['Product_C'] = df['Product_C'].fillna(900)
print(df[37:39], "\n\n")








###
# Fill with the mean/median/mode
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].mean())
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].median())
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].mode()[0])

# Forward/Backward fill
# data['Column_Name'] = data['Column_Name'].fillna(method='ffill')  # Forward fill
# data['Column_Name'] = data['Column_Name'].fillna(method='bfill')  # Backward fill
