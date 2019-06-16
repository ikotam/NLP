import string

cnt = []
for i in range(200):
    cnt.append(0)

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

words = str.split(" ")

for word in words:
    for i in word: 
        if i.isalpha():
            cnt[(ord(i)-65)%32] += 1
            
    print(word + ': ')
    for i in range(200):
        if cnt[i] != 0: 
            print(chr(i+97)),
            print(cnt[i])
            cnt[i] = 0

        
