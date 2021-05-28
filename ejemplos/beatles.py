# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
while True:
    validos = ['Stu Sutcliffe', 'Pete Best']

    tmp = input("introduce 'Stu Sutcliffe' o 'Pete Best': ")

    if tmp not in validos:
        print("'" + tmp + "' no es ninguno de ", validos)
        continue

    if tmp in beatles:
        print(tmp, "ya estaba dentro de la lista")
        continue

    beatles.append(tmp)

    if validos[0] in beatles and validos[1] in beatles:
        break

print("Step 3:", beatles)

# step 4
for _borrado in ['Stu Sutcliffe', 'Pete Best']:
    del(beatles[beatles.index(_borrado)])
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))
