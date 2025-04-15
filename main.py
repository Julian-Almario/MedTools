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
    
#Liquidos en paciente quemado
    peso = 0
    holliday = 0
    parklnd = 0
    if nav == 2:
        peso = int(input("Peso(Kg): "))
        acq = int(input("ACQ: "))

        if peso < 10:
            holliday = peso * 100

        elif peso > 11 and peso < 20:
            val = (peso - 10) * 50  
            holliday = 1000 + val

        else:
            val = (peso - 20) * 20
            holliday = 1500 + val

        parkland = (((4 * peso) * acq) + holliday) / 2
        
        solu1 = parkland / 8
        solu2 = parkland / 16

        #Solucion
        print(f"Pasar {solu1}cc/hora de harmant o SS 0,9% por 8 horas, y {solu2}cc/hora por 16 horas")


# Administracion de liquidos




calculadoras()
