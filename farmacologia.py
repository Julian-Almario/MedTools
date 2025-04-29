import os
import json

with open('db/farmacologia.json', 'r', encoding='utf-8') as file:
    medicamentos = json.load(file)

def tratamiento():
    print(medicamentos[0]['nombre'])
    print(medicamentos[0]['dosis'])
    print(medicamentos[0]['via_administracion'])
    print(medicamentos[0]['frecuencia'])
    print(medicamentos[0]['indicaciones'])

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

