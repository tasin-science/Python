#### pandas

import pandas as pd

### creating a simple series
data = pd.Series([1,2,3,4,5])
print(data)

print("\n\n")

### Creating a dataframe from dictionary
source = {
    'Name' : ['Tasin', 'Rafiq', 'Alam'],
    'Age' : [22,22,23],
    'Score' : ['A+', 'A', 'A-']
}
df = pd.DataFrame(source)
print(df)
print(type(df))

print("\n\n")


### Reading a Spreadsheet file
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n")




### Show Rows and Columns
rows, columns = df.shape
print("Rows are: ", rows, "\nColumns are: ", columns)

print("\n\n")


### head() and tail() method
print(df.head(), "\n\n") ## head() method
print(df.head(10), "\n\n") ## first 10 rows
print(df.tail(), "\n\n") ## tail() method
print(df.tail(10), "\n\n") ## last 10 rows





