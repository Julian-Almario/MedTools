from modules.para import Paraclinicos
from modules.cal import Calculadoras
from modules.meds import Tratamiento
from modules.menu import Clean

def herramientas():
    print("1. Salir")
    print("2. Calculadoras")
    print("3. Hemograma")
    print("4. Farmacologia pediatria/adultos")
    print("-----------------------------")

def main():
    Clean()
    while True:
        navgen = 0

        herramientas()
        navgen = int(input("=> "))
        
        #Menu principal
        if navgen == 1:
            Clean()
            break
        elif navgen == 2:
            Calculadoras()
        elif navgen == 3:
            Paraclinicos()
        elif navgen == 4:
            Tratamiento()


main()
