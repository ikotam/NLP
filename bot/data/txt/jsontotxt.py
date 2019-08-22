import json
import sys
from ast import literal_eval
from fairseq.data import Dictionary

def prepare_str(string):
    string = string.lower()
    return string


def convert(file):
    # fi = open(file+'.x', 'w')
    # fo = open(file+'.y', 'w')
    fi = open(file+'txt', 'w')
    with open(file+'.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            dict = literal_eval(line)
            dialogues = dict['dialogue']
            n = len(dialogues)
            for i in range(n):
                fi.write('%s\n' % (prepare_str(dialogues[i]['text'])))
                # fo.write('%s\n' % (prepare_str(dialogues[i+1]['text'])))
            fi.write('\n')
                        
    fi.close()
    # fo.close()

def main():
    files = sys.argv
    del files[0]
#     print(files)
    for file in files:
        convert(file)

if __name__ == "__main__":
    main()
