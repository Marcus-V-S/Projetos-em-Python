while True:

    try:

        print("Calculadora Básica")
        print("------------------")
        Valor1 = int(input("Digite o valor 1: "))
        Valor2 = int(input("Digite o valor 2: "))

    except ValueError or NameError:
            print("Erro, digite um numero listado")
            continue
    
    print("Agora escolha o calculo")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")


    while True:
        try:
            Calculo = int(input("Escolha aqui:\n> "))
            if Calculo in [1, 2, 3, 4]:
                    break
            else:
                    print("Digite um numero Listado")
        except ValueError or NameError:
                print ("Seu burro")


    if Calculo == 1:
                    print(f"Resultado da adição: {Valor1 + Valor2}")

    elif Calculo == 2:
                    print(f"Resultado da subtração: {Valor1 - Valor2}")
                
    elif Calculo == 3:
                    print(f"Resultado da multiplicação: {Valor1 * Valor2}")

    elif Calculo == 4:
                    print(f"Resultado da divisão: {Valor1 / Valor2}")
        


