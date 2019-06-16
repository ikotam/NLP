index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

str1 =  "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dic = {}

words = str1.split(" ")

for i in range(len(words)):
    if i+1 in index:
        str2 = words[i][0:1]
    else:
        str2 = words[i][0:2]
    dic[str2] = i+1
    print(str2)

# for word, index in dic.items():
#     print(word + ': ' + str(index))
