txt = str(input())
i = len(txt)
j = 0
a = 0
x = 0
while j < i:
    if txt[j] == "a":
        a += 1
        j += 1
    else:
        x += 1
        j += 1
if x > a:
    print(i - (x - a) - 1)
elif x == a:
    print(i-1)
else:
    print(i)
