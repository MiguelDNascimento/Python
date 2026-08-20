import time

saldo = 0
while True:
    print("\n--------------BANCO-----------------")
    op = int(input("1 - Depositar\n2 - Sacar\n3 - Ver saldo\n0 - Sair\nDigite a opção que deseja fazer: "))
    time.sleep(1)

    if op == 1:
        add = float(input("Digite a quantidade que deseja depositar: "))
        saldo += add
        print(f"\nFoi depositado o valor de R${add}\n")
        time.sleep(4)
    elif op == 2:
        sacar = float(input("Digite o valor que deseja sacar: "))
        if sacar > saldo:
            print("Se fizer isso sua conta ficara no vermelho, deseja continuar?")
            time.sleep(5)
            perg2 = input("Digite sua resposta: ").lower()
            if perg2 == "sim":
                saldo -= sacar
                print("\nSaldo sacado com sucesso!, porém, você está devendo")
                print(f"----------------------\nSaldo atual: R${saldo}\n----------------------")
                time.sleep(3)
            elif perg2 == "não" or perg2 == "nao":
                print("Operação cancelada.")
        else:
            saldo -= sacar
            print(f"\nFoi sacado o valor de R${sacar}")
            print(f"----------------------\nSaldo atual: R${saldo}\n----------------------")
            time.sleep(3)
    elif op == 3:
        print(f"\n----------------------\nSeu saldo é de R${saldo}\n----------------------")
        time.sleep(4)
    elif op == 0:
        print("Saindo do banco...")
        time.sleep(1)
        break
    else:
        print("Opção invalida!")
