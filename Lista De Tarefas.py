
Lista = [] 

while True: 

    try:

        if Lista == []:
            print("Lista está Vazia")

        else:
            print("Sua lista de tarefa:")
            for i, tarefa in enumerate(Lista):
                print(f"{i + 1} - {tarefa}")

            print("-----------")
        
        print("1 - Adicionar\n2 - Remover")
        escolha = int(input("Escolha uma opção:\n>"))

        if escolha == 1:
            nova_tarefa = input("Escreva a nova tarefa:\n>")
            item = nova_tarefa
            Lista.append(item)
            continue

        elif escolha == 2:
            if Lista == []:
                print("Não há nada para ser deletado")

            else:
                ndf = int(input("Escolha a tarefa para ser removida: "))
                ndv = ndf - 1
                Lista.pop(ndv)

    except ValueError, NameError:
        print("Você digitou errado!")
        continue