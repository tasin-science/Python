#### Advanced manipulations

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\n\n\n Whole dataframe \'df\' is shown: ", "\n")
print(df)

print("\n\n\n")


### Indexing and slicing the dataframe
print("index 10 to 20 in the dataframe are shown by using df[10:21]: \n")
print(df[10:21], "\n\n\n") #index 10 to 20


### Columns printing
print("Column's are showing by using df.columns:")
print(df.columns, "\n\n\n")


### Single Column dataframe
#<>
## First type doesn't show header
print("Headerless one column Product_A is printing by df.Product_A: \n")
print(df.Product_A, "\n\n\n")
#<>
## Second type doesn't show header, but it is Series printing. It is not applicable for selecting tuples of multiple columns
print("Headerless Product_A column series dataframe is printing by df['Product_A']: \n")
print(df['Product_A'], "\n\n\n")
#<>
## Third type shows header, and it is also applicable for selecting tuples of multiple columns
print("Product_A column dataframe is printing by df[[\'Product_A\']]: \n")
print(df[['Product_A']], "\n\n\n")
#<>
# note: it is better to use [[]] whatever single column or multiple column in dataframe manipulation.
# note: for conditional statement or mean(), std(), min(), var(); then [] used. 
#<>
## ".shape", head(), tail() for single column dataframe
print("Printing .shape for df[[\'Product_A\']]: ", df[['Product_A']].shape, "\n\n\n")
print("Printing head() for df[[\'Product_A\']]: \n\n", df[['Product_A']].head(), "\n\n\n")
print("Printing head(10) for df[[\'Product_A\']]: \n\n", df[['Product_A']].head(10), "\n\n\n")
print("Printing tail() for df[[\'Product_A\']]: \n\n", df[['Product_A']].tail(), "\n\n\n")
print("Printing tail(10) for df[[\'Product_A\']]: \n\n", df[['Product_A']].tail(10), "\n\n\n")
#<>
## Indexing and slicing for single column dataframe
df1 = df[['Product_A']]
print("df[[\'Product_A\']] is kept into new dataframe df1")
print("So, index 10 to 20 in that df1 dataframe are shown by using df1[10:21]: \n")
print(df1[10:21], "\n\n\n") #index 10 to 20



### Multiple column dataframe 
print("Product_A, Product_B, Product_C columns dataframe is printing by df[[\'Product_A\', \'Product_B\', \'Product_C\']]: \n")
print(df[['Product_A', 'Product_B', 'Product_C']], "\n\n\n")
# note: it is better to use [[]] whatever single column or multiple column in dataframe manipulation. 
#<>
# ".shape", head(), tail() for multiple column dataframe
print("Printing .shape for df[[\'Product_A\', \'Product_B\', \'Product_C\']]: ", df[['Product_A', 'Product_B', 'Product_C']].shape, "\n\n\n")
print("Printing head() for df[[\'Product_A\', \'Product_B\', \'Product_C\']]: \n\n", df[['Product_A', 'Product_B', 'Product_C']].head(), "\n\n\n")
print("Printing head(10) for df[[\'Product_A\', \'Product_B\', \'Product_C\']]: \n\n", df[['Product_A', 'Product_B', 'Product_C']].head(10), "\n\n\n")
print("Printing tail() for df[[\'Product_A\', \'Product_B\', \'Product_C\']]: \n\n", df[['Product_A', 'Product_B', 'Product_C']].tail(), "\n\n\n")
print("Printing tail(10) for df[[\'Product_A\', \'Product_B\', \'Product_C\']]: \n\n", df[['Product_A', 'Product_B', 'Product_C']].tail(10), "\n\n\n")
## Indexing and slicing for single column dataframe
df2 = df[['Product_A']]
print("df[[\'Product_A\']] is kept into new dataframe df2")
print("So, index 10 to 20 in that df2 dataframe are shown by using df2[10:21]: \n")
print(df2[10:21], "\n\n\n") #index 10 to 20



### max()
#<>
## max() printing by df[]
print("max() of Product_A, Product_B, Product_C printing for df[]: \n")
print(df['Product_A'].max())
print(df['Product_B'].max())
print(df['Product_C'].max())
print("\n\n\n")
#<>
## max() printing as df[[]]
print("max() of Product_A, Product_B, Product_C printing for df[[]]: \n")
print(df[['Product_A']].max())
print(df[['Product_B']].max())
print(df[['Product_C']].max())
print("\n\n\n")
#<>
## Check the types
print("Let\'s check the type of both df[].max() and df[[]].max() using:\n")
print("type(df[\'Product_A\'].max()) is:\n", type(df['Product_A'].max()))
print("type(df[[\'Product_A\']].max()) is:\n", type(df[['Product_A']].max()))
print("\n\n\n")
#<>
# Same are applicable for mean(), std(), min(), var()
# note: it is better to use [] for max(), mean(), std(), min(), var() because it gives only number. 


### mean()
print("mean() of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].mean())
print(df['Product_B'].mean())
print(df['Product_C'].mean())
print("\n\n\n")

### min()
print("min() of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].min())
print(df['Product_B'].min())
print(df['Product_C'].min())
print("\n\n\n")

### variance
print("variance [var()] of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].var())
print(df['Product_B'].var())
print(df['Product_C'].var())
print("\n\n\n")

### standard deviation
print("standard deviation [std()] of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].std())
print(df['Product_B'].std())
print(df['Product_C'].std())
print("\n\n\n")

### mode()
#<>
## normally printing mode by df[]
print("mode() of Product_A, Product_B, Product_C printing by df[]: \n")
print(df['Product_A'].mode(), "\n")
print(df['Product_B'].mode(), "\n")
print(df['Product_C'].mode(), "\n")
print("\n\n\n")
#<>
## normally printing mode by df[[]]
print("mode() of Product_A, Product_B, Product_C printing by df[[]]: \n")
print(df[['Product_A']].mode(), "\n")
print(df[['Product_B']].mode(), "\n")
print(df[['Product_C']].mode(), "\n")
print("\n\n\n")
#<>
## Together Product_A, Product_B, Product_C mode() printing
print("mode() of Product_A, Product_B, Product_C printing together: \n")
print(df[['Product_A', 'Product_B', 'Product_C']].mode(), "\n")
#<>
## using tolist() with mode()
print("mode().tolist() of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].mode().tolist())
print(df['Product_B'].mode().tolist())
print(df['Product_C'].mode().tolist())
print("\n\n\n")


### describe()
#<>
## describe() printing by df[]
print("describe() of Product_A, Product_B, Product_C printing by df[]: \n")
print(df['Product_A'].describe(), "\n")
print(df['Product_B'].describe(), "\n")
print(df['Product_C'].describe(), "\n")
print("\n\n\n")
#<>
## describe() printing by df[[]]
print("describe() of Product_A, Product_B, Product_C printing by df[[]]: \n")
print(df[['Product_A']].describe(), "\n")
print(df[['Product_B']].describe(), "\n")
print(df[['Product_C']].describe(), "\n")
print("\n\n\n")
#<>
## describe() printing by df[[]] as multiple columns together
print("describe() of Product_A, Product_B, Product_C together printing by df[[]]: \n")
print(df[['Product_A', 'Product_B', 'Product_C']].describe())
print("\n\n\n")
#<>
# note: it is better to use mode(), describe() as [[]]


### another systemic printing describe
#<>
## Calculate statistics for Product_A
print("Another way to print describe without describe() function: \n")
average = df['Product_A'].mean()
std_dev = df['Product_A'].std()
variance = df['Product_A'].var()
median = df['Product_A'].median()
mode = df['Product_A'].mode()
#<>
## Display the results
print(f"Average (Mean) of Product_A: {average}")
print(f"Standard Deviation of Product_A: {std_dev}")
print(f"Variance of Product_A: {variance}")
print(f"Median of Product_A: {median}")
print(f"Mode of Product_A: {mode.tolist()}")
print("\n\n\n")


### Index System
#<>
## Range Index
print("Range Index is: ", df.index, "\n\n\n")
#<>
## set_index()
print("Making Product_A as index of dataframe: \n",)
print(df.set_index('Product_A'))
print("\n\n\n")
#<>
## inplace=True and locating in set_index()
print("Making Product_C as permanent index and locating value 800.0:")
print(df.set_index('Product_C', inplace=True), "\n") # Permanent index setting
print(df.loc[800.0])
print("\n\n\n")
#<>
## reset_index()
print("Resetting index and showing dataframe: \n")
print(df.reset_index(inplace=True)) ## Permanent reset
print(df)
print("\n\n\n")