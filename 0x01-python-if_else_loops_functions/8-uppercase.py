#!/usr/bin/python3
def uppercase(str):
    LN = len(str)
    new_str = ""
    for i in range(LN):
        a = ord(str[i])
        if a >= 97 and a < 123:
            C = chr(a - 32)
            new_str += C
        else:
            new_str += str[i]
    print("{}".format(new_str))
