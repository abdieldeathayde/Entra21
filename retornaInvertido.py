def retornaInvertido(valor):
    return valor[::-1] # [::-1] retorna o valor invertido

numero = input('informe um numero: ')
print(retornaInvertido(numero))

termo = 0
while (termo <= 0):
    termo = int(input("VocÊ que a serie de fibonacci até qual termo: "))
    if(termo <= 0):
        print("O termo deve ser positivo!")

primeiro = 0
print(primeiro)
segunfdo = 1
for i in range(1, termo):
    print(segundo)
    terceiro = primeiro+segundo
    primeiro = segundo
    segundo = terceiro