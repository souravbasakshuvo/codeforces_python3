i = int(input())
t = str(input())
j = 0
fs = 0
sf = 0
while j < (i-1):
    a = t[j]
    b = t[j + 1]
    txt = ""+a+b
    if txt == "FS":
        fs += 1
        j += 1
    elif txt == "SF":
        sf += 1
        j += 1
    else:
        j += 1
if sf > fs:
    print("YES")
else:
    print("NO")
