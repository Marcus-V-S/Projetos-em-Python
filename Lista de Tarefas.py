Tarefa = [ ]


while True:


    enumerate(Tarefa, 1)

    print("<LISTA DE TAREFAS>")
    print (" ")

    for indice, item in enumerate(Tarefa, 1):
        print(f"{indice} - {item}")

    if not Tarefa: 
       print("(Lista Vazia)")
       print(" ")


    print(" --------------------------------------------- ")
    print("A - Adicionar, B - Remover")
    Escolha = (input("Escolha uma opção: "))

    if Escolha == "A":
        novo_item = input("Adicione a tarefa: ")
        Tarefa.append(novo_item)

    elif Escolha == "B":

        if not Tarefa:
            print("[A lista está vazia]")
            continue

        remover_tarefa = int(input("Escolha o número da tarefa a ser removida: "))
        if 1 <= remover_tarefa <= len(Tarefa):
            removido = Tarefa.pop(remover_tarefa - 1)
            print(f"Tarefa '{removido}' foi removida com sucesso")

        else:
            print("Número não está listado")
    
    else:
        print("Opção invalida")
        continue
