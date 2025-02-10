# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import glob
import re
import os


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #

    train_dataset = load_data("train")
    save_output(train_dataset, "train_dataset")
    test_dataset = load_data("test")
    save_output(test_dataset, "test_dataset")


def load_data(ruta):
    # Usamos glob para obtener los archivos txt
    archivos = glob.glob(f"files/input/{ruta}/**/*.txt", recursive=True)

    # Leemos los archivos y agregamos una columna con el nombre del directorio
    dataframes_train = []
    for archivo in archivos:
        # Leer el archivo como un DataFrame
        df = pd.read_csv(archivo, header=None, names=["phrase"])
        # Obtener el nombre del directorio que contiene el archivo
        directorio = os.path.basename(os.path.dirname(archivo))
        # Agregar el nombre del directorio como una nueva columna
        df["target"] = directorio
        # Agregar este DataFrame a la lista
        dataframes_train.append(df)

    # Concatenar todos los DataFrames en uno solo
    dataframe = pd.concat(dataframes_train, ignore_index=True)

    return dataframe


def save_output(dataframe, name, output_directory="files/output"):
    """Save output to a file."""

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    dataframe.to_csv(
        f"{output_directory}/{name}.csv",
        index=False,
    )


if "__main__" in __name__:
    pregunta_01()
