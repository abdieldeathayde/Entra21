def divisao(x, y):
    try:
        print(f'{x}/{y} is { x / y}') 
    except ZeroDivisionError as e:
        print(e)
    else:
        print("divisao() function worked fine.")

divisao(10, 2)
divisao(10, 0)
divisao(10, 4) 
"""
# x = 'arvore'
# print(x[0])

x = ['porco', 'ovelha', 'cavalo']
y = ('porco', 'ovelha', 'cavalo') #tupla
z = 'paralelepipedo'
print(x[1])

print(z[1:4:2]) #slicing
print(z[:-2])

print(z[:5])
print(z.count) #mostra o local da variavel na memoria

lista = ['bug', 'teste', 'terceiroObjeto']
print(sorted(lista))

listaNomes = ['robert', 'john', 'neusa', 'joana','raimunda','nonato']
print(sorted(lista))
print (sorted(listaNomes, key=lambda k: k[1])) #sorteia pela letra do indice


ferramentas = 'alicate'
print(ferramentas.count('i')) #mostra a quantidade de um elemento na lista
#  muito usado para regras de negocios

    
ferramentas = ['alicate', 'chave', 'trena']
print(ferramentas.count('chave'))


empacotandoLista = ['al','ox', 'buz', 'xis']
a, b, c, d = empacotandoLista #unpackage nessa linha esta desempacotando os itens dentro de cada variavel
print(a, b, c, d) 


a = [ m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)


 a = [5, 3, 8, 6]

 a.insert(1, 7)
 print(a)
 a.insert(1, ['a', 'u'])
 print(a)

 b = [9, 10, 15]
 a.extend(b)
print.asc(a) verificar numero ascendente
del(a[1])
a.append(7)
print(a)

 a = [5,3,8,6]
 a.pop()
 print(a)
 print(a.pop()) # mostra ultimo item que foi eliminado

a = [5,3,8,6]
a.remove(3) #especifica o nome do item a ser removido
#remove() remove a primeira instancia de um item
a.reverse()
print(a)


y = ([1, 2, 3], 3)
del(y[0][2])
print(y)



x = {5, 3, 4, 9, 5, 4} #set
print(x)
x.add(12)
x.remove (3) #exatamente o que a gente remove
print(x)
print(5 in x)
"""

x = [5, 3, 4, 9, 5, 4]
for i in x [:]:
    if i < 6:    
        x.remove(i)
    print(x)