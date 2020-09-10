from datetime import datetime
from typing import List


class Notepad:
    #Iniciando a classe:
    def __init__(self, id, text, tags, createAt):
        self.id = id
        self.text = text
        self.tags = tags
        self.createAt = createAt

# Função para criar o bloco de notas:
def createNote(text, tags):
    currentDate = datetime.today()
    with open('archive-annotations.txt', 'a', encoding="utf-8") as archive:
        id = str(sum(1 for line in open('archive-annotations.txt')) + 1)
        newText = id + " - " + text + " - " + tags + " - " + \
                currentDate.strftime("%d/%m/%Y") + "\n"
        archive.writelines(newText)

# Alterar anotações ou tags:
def alterNote(newId, alterTagOrNote, newData):
    with open('archive-annotations.txt', 'r', encoding="utf-8") as archive:
        newText = archive.readlines()
    with open('archive-annotations.txt', 'w', encoding="utf-8") as archive:
        for i in newText:
            if newText.index(i) == newId - 1:
                id, text, tags, createAt = i.split(" - ")
                if alterTagOrNote == '1':
                    archive.write(id + " - " + newData + " - " + tags + " - " + createAt)
                elif alterTagOrNote == '2':
                    archive.write(id + " - " + text + " - " + newData + " - " + createAt)
                else:
                    archive.write(id + " - " + text + " - " + tags + " - " + createAt)
            else:
                archive.write(i)

# Mostrando em tela as anotações feitas:
def listNotes():
    with open('archive-annotations.txt', 'r', encoding="utf-8") as archive:
        list = []
        for line in archive:
            id, text, tags, createAt = line.split(" - ")
            list.append(Notepad(id, text, tags, createAt))
    return list

# Filtro:
def filter(type, filter=""):
    with open('archive-annotations.txt', 'r', encoding="utf-8") as archive:
        list = []
        for line in archive:
            id, text, tags, createAt = line.split(" - ")
            if type == "id":
                if id == filter:
                    list.append(Notepad(id, text, tags, createAt))
            elif type == "textAndTag":
                if filter in text or filter in tags:
                    list.append(Notepad(id, text, tags, createAt))
            elif type == "createAt":
                if createAt == filter+"\n":
                    list.append(Notepad(id, text, tags, createAt))
    return list

# Escolha de reiniciar o código ou sair:
def closed(choice):
    if choice == "1":
        pass
    else:
        exit()



