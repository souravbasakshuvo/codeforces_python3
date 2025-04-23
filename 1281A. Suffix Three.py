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
    word = name[i]
    new = word[::-1]
    last_part = new[0:2:1]
    last = last_part[::-1]
    if last == "po":
        print("FILIPINO")
    last_part = new[0:4:1]
    last = last_part[::-1]
    if last == "desu":
        print("JAPANESE")
    last_part = new[0:4:1]
    last = last_part[::-1]
    if last == "masu":
        print("JAPANESE")
    last_part = new[0:5:1]
    last = last_part[::-1]
    if last == "mnida":
        print("KOREAN")
    i += 1