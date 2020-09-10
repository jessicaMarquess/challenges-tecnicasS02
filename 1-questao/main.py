from numberscomplex import *
import time
import os


while True:
    print("__________________________________\nCalculadora de Números Complexos \n")
    print("__________________________________\nEscolha o primeiro numero complexo\n__________________________________")
    # Lendo os números para serem calculados:
    x = int(input("Digite o número real: "))
    y = int(input("Digite o número imaginário: "))
    c1 = Complex(x, y)
    print("__________________________________\nEscolha o segundo numero complexo\n__________________________________")
    a = int(input("Digite o número real: "))
    b = int(input("Digite o número imaginário: "))
    c2 = Complex(a, b)
    print("__________________________________")
    c1.displayComplexNumber()
    c2.displayComplexNumber()
    # Menu para escolha da operação: 
    way = input("Selecione uma das opções abaixo: \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Comparação\n")
    if way == "1":
        c1.sum(c2)
        print("Concluido... aguarde.")
        time.sleep(3)
        choice = input("----------------------------------\nDeseja fazer mais alguma operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(choice)
    elif way == "2":
        c1.subtract(c2)
        print("Concluido... aguarde.")
        time.sleep(3)
        choice = input("----------------------------------\nDeseja fazer mais alguma operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(choice)
    elif way == "3":
        c1.multiplication(c2)
        print("Concluido... aguarde.")
        time.sleep(3)
        choice = input("----------------------------------\nDeseja fazer mais alguma operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(choice)
    elif way == "4":
        c1.division(c2)
        print("Concluido... aguarde.")
        time.sleep(3)
        choice = input("----------------------------------\nDeseja fazer mais alguma operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(choice)
    elif way == "5":
        print(c1.isEqual(c2))
        print("Concluido... aguarde.")
        time.sleep(3)
        choice = input("----------------------------------\nDeseja fazer mais alguma operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(choice)
    else:
        print("Número inválido, tente novamente")
    #Limpar a tela (funciona somente em terminais):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


