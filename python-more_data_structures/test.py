a = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
for i in sorted(a):
    soz = i
    key = a.get(i)
    print("{}: {}".format(soz,key))