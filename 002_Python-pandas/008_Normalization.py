#### Normalization

import pandas as pd

df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n\n")

#Normalize Product A
df['Normalized_Product_A'] = (df['Product_A'] - df['Product_A'].min()) / (df['Product_A'].max() - df['Product_A'].min())
print(df, "\n\n\n")