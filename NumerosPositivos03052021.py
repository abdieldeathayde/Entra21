lista1 = [111, 32, -9, -45, -17, 9, 85, -10]
lista2 = []

i = 0
for i in range (len(lista1)):
    if (lista1[i] >= 0):
        lista2.append(lista1[i])
print(lista2)