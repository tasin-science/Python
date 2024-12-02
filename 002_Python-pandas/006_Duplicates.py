### Duplicates
import pandas as pd
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n")

print(df.duplicated(), "\n\n")
df = df.drop_duplicates()
print(df)

