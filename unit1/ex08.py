def cipher(str1):
    Str = str1
    for char in Str:
        if char.islower(): 
            Str = Str.replace(char, chr(219), 1)
    return Str

