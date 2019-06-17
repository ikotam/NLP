
fi1 = open('col1.txt', 'r')
lines1 = fi1.readlines()

fi2 = open('col2.txt', 'r')
lines2 = fi2.readlines()

fo = open('col12.txt', 'w')
for i in range(24):
    fo.write(lines1[i].rstrip() + '\t' + lines2[i] + '\n') 

fi1.close
fi2.close
fo.close

# command:
# paste col1.txt col2.txt > col12.txt
