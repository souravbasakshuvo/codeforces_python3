n, m, a = map(int, input().split())
i = n // a
j = m // a
if (float(n % a)) > 0:
    i = i + 1
if (float(m % a)) > 0:
    j = j + 1
x = i * j
print(x)
