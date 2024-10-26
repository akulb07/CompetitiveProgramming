n = int(input(""))
l = []
f = []
if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(i)
        else:
            f.append(i)

    l = l + f
    x = " ".join(map(str, l))
    print(x)