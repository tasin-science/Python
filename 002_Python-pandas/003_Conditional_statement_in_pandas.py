#### Conditional Statement in Pandas

# Note: For conditional statement, it is better to use df['<column_name>'], not df[['<column_name>']]

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
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
print("max() of df1:")
print("for Product_A in df1: ", df1['Product_A'].max())
print("for Product_B in df1: ", df1['Product_B'].max())
print("for Product_C in df1: ", df1['Product_C'].max(), "\n")

