number = int(input())
length = 0
unlucky = 0
total_lucky = 0
if number == 0:
    print("NO")
    exit(0)
if number == 4:
    print("NO")
    exit(0)
if number == 7:
    print("NO")
    exit(0)
while number != 0:
    remainder = (number % 10)
    if remainder == 4:
        total_lucky += 1
    elif remainder == 7:
        total_lucky += 1
    else:
        unlucky += 1
    number = number // 10
    length += 1

if total_lucky == 7:
    print("YES")
elif total_lucky == 4:
    print("YES")
else:
    print("NO")