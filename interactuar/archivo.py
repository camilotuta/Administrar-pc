"""Módulo para obtener información sobre directorios específicos"""

from os import listdir

RUTA_SCRIPTS = "C:\\Users\\tutaa\\scripts"


def obtener_lista_archivos(ruta):
    """Obtiene una lista de archivos en el directorio especificado.

    Args:
        ruta (str): La ruta del directorio del cual se obtendrán los archivos.

    Returns:
        str: Una cadena que contiene los nombres de los archivos en el directorio,
              cada uno precedido y seguido por comillas invertidas, y con la
              extensión ".bat" eliminada. Cada nombre de archivo está en una nueva línea.
    """
    texto_lista_archivos = ""
    archivos = listdir(ruta)
    for i in archivos:
        texto_lista_archivos += f"`{i.replace('.bat', '')}`\n"

    return texto_lista_archivos
