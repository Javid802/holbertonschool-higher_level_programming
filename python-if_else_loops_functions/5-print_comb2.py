#!usr/bin/python3
for i in range(99):
    if len(str(i))==1:
        i = "0" + str(i)
    print("{}".format(i), end=", ")
print("99")
