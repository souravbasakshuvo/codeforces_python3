s, v1, v2, t1, t2 = map(int, input().split())
p1 = (s * v1) + (t1 * 2)
p2 = (s * v2) + (t2 * 2)
if p1 < p2:
    print("First")
elif p1 > p2:
    print("Second")
elif p1 == p2:
    print("Friendship")
