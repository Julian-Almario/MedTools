from paraclinicos import hemograma
from calculadora import calculadoras
import os

def herramientas():
    print("1. Salir")
    print("2. Calculadoras")
    print("3. Hemograma")
    print("4. Ayudas diagnosticas")
    print("5. Farmacologia pediatria/adultos")
    print("-----------------------------")

def main():
    os.system("clear")
    while True:
        navgen = 0

        herramientas()
        navgen = int(input("=> "))

        if navgen == 1:
            break
        elif navgen == 2:
            calculadoras()
        elif navgen == 3:
            hemograma()
main()
