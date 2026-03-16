a = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in range(99):
    b = i % 16
    c = i // 16
    if c > 0:
        print(f"{i} = 0x{c}{a[b]}")
        continue
    print(f"{i} = 0x{a[b]}")
    