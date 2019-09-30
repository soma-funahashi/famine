import json
f = open("../famineDB/famineDB.json", "r")
json_dict = json.load(f)

for item in json_dict:
    print(json_dict(item))
