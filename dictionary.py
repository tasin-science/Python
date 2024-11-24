#dictionary

dict = {
    "dict1" : {"Name": "Alice", "Age":25},
    "dict2" : {"Name": "Bob", "Age":26}
}
print(dict , "\n")
print(dict["dict1"]["Name"])
print(dict["dict1"]["Age"])
print(dict["dict2"]["Name"], ["dict2"]["Age"], "\n")



#printing dictionary in vertical manner
import json
course = {
    "crs1" : {"crs_name":"CSE103", "crs_title":"Basic Programming"},
    "crs2" : {"crs_name":"CSE106", "crs_title":"Discrete Mathematics"},
    "crs3" : {"crs_name":"CSE110", "crs_title":"OOP"},
    "crs4" : {"crs_name":"CSE200", "crs_title":"Autocad"},
    "crs5" : {"crs_name":"CSE207", "crs_title":"Data Structure"},
    "crs6" : {"crs_name":"CSE209", "crs_title":"Electric Circuits"}
}
print(course["crs1"]["crs_name"], course["crs1"]["crs_title"])
print(course)
print("\n")
print(json.dumps(course,indent=9))
#here intend works as tab system.



