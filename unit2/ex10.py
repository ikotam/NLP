def countLine(file):
    num_lines = sum(1 for line in open(file))
    return num_lines

print(countLine('hightemp.txt'))

# command line:
# wc -l hightemp.txt