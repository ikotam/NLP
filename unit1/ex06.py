
def union(X, Y):
    List = []
    for ele in X:
        if ele not in List: List.append(ele)
    for ele in Y:
        if ele not in List: List.append(ele)

    return List


def intersection(X, Y):
    List = []
    for ele in X:
        if (ele in X) and (ele in Y) and (ele not in List):
            List.append(ele)
    return List


def difference(X, Y):
    List = []
    for ele in X:
        if (ele in X) and (ele not in Y) and (ele not in List):
            List.append(ele)
    return List

str1 = "paraparaparadise"
str2 = "paragraph"
from ex05 import calc_n_gram_char_level
X = calc_n_gram_char_level(2, str1)
Y = calc_n_gram_char_level(2, str2)

print(X)
print(Y)
print(union(X, Y))
print(intersection(X, Y))
print(difference(X, Y))
print(difference(Y, X))



