from math import pow


'''
a+b"i"
c+d"i"
'''

class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Iniciações alternativas:
    def initAlternative(self):
        self.x = int(input("Digite o número real: "))
        self.y = None

    def initAlternative(self):
        pass
    # Imprimir em tela os números complexos:
    def displayComplexNumber(self):
        print("Número complexo: " + str(self.x) + "+" + str(self.y) + "i")
        print("------------------------------------")
    # Comparando os números complexos para saber se são iguais, utilizando booleans:
    def isEqual(self, c2):
        if self.x == c2.x and self.y == c2.y:
            return True
        else:
            return False
    # Soma:

    #propriedade para calcular numeros complexos diz que numero real só opera com numero e numero só
    #opera com numero imaginario
    def sum(self, c2):
        self.x = self.x + c2.x
        self.y = self.y + c2.y
        if self.y > 0:
            print("Soma: " + str(self.x) + "+" + str(self.y) + "i")
        else:
            print("Soma: " + str(self.x) + str(self.y) + "i")
    # Subtração: 
    def subtract(self, c2):
        self.x = self.x - c2.x
        self.y = self.y - c2.y
        if self.y > 0:
            print("Subtração: " + str(self.x) + "+" + str(self.y) + "i")
        else:
            print("Subtração: " + str(self.x) + str(self.y) + "i")
    # Multiplicação:
    def multiplication(self, c2):
        self.x = (self.x * c2.x) - (self.y * c2.y)
        self.y = (self.x * c2.y) + (self.y * c2.x)
        if self.y > 0:
            print("Multiplicação: " + str(self.x) + "+" + str(self.y) + "i")
        else:
            print("Multiplicação: " + str(self.x) + str(self.y) + "i")
    # Divisão:
    def division(self, c2):
        self.x = ((self.x * c2.x) - (self.y * c2.y)) / ((pow(c2.x, 2)) + (pow(c2.y, 2)))
        self.y = ((self.x * c2.y) + (self.y * c2.x)) / ((pow(c2.x, 2)) + (pow(c2.y, 2)))
        if self.y > 0:
            print("Divisão: " + "{0:.2f}".format(self.x) + "+" + "{0:.2f}".format(self.y) + "i")
        else:
            print("Divisão: " + "{0:.2f}".format(self.x) + "{0:.2f}".format(self.y) + "i")

# Função para escolha de fazer reload ou sair:
def closed(choice):
    if choice == "1":
        pass
    else:
        exit()



