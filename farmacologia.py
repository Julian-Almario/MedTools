import os

def tratamiento():
    while True:
        nav = 0
        print("1. Salir")
        print("2. ITU")
        print("-----------------------------")

        nav = int(input("=> "))

        if nav == 1:
            os.system("clear")
            break

#
        if nav == 2:
            print("Si paciente es < 1 año inserta * ")
            meseoaños = int(input("=> "))
            edad = int(input("=> "))
            peso = int
