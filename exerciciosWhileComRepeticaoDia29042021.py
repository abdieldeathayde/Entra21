import math
"""
def verificaNumeroPrimo(numero):
    
    if (numero % 1 == 0 and numero % numero == 0 and numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero != 1):
        print("Primo")
    else:
        print("Não primo")
#verificaNumeroPrimo(15)
"""

def primo(n):
    if (n == 2 or (n!= 1 and n % 2 == 1)):
        é_primo = True
    else:
        é_primo = False
    divisão = 3
    while (divisão < n // 2 and é_primo):
        if (n % divisão == 0):
            é_primo = False
        divisão += 2
    if (é_primo):
        print("Primo");        
    else:
        print("Não primo");
primo(int(input("digite um numero: ")))
"""
def verificaDigito():
    #verificador de numeros adjacentes iguais
    numero = int(input("Digite um valor inteiro: "))
    if (numero >= 10 and numero < 100):
        digito1 = numero // 10
        digito2 = numero % 10

        if (digito1 == digito2):
            print("Sim")
        else:
            print("Não")
        
    elif (numero >= 100 and numero < 1000):
        while(numero > 0):
            digito = numero % 10
            digito2 = int(numero // 10)
            digito3 = numero//100

        print(str(digito) + " " + str(digito2) + str(digito3))


    else:
        print("não")    
verificaDigito()    
"""

def verificadorDeNumerosIdenticos():
    numero_salvo = n = int(input("Digite um numero: "))

    anterior = n % 10
    n = n // 10
    adjacente_iguais = False
    posterior = 0

    while (n > 0 and not adjacente_iguais):
        atual = n % 10
        if (atual == anterior):
            adjacente_iguais = True
        else:
            posterior += 1
        anterior = atual
        n = n // 10

    if adjacente_iguais:
        print("Sim")
    else:
        print("Não")
verificadorDeNumerosIdenticos() 


    