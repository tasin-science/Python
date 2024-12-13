#### Conditional Statement in Pandas

# Note: For conditional statement, it is better to use df['<column_name>'], not df[['<column_name>']]

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n")

### Using Conditional Operation
print(df[df['Product_A']>= 1800], "\n\n")
print(df[df['Product_C']< 1100], "\n\n")

#Finding row of maximum / minimum boolean
print(df["Product_C"] == df["Product_C"].max(), "\n")
print(df["Product_A"] == df["Product_A"].max(), "\n")
