import sys
from fairseq.data import Dictionary

Dict = Dictionary()

def convertToDict(file): 
    global Dict
    # print(Dict.indices)
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                # print(word)
                Dict.add_symbol(word=word, n=1)

def main():
    files = sys.argv
    del files[0]
    for file in files:
        convertToDict(file)

    with open('dict.txt', 'w', encoding='utf-8') as f:
        Dict.save(f)

if __name__ == "__main__":
    main()