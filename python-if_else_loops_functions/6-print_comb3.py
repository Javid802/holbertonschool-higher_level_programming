#!/usr/bin/python3
siyahi = []
for i in range(99):
    i = str(i)
    if len(str(i)) == 1:
        i = "0" + str(i)
    siyahi.append(i)
    
    if i[::-1] not in siyahi:
        print("{}".format(i), end=", ")
