i = int(input())
j = 0
faces = 0
while j < i:
    k = str(input())
    if k == "Tetrahedron":
        faces = faces + 4
        j += 1
    elif k == "Cube":
        faces = faces + 6
        j += 1
    elif k == "Octahedron":
        faces = faces + 8
        j += 1
    elif k == "Dodecahedron":
        faces = faces + 12
        j += 1
    elif k == "Icosahedron":
        faces = faces + 20
        j += 1
print(faces)
