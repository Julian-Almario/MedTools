import os

def salir():
    cont = input("* Para continuar: ")
    if cont == "*":
        os.system("clear")
        main = True
    else:
        os.system("clear")
        main = False