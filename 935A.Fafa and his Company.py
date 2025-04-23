total_employees = int(input())
initial = 1
ways = 0
while initial < total_employees:
    leaders = total_employees - initial
    if ((total_employees - leaders) % leaders) == 0:
        ways += 1
        initial += 1
    else:
        initial += 1
print(ways)
