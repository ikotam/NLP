import json
import sys
import codecs

data = {}
stringdata = ""

with open('jawiki-country.json', 'r') as f:
    for line in f:
        stringdata += str(json.loads(line.encode('utf-8','replace')))


# data = eval(stringdata)

# print(type(data))