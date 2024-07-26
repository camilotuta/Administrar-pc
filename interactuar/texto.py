"""Módulo para interactuar con cadenas de texto"""

from re import sub
from unicodedata import category, normalize


def quitar_espacios_antes_palabra(texto):
    """Elimina los espacios en blanco al inicio de una cadena de texto.

    Args:
        texto (str): La cadena de texto de la que se quieren eliminar los espacios al inicio.

    Returns:
        str: La cadena de texto sin los espacios iniciales.
    """
    return sub(r"^\s+", "", texto)


def quitar_saltos_linea(texto):
    """Elimina los saltos de línea (\n y \r) de una cadena de texto.

    Args:
        texto (str): La cadena de texto de la que se quieren eliminar los saltos de línea.

    Returns:
        str: La cadena de texto sin saltos de línea.
    """
    return sub(r"[\n\r]", "", str(texto))


def quitar_acentos(texto):
    """Elimina los acentos de una cadena de texto.

    Args:
        texto (str): La cadena de texto de la que se quieren eliminar los acentos.

    Returns:
        str: La cadena de texto sin acentos.
    """
    texto_normalizado = normalize("NFD", texto)
    texto_sin_acentos = "".join(c for c in texto_normalizado if category(c) != "Mn")
    return texto_sin_acentos


def verificar_elemento_en_string(lista, texto):
    """verifica si un elemento de una lista dada, esta dentro de una cadena de texto

    Args:
        lista (list): lista con elementos string
        texto (str): texto

    Returns:
        bool: devuelve si algún elemento de la lista esta en la cadena de texto
    """
    for elemento in lista:
        if elemento in texto:
            return True

    return False


def verificar_llave_diccionario_en_string(dic, cadena):
    """verifica si un elemento de un diccionario dado, esta dentro de una cadena de texto

    Args:
        diccionario (dic): diccionario lleves string y funciones como valores
        texto (str): texto

    Returns:
        bool: devuelve si algún elemento del diccionario esta en la cadena de texto
    """
    for y, _ in dic.items():
        if y in cadena:
            return True
    return False
