import json
import csv

json_list = []

with open('../famineDB/famineDB.csv', 'r') as f:
    for row in csv.DictReader(f):
        json_list.append(row)

with open('../famineDB/famineDB.json', 'w') as f:
    json.dump(json_list, f)

with open('../famineDB/famineDB.json', 'r') as f:
    json_output = json.load(f)
