# def repetir_palavra(parte1, parte2):
#     print_twice = 'ing'
#     palavra = str(parte1) + str(parte2)
#     print_twice(palavra)

# repetir_palavra('ast','bin')

def repetir_palavra(edu):
    print(edu)
    print(edu)
    print(edu)

#repetir_palavra("uwe") #padronizar usando aspas simples ou dupla
#repetir_palavra(2.30)

def calcular_pagamento(qtd_horas, valor_hora):
    horas = float (qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas*taxa
    else:
        horas_excedidas = horas - 40
        salario = 40*taxa+(horas_excedidas*(1.5*taxa))
    return salario    

calcular_pagamento(40,20)

str_horas = input("Digite as horas: ")
str_taxa = input("Digite a taxa")
total_salario = calcular_pagamento(str_horas, str_taxa)
print("O valor de seus rendimentos é: R$ ", total_salario)
