# leia da quantidade de notas
numero_notas = int(input("Digite o numero de notas: "))
# iniciar o contador de notas
contador_recebe = 0
# leia as notas e conte o numero de alunos que recebe
i = 0 # contador de notas lidas
while i < nota:
    nota_final = float(input("Digite uma nota: "))
    if nota_final >= 3 and nota_final <= 5:   # equivalente a 3 <= nota_final <5:
        contador_recebe += 1
    elif nota_final > 10 or nota_final < 0:
        print("Você digitou um numero inválido")
    i += 1
print( contador_recebe, "alunos ficaram de recuperação")