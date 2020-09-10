import time


class Crypto:
    # Iniciando com algumas especificações:
    def __init__(self):
        self.numbers = []
        print("Digite respectivamente os 4 digitos do número (0 à 9):")
        for i in range(4):
            self.numbers.append(int(input("Digito: ")))
            if self.numbers[i] > 9:
                print("Erro, tente novamente!")
                exit()
            else: 
                pass
    # Função para criptografar utilizando os passos dados na questão:
    def functionCryp(self):
        for i in range(4):
            self.numbers[i] = (self.numbers[i] + 6) % 10
        finished = str(self.numbers[2]) + str(self.numbers[3]) + str(self.numbers[0]) + str(self.numbers[1])
        print("---------------------------")
        print("Criptografando... aguarde")
        print("---------------------------")
        time.sleep(3)
        print("Critografado! \nO número é: " + finished)
        exit()
    # Função para descriptografar:
    def functionDesc(self):
        for i in range(4):
            if self.numbers[i] >= 7:
                self.numbers[i] -= 6
            else:
                self.numbers[i] += 4
        finished = str(self.numbers[2]) + str(self.numbers[3]) + str(self.numbers[0]) + str(self.numbers[1])
        print("------------------------------")
        print(" Descriptografando... aguarde")
        print("------------------------------")
        time.sleep(3)
        print("Descritografado! \nO número é: " + finished)
        exit()

