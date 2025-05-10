from modules.para import Paraclinicos
from modules.cal import Calculadoras
from modules.meds import Tratamiento
from modules.menu import Clean

def herramientas():
    herra = ["1. Salir","2. Calculadoras","3. Hemograma","4. Farmacologia pediatria/adultos", "----------------------"]
    for i in herra:
        print(i)


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
