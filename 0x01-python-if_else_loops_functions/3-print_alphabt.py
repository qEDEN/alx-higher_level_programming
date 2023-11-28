#!/usr/bin/python3
for i in range(97, 123):
    if i not in [101, 113]:  # ASCII values for 'e' and 'q'
        print("{}".format(chr(i)), end="")
