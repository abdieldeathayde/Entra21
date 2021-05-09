def parOuImpar():
    numero = int(input("Digite algum numero: "))
    
    if (numero % 2 == 0):
        print("Par")
    elif (numero %2 != 0):
        print("Impar")
parOuImpar()

def fizzBuz():
    numero = int(input("Digite um numero"))

    if (numero % 3 == 0):
        print("Fizz")
    else:
        print(numero)
fizzBuz()

def fizBuzzParte2():
    numero = int(input("digite um numero: "))
    if (numero % 5 == 0):
        print("Buzz")
    else:
        print(numero)
fizBuzzParte2()

def fizBuzzParte3():
    numero = int(input("digite um numero"))
    if (numero % 3 == 0 and numero % 5 == 0):
        print("FizzBuzz")
    else:
        print(numero)
fizBuzzParte3()

def verificandoOrdenacao():
    numero1 = int(input("Digite o numero 1"))
    numero2 = int(input("Digite o numero 2"))
    numero3 = int(input("Digite o numero 3"))

    if(numero1 < numero2 and numero2 < numero3 ):
        print("Crescente")
    else:
        print("Não está em ordem crescente")
verificandoOrdenacao()

def ordemCrescente():
    variavel = int(input("digite um valor"))
    if (variavel == 200):
        print ("1 - peguei uma expressão de valor True")
        print (variavel)
    elif variavel == 150:
        print("2 - oeguei uma expressão de valor True")
        print(variavel)
    elif variavel == 100:
        print("3 - peguei uma expressão de valor True")
        print(variavel)
    else:
        print("4 - peguei uma expressãod de valor False")
        print(variavel)
    print("Goodbye")
ordemCrescente()