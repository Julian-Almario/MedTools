import os


def herramientas():
    print("1. Salir")
    print("2. Calculadoras")
    print("3. Criterios clinicos")
    print("4. Ayudas diagnosticas")
    print("5. Farmacologia pediatria/adultos")
    print("-----------------------------")

def calculadoras():
    while True:
        print("1. Salir")
        print("2. Liquidos en paciente quemado")
        print("3. Liquidos en general")
        print("-----------------------------")

        cont = "o"
        nav = int(input("=> "))
        
        if nav == 1:
            break

#Liquidos en paciente quemado
        if nav == 2:
            peso = 0
            holliday = 0
        
        #Variables a usar en parkland
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

        # parkland = (((4 * peso) * acq) + holliday) / 2
            park1 = 4 * peso
            park2 = park1 * acq
            park3 = park2 + holliday
            park4 = park3 / 2

            solu1 = park4 / 8
            solu2 = park4 / 16

        #Solucion
            print(f"Pasar {solu1}cc/hora de harmant o SS 0,9% por 8 horas, y {solu2}cc/hora por 16 horas")
            print("SOLUCION")
            print(f"4 * {peso} = {park1} * {acq} = {park2} + {holliday} = {park3} / 2 = {park4}")
            print("-------------------")
            
            #break
            cont = input("* Para continuar: ")
            if cont == "*":
                continue
            else:
                break

# Administracion de liquidos holliday
        if nav == 3:

            peso = 0
            holliday = 0
            correcciondeficit = 0
            timexbolo = 0

            peso = int(input("Peso(Kg): "))
            gradoshok = int(input("Grado de deficit: "))
            #Correccion de deficit de liquidos
            #Paciente menor de 12kg
            if peso < 12 and gradoshok == 1:
                timexbolo = 2
                bolo = (peso * 50) / timexbolo
            elif peso < 12 and gradoshok == 2:
                timexbolo == 4
                bolo = (peso * 100) / timexbolo
            elif peso < 12 and gradoshok == 3:
                timexbolo == 6
                bolo = (peso * 150) / timexbolo

            #Paciente que mayor de 12kg
            elif peso > 12 and gradoshok == 1:
                timexbolo = 2
                bolo = (peso * 30) / timexbolo
            elif peso > 12 and gradoshok == 2:
                timexbolo = 4
                bolo = (peso * 60) / timexbolo
            elif peso > 12 and gradoshok == 3:
                timexbolo = 6
                bolo = (peso * 90) / timexbolo
                


            #Liquidos de manteniento
            if peso < 10:
                holliday = peso * 100
            elif peso > 11 and peso < 20:
                val = (peso - 10) * 50
                holliday = 1000 + val
            else:
                val = (peso - 20) * 20
                holliday = 1500 + val

            hollidayxhora = holliday / 24

            print(f"Administrar bolo de lactato o SS a 0,9% a {bolo}cc/Hora en {timexbolo} horas")
            print(f"administrar {hollidayxhora}cc/Hora hasta 24 horas")
            #break
            cont = input("* Para continuar: ")
            if cont == "*":
                continue
            else:
                break


def main():

    while True:
        navgen = 0

        herramientas()
        navgen = int(input("=> "))

        if navgen == 1:
            break
        elif navgen == 2:
            calculadoras()


main()
