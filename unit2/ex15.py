n = input("enter N")
n = int(n, 10)

fi = open('hightemp.txt', 'r')
lines = fi.readlines()

for i in range(max(24-n, 0), 24):
    print(lines[i])