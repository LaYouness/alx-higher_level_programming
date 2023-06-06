#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    new_str = ""
    for i in range(l):
        a = ord(str[i])
        if a >= 97 and a < 123:
            C = chr(a - 32)
            new_str += C
        else:
            new_str += str[i]
    print("{}".format(new_str))
