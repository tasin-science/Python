#### Removing Outliers

import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n")

Q1 = df['Product_A'].quantile(0.25)
Q3 = df['Product_A'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
df = df[(df['Product_A'] >= lower_bound) & (df['Product_A'] <= upper_bound)]
print(df['Product_A'])
