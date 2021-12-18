import os
import pandas as pd
from pathlib import Path


def crear_archivos():
    # leer a dataframe
    data = pd.read_csv("drugsComTest_raw.csv")

    # Se guardan todos los años en una lista
    list = []
    for x in data.date:
        list.append(x[-2:])
    # Se agrega la columna de todos los años al dataframe
    data["anio"] = list
    # se crea carpeta
    os.mkdir('archivos1')
    # se le asigna la ruta de la carpeta creada a una variable
    carpeta = Path('/home/denise/Escritorio/ultimo/archivos1')
    # Se genera un archivo por cada año diferente
    for (anio), group in data.groupby(["anio"]):
        # se crea el archivo y se le entrega una posición en donde
        # debe crearse, para que aparezca dentro de la carpeta
        # creada anteriormente
        group.to_csv(carpeta/f"año 20{anio}.csv", index=False)


if __name__ == "__main__":
    crear_archivos()
