from rich.console import Console
from rich.table import Table
from modules.menu import Exit,Clean
import os

def Paraclinicos():
    while True:
        nav = 0
        print("1.Salir")
        print("2.Hemograma (Adultos)")
        nav = int(input("=> "))

        if nav == 1:
            Clean()
            break
        elif nav == 2:
            # Crear consola
            console = Console()

            # Crear tabla
            table = Table(title="Valores normales del Hemograma en Adultos")

            # Agregar columnas
            table.add_column("Parámetro", style="cyan", no_wrap=True)
            table.add_column("Valor Normal", style="green")
            table.add_column("Unidades", style="magenta")

            # Agregar filas
            table.add_row("Hemoglobina (Hombre)", "13.5 - 17.5", "g/dL")
            table.add_row("Hemoglobina (Mujer)", "12.0 - 15.5", "g/dL")
            table.add_row("Hematocrito (Hombre)", "41 - 53", "%")
            table.add_row("Hematocrito (Mujer)", "36 - 46", "%")
            table.add_row("Leucocitos", "4,000 - 11,000", "células/μL")
            table.add_row("Neutrófilos", "40 - 70", "%")
            table.add_row("Linfocitos", "20 - 45", "%")
            table.add_row("Monocitos", "2 - 8", "%")
            table.add_row("Eosinófilos", "1 - 4", "%")
            table.add_row("Basófilos", "0 - 1", "%")
            table.add_row("Plaquetas", "150,000 - 450,000", "células/μL")

            # Mostrar la tabla
            console.print(table)

            Exit()

