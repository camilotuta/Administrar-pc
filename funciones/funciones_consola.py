"""Módulo para ejecutar comandos por consola"""

from subprocess import PIPE, CalledProcessError, run

from mensajes.mensaje import body_mensaje_comando_consola
from mensajes.mensaje_error import body_mensaje_error_comando_consola


def ejecutar_consola(comando):
    """Se ejecutará por la consola de Windows el comando recibido

    Args:
        comando (str): comando para ejecutarlo en consola
    """
    try:
        run(comando, shell=True, check=True, stderr=PIPE, timeout=10)
        return body_mensaje_comando_consola((str(comando).capitalize()))
    except CalledProcessError as e:
        return body_mensaje_error_comando_consola(str(e.stderr))
