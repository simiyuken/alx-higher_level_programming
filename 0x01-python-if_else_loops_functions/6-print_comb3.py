#!/usr/bin/python3
for s in range(0, 10):
    for k in range(s + 1, 10):
        if (not (s == 8 and k == 9)):
            print("{}{}".format(s, k), end=", ")
        else:
            print("{}{}".format(s, k))
