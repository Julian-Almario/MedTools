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


        if nav == 2:
            peso = int(input("Peso(Kg): "))

            amikacina = peso * 15

            print(f"Amikacina {amikacina}mg/24horas")

