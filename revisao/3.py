import time
lista = []

while True:
    opcao = int(input("\n1 - Adicionar nome\n2 - Mostrar nomes\n3 - Remover nome\n0 - Sair\nEscolha uma opção: "))
    if opcao == 1:
        nome = input("Adicione um nome: ")
        lista.append(nome)
        print("Nome adicionado com sucesso!\n")
    elif opcao == 2:
        print("\n------------NOMES--------------")
        for i, user in enumerate(lista):
            print(f"{i + 1} - {user}")
    elif opcao == 3:
            if len(lista) == 0:
                print("Nenhum nome cadastrado!")
            else:
                for i, user in enumerate(lista, start=1):
                    print(f"{i} - {user}")

                remov = int(input("Qual usuário deseja remover? "))

                if 1 <= remov <= len(lista):
                    lista.pop(remov - 1)
                    print("Nome removido com sucesso!")
                else:
                    print("Número inválido!")
    elif opcao == 0:
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Escolha uma opção válida!")