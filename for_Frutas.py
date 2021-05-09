"""
frutas_exoticas = ["jabuticaba", "Cupuaçu", "graviola", "melancia", "laranja", "pindamonhangaba"]

for i in range(len(frutas_exoticas)):
    print(i+1, frutas_exoticas[i])
"""

inicial = int(input('Informe o valor inicial')) #raw input consegue ver um padrão de dados brutos que o usuário digita
final = inicial

while (final <= inicial):
    final = int(input('Informe o valor final: '))
    if (final <= inicial):
        print('O valor final deve ser maior que o valor inicial! ')


for i in range(inicial, final + 1):
    print(i)