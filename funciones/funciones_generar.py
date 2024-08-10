"""Módulo para generar qr y contraseña aleatoria"""

# cSpell: ignore codigo codigos contrasena
from funciones.clases.password import Password


def generar_clave_aleatoria(longitud):
    """Genera la contraseña según el tamaño ingresa

    Args:
       longitud (int): tamaño de la contraseña
    """
    return Password(longitud)
