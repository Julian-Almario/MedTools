import os

def Exit():
    cont = input("* Para continuar: ")
    if cont == "*":
        os.system("clear")
        main = True
    else:
        os.system("clear")
        main = False

def Clean():
    os.system("clear")