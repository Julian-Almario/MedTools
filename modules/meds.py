from modules.menu import Exit,Clean
import json

with open('db/farmacologia.json', 'r', encoding='utf-8') as file:
    Med = json.load(file)

def Tratamiento():
    while True:
        nav = 0
        print("1. Salir")
        print("2. ITU")
        print("-----------------------------")

        nav = int(input("=> "))

        if nav == 1:
            Clean()
            break


        if nav == 2:
            peso = int(input("Peso(Kg): "))

            amikacina = Med["ITU_pediatrica"]["Amikacina"]["dosis"] * peso

            print(f"Amikacina {amikacina}mg/24horas por {Med["ITU_pediatrica"]["Amikacina"]["duracion"]}")
            
            Exit()

