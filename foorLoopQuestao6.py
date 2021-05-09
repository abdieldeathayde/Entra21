Lista1 = [3.14, 66, "Ursinho Carinhoso", True, [], {}]
Lista2 = []

i = 0
for i in range (len(Lista1)):
    Lista2.append(type(Lista1[i]))
print(Lista2)