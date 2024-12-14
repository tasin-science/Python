#### Group by function

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n\n")

### Group by year and calculate the average of 'Product A'
print("Calculate the averages of Product A according years")
print(df.groupby('Year')['Product_A'].mean(), "\n\n\n")

### Group by year and calculate the average of 'Product A', 'Product B' and 'Product C'
print("Calculate the averages of Product A, 'Product B' and 'Product C' according years")
print(df.groupby('Year')[['Product_A', 'Product_B', 'Product_C']].mean(), "\n\n\n")

dictionary = {
    'Product_A' : df['Product_A'].mean(),
    'Product_B' : df['Product_B'].mean(),
    'Product_C' : df['Product_C'].mean()
}
print(dictionary)