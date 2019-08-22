from ex20 import readData

def getCategory():
    listWiki = readData()
    listCate = []
    for ele in listWiki:
        text = ele['text']
        lines = text.splitlines()
        List = []
        for line in lines:
            # print('[[Category:' in line)
            if (('[[Category:' in line) == True):
                if (('|*' in line) == True):
                    List.append(line[11:-4])
                else:
                    List.append(line[11:-2])
        listCate.append(List)

    return listCate



def main():
    listCate = getCategory()
    r = 0
    for ele in listWiki:
        text = ele['text']
        lines = text.splitlines()
        for line in lines:
            if any(cate in line for cate in listCate[r]):
                print(line)
        r += 1
        print('\n')
            

if __name__ == '__main__':
    main()
    
