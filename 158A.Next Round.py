participant, margin_participant = map(int, input().split())
points = str(input())
list_points = points.split()
value = margin_participant - 1
margin_point = int(list_points[value])
i = 0
nxt_round = 0
while i < participant:
    number = int(list_points[i])
    if number >= margin_point and number > 0:
        nxt_round += 1
    i += 1
print(nxt_round)