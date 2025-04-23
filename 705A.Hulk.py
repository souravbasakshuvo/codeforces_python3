term = int(input())
i = 1
while i <= term:
    if i == 1:
        print("I hate", end=" ")
    elif (i % 2) == 0:
        print("that I love", end=" ")
    elif (i % 2) == 1:
        print("that I hate", end=" ")
    i = i +1
print("it")
