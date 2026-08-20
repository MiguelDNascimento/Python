while True:
    print("------------CALCULADORA-------------")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    opr = input("Digite o operador: ")
    if opr == "+":
        result = num1 + num2
        print(result)
    elif opr == "-":
        result = num1 - num2
        print(result)
    elif opr == "*":
        result = num1 * num2
        print(result)
    elif opr == "/":
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            result = num1 / num2
            print(result)
    elif opr == "^":
        result = num1 ** num2
        print(result)
    elif opr == "%":
        result = num1 % num2
        print(result)
    else:
        print("Digite um operador valido!")

    perg = int(input("Deseja continuar?\n1 - Continuar\n2 - Sair\n"))
    if perg == 2:
            break