# Painel de tarefas
lista = []

while True:
    print("\n1 - Adicionar tarefa\n2 - listar tarefa\n3 - Remover tarefa\n0 - Sair")
    opcao = input("Digite a opção desejada:\n")

    if opcao == "1":
        add = input("Digite o nome da tarefa\n")
        lista.append(add)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        print("Tarefas:\n")
        for i in lista:
            print("-", i)
    elif opcao == "3":
        numero = int(input("Digite o número da tarefa que deseja remover\n"))
        lista.pop(numero - 1)
        print("Tarefa removida com sucesso!")
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opçao invalida!")