from ex21 import getCategory

def main():
    listCate = getCategory()

    r = 1
    for stt in listCate:
        print('%d: ' %(r))
        for  cateName in stt:
            print('%s' % (cateName))
        r += 1

if __name__ == "__main__":
    main()

