import random

def getnum(v):
        n = len(v)
        index = random.randint(0, n-1)
        num = v[index]
        v[index], v[n-1] = v[n-1], v[index]
        v.pop()
        return num

def generateRandom(l, r, word):
        Str = ''
        v = []
        for num in range(l, r+1):
                v.append(num)
        while (len(v)): 
                Str += word[getnum(v)]
        return Str

def typo(str1):
        Str = ''
        words = str1.split(" ")
        for word in words:
                n = len(word)
                if n < 4: 
                        Str += word + ' '
                        continue
                tmp = generateRandom(1, n-2, word)
                word = word.replace(word[1:n-1], tmp)
                Str += word + ' '
        return Str
        

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
print(typo(str1))