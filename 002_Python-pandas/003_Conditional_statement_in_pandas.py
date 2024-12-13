#### Conditional Statement in Pandas

# Note: For conditional statement, it is better to use df['<column_name>'], not df[['<column_name>']]

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\n\n\n Whole dataframe \'df\' is shown: ", "\n")
print(df, "\n\n\n")

### Using Conditional Operation
print("Printing dataframe where Product_A value>=1800 \n")
print(df[df['Product_A']>= 1800], "\n\n\n")
print("Printing dataframe where Product_C value<1100 \n")
print(df[df['Product_C']< 1100], "\n\n\n")


### Finding row of maximum/minimum
print("Finding row of maximum of Product_C and Product_A: ")
print(df["Product_C"] == df["Product_C"].max(), "\n")
print(df["Product_A"] == df["Product_A"].max(), "\n")
#<>
# for minimum, write df["Product_C"] == df["Product_C"].min()


### Advance manipulations in conditional statement
#<>
## ".shape", head(), tail()
print("Printing .shape for df[\'Product_A\']>=2000: ", df[df['Product_A']>=2000].shape, "\n\n\n")
print("Printing head() for df[\'Product_A\']>=2000: \n\n", df[df['Product_A']>=2000].head(), "\n\n\n")
print("Printing head(10) for df[\'Product_A\']>=2000: \n\n", df[df['Product_A']>=2000].head(10), "\n\n\n")
print("Printing tail() for df[\'Product_A\']>=2000: \n\n", df[df['Product_A']>=2000].tail(), "\n\n\n")
print("Printing tail(10) for df[\'Product_A\']>=2000: \n\n", df[df['Product_A']>=2000].tail(10), "\n\n\n")
#<>
## max(), min(), std(), mean(), median(), mode(), describe()
df1 = df[df['Product_A']>= 2000]
print("df[\'Product_A\']>= 2000 tuples are stored in a new dataframe df1")
print("df1 dataframe is: \n", df1, "\n\n\n")
#<>
# Note: max() of df1 is as same as max() of df in this program
#<>
print("min() of df1:")
print("for Product_A in df1: ", df1['Product_A'].min())
print("for Product_B in df1: ", df1['Product_B'].min())
print("for Product_C in df1: ", df1['Product_C'].min(), "\n\n\n")
print("std() of df1 vs std() of df")
print("for Product_A, std() of df1: ", df1['Product_A'].std(), " but std() of df: ", df['Product_A'].std())
print("for Product_B, std() of df1: ", df1['Product_B'].std(), " but std() of df: ", df['Product_B'].std())
print("for Product_C, std() of df1: ", df1['Product_C'].std(), " but std() of df: ", df['Product_C'].std(), "\n\n\n")
print("mean() of df1: ")
print("for Product_A in df1: ", df1['Product_A'].mean())
print("for Product_B in df1: ", df1['Product_B'].mean())
print("for Product_C in df1: ", df1['Product_C'].mean(), "\n\n\n")
print("median() of df1: ")
print("for Product_A in df1: ", df1['Product_A'].median())
print("for Product_B in df1: ", df1['Product_B'].median())
print("for Product_C in df1: ", df1['Product_C'].median(), "\n\n\n")
print("mode() of df1: ")
print("for Product_A in df1: \n\n", df1[['Product_A']].mode())
print("for Product_B in df1: \n\n", df1[['Product_B']].mode())
print("for Product_C in df1: \n\n", df1[['Product_C']].mode(), "\n\n\n")
print("describe() of df1: ")
print("for Product_A in df1: \n\n", df1[['Product_A']].describe())
print("for Product_B in df1: \n\n", df1[['Product_B']].describe())
print("for Product_C in df1: \n\n", df1[['Product_C']].describe(), "\n\n\n")
#<>
df2 = df[df['Product_A']<= 2000]
print("df[\'Product_A\']<= 2000 tuples are stored in a new dataframe df2")
print("df2 dataframe is: \n", df2, "\n\n\n")
print("max() of df2:")
print("for Product_A in df2: ", df2['Product_A'].max())
print("for Product_B in df2: ", df2['Product_B'].max())
print("for Product_C in df2: ", df2['Product_C'].max(), "\n\n\n")