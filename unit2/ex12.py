# -- coding: utf-8 --

f = open("hightemp.txt", "r")
f1 = open("col1.txt", "w")
f2 = open("col2.txt", "w")

lines = f.readlines()
for line in lines:
    words = line.split()
    print(line)
    # f1.write(words[0])
    f2.write(words[1])


f.close
f1.close
f2.close

    