
n = input("enter N")
n = int(n, 10)

fi = open('hightemp.txt', 'r')
lines = fi.readlines()

for i in range(min(24, n)):
    print(lines[i])

# command:
# head -n [numberofline] hightemp.txt