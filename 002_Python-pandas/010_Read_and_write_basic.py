#### Read and write basic ###

import pandas as pd




### Read csv file
df = pd.read_csv("Datasheet/Countries.csv")
print("Printed csv: \n" ,df, "\n\n")

## skiprows argument
dfs = pd.read_csv("Datasheet/Countries.csv", skiprows=1) #first row is heading, and heading will be skipped
print("Header is skipped and \'United States\' part becomes header: \n" , dfs, "\n\n")

## headingless problem solution
print("This csv file has no header and \'United States\' part is header: \n" , pd.read_csv("Datasheet/Countries2.csv"), "\n\n") # Here first row 'United States' shows heading
dfn = pd.read_csv("Datasheet/Countries2.csv", header=None) # for fixing this problem
print("header=None fixed this problem as: \n", dfn, "\n\n")
# in dfn, it shows headers as 0 1 2.
# so if we use 'names' argument, it will create header
dfb = pd.read_csv("Datasheet/Countries2.csv", header=None, names=['COUNTRIES', 'CAPITALS', 'LANGUAGES'])
print("Using \'names\' parameter: \n", dfb, "\n\n")


## nrows argument
# when we want to execute only 0~n-1 rows, then we use nrows=n
df = pd.read_csv("Datasheet/Countries.csv", nrows=3)
print("Printing 0~2 rows: \n", df, "\n\n")

## na_values argument
print("This data shows not availiable in different: \n", pd.read_csv("Datasheet/Countries3.csv"), "\n\n")
df = pd.read_csv("Datasheet/Countries3.csv", na_values={
    'Capital' : ["Not Availiable", "n.a.", "N.a."],
    'Language' : ["Not Availiable", "n.a.", "N.a."]
})
print("After fixing different types of \'Not Availiable\': \n", df, "\n\n") 
# this won't work in terminal, rather this will work in jupyter





### Write csv file
dfl = pd.read_csv("Datasheet/Countries2.csv", header=None, names=['Ctrs', 'Cptls', 'langs'])
dfl.to_csv("Datasheet/Countries2_a.csv")
## for removing index in csv file 
dfl.to_csv("Datasheet/Countries2_b.csv", index=False)
## for showing some specific columns
dfl.to_csv("Datasheet/Countries2_c.csv", index=False, columns=['Ctrs', 'Cptls'])



### Mistake handling
# Bangladesh's capital is given as Jahangirnagar, this is a mistake. 
# Now we want to fix this 
def mistake_handling(cell):
    if cell == 'Jahangirnagar':
        return 'Dhaka'
    return cell
df = pd.read_csv("Datasheet/Countries.csv", converters= {
    'Capital' : mistake_handling
})
print("Jahangirnagar changed as Dhaka: \n", df, "\n\n")




### Read excel file
# For reading excel file, use df.read_excel("<filename>.xlsx", "<sheetname>")



### Writing excel file
# For writing excel file, use df.to_excel("<filename>.xlsx", sheet_name="<sheetname>")
## startrow and startcol argument (works in excel, not csv)
# df.to_excel("<filename>.xlsx", sheet_name="<sheetname>", startrow=1, startcol=2)
