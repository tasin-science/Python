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
print("For showing different type of filling missing values, we need to Read dataframe by using different dataframe variables.")
print("Because once dataframe\'s missing value filled, then it can\'t be possible for using other methods")
df1 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\'Dataset_Lab_Test.csv\' dataframe is assigned/copied in another new dataframe \'df1\'")
print("\'Dataset_Lab_Test.csv\' dataframe is: \n", df1, "\n\n\n")
#<>
## Filling missing values with specific values
df1['Product_A'] = df1['Product_A'].fillna(0)
df1['Product_C'] = df1['Product_C'].fillna(900)
print("Filling missing values with specific values, and only showing that rows where values were missed: \n")
print(df1[37:39], "\n\n\n")
#<>
#<>
df2 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
df3 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
df4 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\'Dataset_Lab_Test.csv\' dataframe is assigned/copied in new dataframes \'df2\', \'df3\', \'df4\'")
print("Those copies are as same as \'df1\', so it is unnecessary for printing all of them. \n\n\n")
print("\'df2\' dataframe is for filling missing values with mean")
print("\'df3\' dataframe is for filling missing values with median")
print("\'df4\' dataframe is for filling missing values with mode")
#<>
#<>
## Filling missing value with the mean
df2['Product_A'] = df2['Product_A'].fillna(df2['Product_A'].mean())
df2['Product_C'] = df2['Product_C'].fillna(df2['Product_C'].mean())
print("Filling missing values with mean, and only showing that rows where values were missed: \n")
print(df2[37:39], "\n\n\n")
#<>
## Filling missing value with the median
df3['Product_A'] = df3['Product_A'].fillna(df3['Product_A'].median())
df3['Product_C'] = df3['Product_C'].fillna(df3['Product_C'].median())
print("Filling missing values with median, and only showing that rows where values were missed: \n")
print(df3[37:39], "\n\n\n")
#<>
## Filling missing value with the mode
df4['Product_A'] = df4['Product_A'].fillna(df4['Product_A'].mode()[0])
df4['Product_C'] = df4['Product_C'].fillna(df4['Product_C'].mode()[0])
print("Filling missing values with mode, and only showing that rows where values were missed: \n")
print(df4[37:39], "\n\n\n")
#<>
#<>
df5 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
df6 = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\'Dataset_Lab_Test.csv\' dataframe is assigned/copied in new dataframes \'df5\', \'df6\' ")
print("Those copies are as same as \'df1\', so it is unnecessary for printing all of them. \n\n\n")
print("\'df5\' dataframe is for filling missing values by forward fill")
print("\'df6\' dataframe is for filling missing values with backward fill")
#<>
#<>
## Forward fill
df5['Product_A'] = df5['Product_A'].ffill()
df5['Product_C'] = df5['Product_C'].ffill()
print("Filling missing values by forward fill, and only showing that rows where values were missed: \n")
print(df5[37:39], "\n\n\n")
#<>
## Backward fill
df6['Product_A'] = df6['Product_A'].bfill()
df6['Product_C'] = df6['Product_C'].bfill()
print("Filling missing values by backward fill, and only showing that rows where values were missed: \n")
print(df6[37:39], "\n\n\n")


