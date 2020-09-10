from notepad import *
import time
import os

while True:
    print("-----------------------------------------------------------")
    print("                   BLOCO DE ANOTAÇÕES                      ")
    print("-----------------------------------------------------------")
    choice = input("SELECIONE: \n1-Criar nova anotação\n2-Alterar anotação"
                   "\n3-Buscar anotações\n -Qualquer outro caractere para sair\n")
    print("-----------------------------------------------------------")
    # Menu de escolha:
    if choice == "1":
        text = input("Anote: ")
        tags = input("Tags para busca: ")
        createNote(text, tags)
        print("-----------------------------------------------------------")
        print("Aguarde um momento, estamos processando...")
        time.sleep(3)
        aux = input("Deseja fazer mais operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(aux)
    elif choice == "2":
        newId = int(input("Informe o id da anotação: "))
        alterTagOrNote = input("Selecione: \n1-Alterar anotação\n2-Alterar tags\n")
        newData = input("Escreva aqui a alteração: \n")
        alterNote(newId, alterTagOrNote, newData)
        print("-----------------------------------------------------------")
        print("Aguarde um momento, estamos processando...")
        time.sleep(3)
        print("-----------------------------------------------------------")
        aux = input("Deseja fazer mais operação? \nPressione 1 se sim "
                       "\nOu qualquer outro caractere pra sair\n")
        closed(aux)
    elif choice == "3":
        way = input("1-Todas as notas \n2-Achar pelo id"
                    "\n3-Achar pela anotação ou tag"
                    "\n4-Achar pela data de criação\n")
        returnList = []
        if way == "1":
            returnList = listNotes()
        if way == "2":
            newFilter = input("Informe o id:\n")
            returnList = filter("id", newFilter)
        if way == "3":
            newFilter = input("Informe a anotação ou as tags:\n")
            returnList = filter("textAndTag", newFilter)
        if way == "4":
            newFilter = input("Informe a data que foi criada:\n")
            returnList = filter("create_date", newFilter)
        print("-----------------------------------------------------------")
        print("Aguarde um momento, estamos processando...")
        print("-----------------------------------------------------------")
        time.sleep(3)
        print("                  Encontrado! Aqui está:                   ")
        print("-----------------------------------------------------------")
        for note in returnList:
            print("Anotação\nNota: " + note.text + "\nTags: " + note.tags + "\nData de criação: " 
            + note.createAt)
            print("-----------------------------------------------------------")
            aux = input("Deseja fazer mais operação? \nPressione 1 se sim "
                           "\nOu qualquer outro caractere pra sair\n")
            closed(aux)
        else:
            print("Não foi possível, tente novamente")
    else:
        exit()
    # Limpeza de tela (funciona somente em terminais de comando):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
