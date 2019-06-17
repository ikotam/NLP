

f = open("hightemp.txt", "r")
f1 = open("col1.txt", "w")
f2 = open("col2.txt", "w")

lines = f.readlines()
for line in lines:
    words = line.split()
    # print(line)
    f1.write(words[0] + '\n')
    f2.write(words[1] + '\n')


f.close
f1.close
f2.close

# command:
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
    