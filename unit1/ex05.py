
def calc_n_gram_word_level(n, str):
    str = str.lower()
    words = str.split(" ")
    str_res = []
    for i in range(len(words)-n+1):
        str1 = words[i]
        for j in range(i+1,i+n):
            str1 += ' ' + words[j]
        str_res.append(str1)
    return str_res

def calc_n_gram_char_level(n, str):
    str = str.lower()
    str_res = []
    for i in range(len(str)-n+1):
        str1 = str[i:i+n]
        str1 = str1.replace(' ', '#')
        str_res.append(str1)

    return str_res


# print(calc_n_gram_word_level(2, "I am an NLPer"))
# print(calc_n_gram_char_level(2, "I am an NLPer"))
