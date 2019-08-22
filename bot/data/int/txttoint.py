from fairseq.data import Dictionary
import sys

filedict = ''

def convertToInt(filedict, file):
    Dict = Dictionary.load(filedict)
    idx = Dict.indices
    fi = open(file+'.int', 'w')
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            # print(line)
            for word in words:
                fi.write('%d ' % (idx[word]))
            fi.write('\n')
    fi.close()

def main():
    files = sys.argv
    filedict = files[1]
    del files[0]
    del files[0]
    # print(files)
    for file in files:
        convertToInt(filedict, file)

if __name__ == "__main__":
    main()