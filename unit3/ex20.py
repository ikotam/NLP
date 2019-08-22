from json import loads, load
from ast import literal_eval

data = {}

def readData():
    global data
    str1 = 'イギリス'
    listWiki = []

    with open('jawiki-country.json', 'r', encoding='utf-8') as fi:
        lines = fi.readlines()
        r = 0
        for line in lines:
            r += 1
            a = literal_eval(line)
            data[str(r)] = a

    for stt in data:
        if str1 in data[stt]['text']:
            listWiki.append(data[stt])
    
    # print(data)

    return listWiki

def main():
    readData()
    # print(listWiki[0]['text'])

if __name__ == "__main__":
    main()

