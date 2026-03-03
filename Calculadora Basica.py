while True:

    print("Calculadora Básica")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    Calculo = input("Escolha aqui: ")
    if Calculo not in ["1", "2", "3", "4"]:
           print("Erro... Reiniciando")
           continue
    

    number1 = int(input("Digite o valor aqui: "))
    number2 = int(input("Digite o valor aqui: "))

    if Calculo == "1":
        print(f"Resultado: {number1 + number2}")
        
    elif Calculo == "2":
        print(f"Resultado: {number1 - number2}")

    elif Calculo == "3":
                print(f"Resultado: {number1 * number2}")

    elif Calculo == "4":
                if number2 != 0:
                       print(f"Resultado: {number1 / number2}")
                else:
                       print("Erro... Não existe divisão por 0 BURRO")