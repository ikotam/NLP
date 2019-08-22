from ex20 import readData

s = '{{基礎情報'


def filterTem(listWiki):
    template = {}
    for ele in listWiki:
        text = ele['text']
        lines = text.split('\n')
        n = len(lines)
        for i in range(n):
            line = lines[i]
            if s in line:
                template[ele['title']] = i
    return template



def main():
    listWiki = readData()
    temp = filterTem(listWiki)

    print(temp)



if __name__ == "__main__":
    main()

