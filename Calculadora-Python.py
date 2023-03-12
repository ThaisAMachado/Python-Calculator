# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:50:35 2023

@author: Thais.Machado
"""

def calculadora():
    print("\n************* Calculadora Python *************")
    print("\nEscolha uma operação: ")
    print("\n1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Potência")
    while True:
        try:
            operacao = int(input("\nDigite a operação desejada: "))
            if not operacao in (1,2,3,4,5):
                print("\nOperação inválida!")
                continue
        except:
            print("\nSeleção inválida!")
            continue
        else:
            break
    try:
        num1 = int(input("\nDigite o 1º número: "))
    except ValueError:
        print("\nNúmero inválido!")
        return
    try:
        num2 = int(input("\nDigite o 2º número: "))
    except ValueError:
        print("\nNúmero inválido!")
        return
    if operacao == 1:
        resultado = num1+num2
        print("\n", num1, "+", num2, "= ", resultado)
    elif operacao == 2:
        resultado = num1-num2
        print("\n", num1, "-", num2, "= ", resultado)
    elif operacao == 3:
        resultado = num1*num2
        print("\n", num1, "x", num2, "= ", resultado)
    elif operacao == 4:
        resultado = num1/num2
        print("\n", num1, "/", num2, "= ", resultado)
    else:
        resultado = num1**num2
        print("\n", num1, "^", num2, "= ", resultado)

calculadora()
