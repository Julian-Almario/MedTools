import os

def herramientas():
    print("1. Calculadoras")
    print("2. Farmacologia Pediatria/Adultos")
    print("3. Criterios clinicos")
    print("4. Ayudas diagnosticas")
    print("0. Salir")
    print("-----------------------------")






def calculadoras():
    print("1. Salir")
    print("2. Liquidos en paciente quemado")
    print("-----------------------------")

    nav = int(input("=> "))
    peso = 0
    holliday = 0
    parklnd = 0

    if nav == 2:
        peso = int(input("Peso(Kg): "))
        acq = int(input("ACQ: "))

        if peso < 10:
            holliday = peso * 100
            print(holliday)

        elif peso > 11 and peso < 20:
            val = (peso - 10) * 50  
            holliday = 1000 + val
            print(holliday)

        else:
            val = (peso - 20) * 20
            holliday = 1500 + val
            print(holliday)


        parkland = (((4 * peso) * acq) + holliday) / 2

        print("pasar en 8 horas")
        print(parkland)

        print("pasar en 16 horas")
        print(parkland)


calculadoras()
