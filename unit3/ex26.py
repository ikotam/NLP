from ex20 import readData
from ex25 import filterTem

listWiki = readData()
temp = {}

def isInList(s):
    n = len(listWiki)
    for i in range(n):
        if (s == listWiki[i]['title']):
            return i
    return -1


def main():
    temp = filterTem(listWiki)
    for title in temp:
        linebegin = temp[title]
        pos = isInList(title)
        if (pos == -1): continue
        text = listWiki[pos]['text']
        lines = text.split('\n')
        nline = len(lines)
        so = ''
        sc = ''
        for i in range(linebegin,nline):
            if (lines[i] == ']' or lines[i] == '}'):
                sc += lines[i]
            elif (lines[i] == '[' or lines[i] == '{'):
                so += lines[i]
            
                

        


if __name__ == "__main__":
    main()