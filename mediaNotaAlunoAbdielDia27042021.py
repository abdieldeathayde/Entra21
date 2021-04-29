import os

opcao = 's'

while(opcao == 's' or opcao == 'S'):
    
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: \n"))
    nota3 = float(input("Digite a terceira nota: \n"))
    nota4 = float(input("Digite a quarta nota: \n"))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if (media >= 7):
      print("Aprovado")
    elif (media >= 6 and media < 7):
      print("Recuperação")
    else:
      print("Reprovado")
    opcao = str(input("Deseja continuar? S/n"))
    os.system('cls' if os.name == 'nt' else 'clear')

   
