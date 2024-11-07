import pandas as pd
import numpy as np

# ===============================================================================================================================================================================================#


def snakecase(df, columnas):
    # '''
    # Función que cambia los valores tipo str a minúsculas a partir de columnas de un DataFrame
    # '''
    for columna in columnas:
        df[columna] = df[columna].str.lower()
    return df

# ===============================================================================================================================================================================================#


def unique(df, columnnas):
    # '''
    # Función que permite obtener los valores únicos de columnas específicas de un DataFrame
    # '''
    unique_values = []
    for columna in columnnas:
        unique_values.append(df[columna].unique())
    return unique_values
