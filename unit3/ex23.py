from ex20 import readData

listWiki = readData()
level = [0] * 100

def main():
    for ele in listWiki:
        text = ele['text']
        lines = text.splitlines()
        for line in lines:
            indexl = line.find('==')
            indexr = line.rfind('==')
            if (indexl != -1 ):
                str1 = line[indexl:indexr+2]
                cnt = 0
                section = ''
                for char in str1:
                    if char == '=': cnt += 1
                    if char.isalpha() == True: section += char
                lv = int(cnt/2 - 1)
                level[lv] += 1
                for i in range(lv+1, 100):
                    level[i] = 0
                print(('\t'*(lv-1)), end = '')
                for i in range(1,lv+1):
                    print(str(level[i]) + '.', end = '')
                print(' ' + section)

if __name__ == "__main__":
    main()