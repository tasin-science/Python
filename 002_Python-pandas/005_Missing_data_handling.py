#### Handling missing data

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\n\n\n Whole dataframe \'df\' is shown: ", "\n")
print(df, "\n\n\n")

### isnull() function
#<>
## Checking missing data
print("Checking missing data: ")
print(df.isnull().sum(), "\n\n\n")
#<>
## Priniting rows which contains missing values
print("Printing rows which contains missing values: \n")
print(df[df.isnull().any(axis=1)], "\n\n\n")
#<>
## Printing only isnull() function
print("Only isnull() function shows false and true boolean. Only missing values are here true, otherwise false: \n")
print(df.isnull(), "\n\n\n\n")


### dropna() function
#<>
## Dropping rows which contains missing values
print("Dropping rows which contains missing values: \n")
print(df.dropna(), "\n\n\n")
#<>
## Dropping columns which contains missing values
print("Dropping columns which contains missing values: \n")
print(df.dropna(axis=1), "\n\n\n")



### Filling missing values
print("For showing different type of filling missing values, we need to assign/copy main dataframe \'df\' to another dataframe.")
print("Because if once main dataframe\'s missing value filled, then it can\'t be possible to restore that")
df1 = df
print("\'df\' dataframe is assigned/copied in another new dataframe \'df1\'")
print("\'df1\' dataframe is: \n", df1, "\n\n\n")
#<>
## Filling missing values with specific values
df1['Product_A'] = df1['Product_A'].fillna(0)
df1['Product_C'] = df1['Product_C'].fillna(900)
print("Filling missing values with specific values, and only showing that rows where values were missed: \n")
print(df1[37:39], "\n\n")








###
# Fill with the mean/median/mode
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].mean())
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].median())
# data['Column_Name'] = data['Column_Name'].fillna(data['Column_Name'].mode()[0])

# Forward/Backward fill
# data['Column_Name'] = data['Column_Name'].fillna(method='ffill')  # Forward fill
# data['Column_Name'] = data['Column_Name'].fillna(method='bfill')  # Backward fill
