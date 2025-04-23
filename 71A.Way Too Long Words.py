term = int(input())
i = 0
name = []
while i < term:
    name.append(input())
    i += 1
i = 0
while i < term:
    word = str(name[i])
    length = len(name[i])
    if length <= 10:
        print(word)
        i += 1
        continue
    first_letter = word[0]
    last_letter = word[length - 1]
    length = len(name[i])
    output = first_letter+str((length-2))+last_letter
    print(output)
    i += 1