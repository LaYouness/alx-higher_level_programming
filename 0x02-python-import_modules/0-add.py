
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]))
from add_0 import add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
