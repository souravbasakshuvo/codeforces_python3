i, j, k, l = map(int, input().split())
if (i + j + k) == 2*l:
    a_b_c = l
    a = a_b_c - i
    b = a_b_c - j
    c = a_b_c - k
    print(a, b, c)
elif (i + j + l) == 2*k:
    a_b_c = k
    a = a_b_c - i
    b = a_b_c - j
    c = a_b_c - l
    print(a, b, c)
elif (i + l + k) == 2*j:
    a_b_c = j
    a = a_b_c - i
    b = a_b_c - l
    c = a_b_c - k
    print(a, b, c)
elif (l + j + k) == 2*i:
    a_b_c = i
    a = a_b_c - l
    b = a_b_c - j
    c = a_b_c - k
    print(a, b, c)
