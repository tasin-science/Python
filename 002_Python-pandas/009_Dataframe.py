#### Dataframe ####

import pandas as pd




### Creating dictionary and show it as dataframe
data = {
    'name' : ['Asif', 'Rahim', 'Rahman'],
    'age' : [14, 15, 13],
    'hobby' : ['Gardening', 'Programming', 'Learning']
}
df = pd.DataFrame(data)
print(df, "\n\n")





### Creating a list of tuples and show it as dataframe
geography = [
    ('United States', 'Washington D.C.', 177.0),
    ('United Kingdom','London', 1572),
    ('Japan','Tokyo', 2194.07),
    ('South Korea','Seoul', 605.21),
    ('Russia','Moscow', 2511),
    ('Turkiye','Ankara', 24521),
    ('China','Beijing', 16410.5)
]

df = pd.DataFrame(geography, columns=['Country', 'Capital', 'Area of Capital (km^2)'])
print(df, "\n\n")






### A bunch of dictionaries
Languages = [
    {'Lang_Name': 'English', 'Country':'United Kingdom', 'Words': 600000},
    {'Lang_Name': 'Arabic', 'Country':'Saudi Arabia', 'Words': 12300000},
    {'Lang_Name': 'Japanese', 'Country':'Japan', 'Words': 500000},
    {'Lang_Name': 'Chinese', 'Country':'China', 'Words': 350000},
    {'Lang_Name': 'Korean', 'Country':'Korea', 'Words': 1100000},
    {'Lang_Name': 'Deutsch', 'Country':'Deutschland', 'Words': 5300000}
]
df = pd.DataFrame(Languages)
print(df)