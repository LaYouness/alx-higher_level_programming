#!/usr/bin/python3
for a in range(97, 123):
    c = chr(a)
    if c == 'q' or c == 'e':
        continue
    print("{}".format(c), end='')
