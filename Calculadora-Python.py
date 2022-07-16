def calculadora():
    print("\n************* Calculadora Python *************")
    print("\nEscolha uma operação: ")
    print("\n1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n")
    operacao = int(input("Digite a operação desejada: "))
    if (operacao != 1) and (operacao != 2) and (operacao != 3) and (operacao != 4):
        print("Operação inválida!")
        return
    num1 = int(input("\nDigite o 1º número: "))
    num2 = int(input("\nDigite o 2º número: "))
    if operacao == 1:
        resultado = num1+num2
        print("\n", num1, "+", num2, "= ", resultado)
    elif operacao == 2:
        resultado = num1-num2
        print("\n", num1, "-", num2, "= ", resultado)
    elif operacao == 3:
        resultado = num1*num2
        print("\n", num1, "x", num2, "= ", resultado)
    else:
        resultado = num1/num2
        print("\n", num1, "/", num2, "= ", resultado)

calculadora()
