#### Advanced manipulations

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print("\n\n\n Whole dataframe \'df\' is shown: ", "\n")
print(df)

print("\n\n\n")



### Indexing and slicing the dataframe
print("index 10 to 20 in the dataframe are shown as using df[10:21]: \n")
print(df[10:21], "\n\n\n") #index 10 to 20




### Columns printing
print("Column's are showing by using df.columns:")
print(df.columns, "\n\n\n")



### One Column tuples printing
#<>
## First type doesn't show header
print("Headerless one column Product_A is printing by df.Product_A: \n")
print(df.Product_A, "\n\n\n")
#<>
## Second type doesn't show header, but it is Series printing. This doesn't allow for showing multiple columns
print("Headerless Product_A column series dataframe is printing by df['Product_A']: \n")
print(df['Product_A'], "\n\n\n")
#<>
## Third type shows header, and it is applicable for multiple column
print("Product_A column dataframe is printing by df[['Product_A']]: \n")
print(df[['Product_A']], "\n\n\n")





### Multiple column printing
print("Product_A, Product_B, Product_C columns dataframe is printing by df[['Product_A', 'Product_B','Product_C']]: \n")
print(df[['Product_A','Product_B','Product_C']], "\n\n\n")
# note: it is better to use [[]] whatever single column or multiple column in dataframe manipulation. 





### max()
#<>
## max() printing by df[]
print("max() of Product_A, Product_B, Product_C printing by df[]: \n")
print(df['Product_A'].max())
print(df['Product_B'].max())
print(df['Product_C'].max())
print("\n\n\n")
#<>
## max() printing as df[[]]
print("max() of Product_A, Product_B, Product_C printing by df[[]]: \n")
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
# Same are applicable for mean(), std(), min(), var(), mode()
# note: it is better to use [] for max(), mean(), std(), min(), var(), mode() because it gives only number. 



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
print("\n\n")

### variance
print("variance [var()] of Product_A, Product_B, Product_C printing: \n")
print(df['Product_A'].var())
print(df['Product_B'].var())
print(df['Product_C'].var())
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
# describe() printing by df[[]] as multiple columns together
print("describe() of Product_A, Product_B, Product_C together printing by df[[]]: \n")
print(df[['Product_A', 'Product_B', 'Product_C']].describe())
print("\n\n\n")


### another systemic printing describe
    # Calculate statistics for Product_A
average = df['Product_A'].mean()
std_dev = df['Product_A'].std()
variance = df['Product_A'].var()
median = df['Product_A'].median()
mode = df['Product_A'].mode()
    # Display the results
print(f"Average (Mean) of Product_A: {average}")
print(f"Standard Deviation of Product_A: {std_dev}")
print(f"Variance of Product_A: {variance}")
print(f"Median of Product_A: {median}")
print(f"Mode of Product_A: {mode.tolist()}")
print("\n\n")

### Range Index
print(df.index, "\n")

### set_index()
print(df.set_index('Product_A'), "\n")
print(df.set_index('Product_C', inplace=True), "\n") ## Permanent index setting
print(df.loc[840.0])

### reset_index()
print(df.reset_index(inplace=True)) ## Permanent reset
print(df)
