#Lista de tarefas onde pode-se adicionar e remover uma tarefa.
Lista = [] # Abre uma lista chamada "Lista" por enquanto vazia

while True: # Cria um loop

    try:

        if Lista == []:  # se a Lista estiver vazia
            print("Lista está Vazia")   # print("Lista está Vazia")

        else:
            print("Sua lista de tarefa:")
            for i, tarefa in enumerate(Lista): # para cada item, enumere uma palavra, em sequencia, dentro de lista
                print(f"{i + 1} - {tarefa}") # print item + 1 (para não começar a partir de 0) - {tarefa}(mostra a tarefa escrita na posição atual do item)

            print("-----------")

        print("1 - Adicionar\n2 - Remover") # o \n desce uma linha
        escolha = int(input("Escolha uma opção:\n>"))

        if escolha == 1: # se a escolha em "escolha" for 1
            Lista.append(input("Escreva a nova tarefa:\n>"))   # adiciona um novo item a frente, dentro da lista, escrito no "input"
            continue #Reinicia o while

        elif escolha == 2: # se a escolha em "escolha" for 2
            if Lista == []: # e se caso lista estiver vazia
                print("Não há nada para ser deletado") 

            else: # caso contrário
                Lista.pop((int(input("Escolha a tarefa para ser removida: "))) - 1) # Definimos o "input" como inteiro e o valor retornado por lee sera subtraido por 1
                # "Lista.pop" serve para remover o valor do item selecionado dentro de Lista

    except ValueError, NameError: # caso o programa encontre um erro de valor ou nome(usuario digitou algo indevido em um campo)
        print("Você digitou errado!")
        continue # Reinicia o while