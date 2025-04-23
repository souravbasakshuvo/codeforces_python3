x = str(input())
rank = x[0]
suit = x[1]
y = str(input())
l = len(y)
i = 0
while i < l:
    if rank == y[i] or suit == y[i]:
        print("YES")
        exit(0)
    else:
        i = i + 1
print("NO")
