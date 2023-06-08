
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]))
from add_0 import add as addf
a = 1
b = 2
r = addf(a, b)
print("{} + {} = {}".format(a, b, r))
