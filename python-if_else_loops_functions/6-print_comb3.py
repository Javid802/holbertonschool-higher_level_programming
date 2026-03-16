#!/usr/bin/python3
for i in range(89):
    i = str(i)
    if len(str(i)) == 1:
        i = "0" + str(i)
    
    if i[::-1] > i:
        print("{}".format(i), end=", ")
print("89")
