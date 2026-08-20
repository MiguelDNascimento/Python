import time
lista = []

while True:
    opcao = int(input("\n1 - Adicionar produto\n2 - Listar produtos\n0 - Sair\nEscolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        lista.append(nome)
        print("Produto adicionado com sucesso!\n")

    elif opcao == 2:
        if len(lista) == 0:
            print("Nenhum produto cadastrado!")

        else:
            print("\n------------PRODUTOS--------------")
            for i, produto in enumerate(lista, start=1):
                print(f"{i} - {produto}")

    elif opcao == 0:
        print("Saindo do programa...")
        time.sleep(1)
        break

    else:
        print("Escolha uma opção válida!")


