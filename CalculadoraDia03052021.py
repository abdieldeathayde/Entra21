def calculadora(opcao):
   
    while (opcao != 5):
        
        

        
        a = int(input("Digite o valor 1: "))
        b = int(input("Digite o valor 2:"))
        if (opcao == 1):

            soma = a + b
            print("soma: " + str(soma))

        elif (opcao == 2):

            subtracao = a - b 
            print("Subtracao de {a} por {b} : " + str(subtracao))

        elif (opcao == 3):

            divisao = a / b
            print("Divisão: " + str(divisao))
        
        elif (opcao == 4):
        
            multiplicacao = a * b
            print("Multiplicacao: " + str( multiplicacao ))
        
        else:
        
            print("Digite uma opção do menu")
        calculadora(int(input("Escolha uma opção: \n1 - Somar \n2 - Subtrair \n3 - Dividir \n4 - Multiplicar \n 5 - sair")))
            
calculadora(int(input("Escolha uma opção: \n1 - Somar \n2 - Subtrair \n3 - Dividir \n4 - Multiplicar \n 5 - sair")))



