terms = int(input())
l = []
i = 0
while i < terms:
    a, b, c, d, k = map(int, input().split())
    x = a // c
    y = b // d
    if (a % c) != 0:
        x = x + 1
    if (b % d) != 0:
        y = y + 1
    if (x+y) <= k:
        t = "" + str(x) + " " + str(y)
        l.append(t)
        i += 1
    else:
        l.append("-1")
        i += 1
i = 0
while i < terms:
    pen_pencils = l[i]
    print(pen_pencils)
    i += 1
