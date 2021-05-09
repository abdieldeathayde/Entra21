def calculaMedia():
    
    n = 2
    
    i = 0
    alunosEmRecuperacao = 0

    while (n != 0):
        for i in range(n):
            print("digite a nota " + str(i))
            media = int(input())
            if (media >= 3 and media <= 5):
                print("Você está em recuperação")
                alunosEmRecuperacao += 1
            elif (media < 3 and media >= 0):
                print("Você está reprovado")

            elif (media >  5 and media <= 10):
                print("Você está aprovado")

            else:
                print("insira uma nota menor que 10 e maior que 0")
        print(str(alunosEmRecuperacao) + " Alunos ficaram em recuperação")
        print("Digite a quantidade de notas: ")
        n = int(input())
calculaMedia()