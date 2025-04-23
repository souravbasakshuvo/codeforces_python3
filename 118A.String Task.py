name = str(input())
i = 0
name = name.lower()
name = name.replace("a", "")
name = name.replace("e", "")
name = name.replace("i", "")
name = name.replace("o", "")
name = name.replace("u", "")
name = name.replace("y", "")
number = len(name)

while number>0 :
    print (("."+(name[i])), end='')
    number -= 1
    i = i+1