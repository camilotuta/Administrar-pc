"""Módulo para ejecutar comandos por consola"""

from subprocess import CalledProcessError, TimeoutExpired, run
from mensajes.mensaje import (
    body_mensaje_comando_consola_con_resultado,
    body_mensaje_comando_consola_sin_resultado,
)
from mensajes.mensaje_error import body_mensaje_error_comando_consola
from interactuar.texto import quitar_saltos_linea, quitar_espacios_antes_palabra


def ejecutar_consola(comando):
    """Se ejecutará por la consola de Windows el comando recibido

    Args:
        comando (str): comando para ejecutarlo en consola
    """

    try:
        resultado = run(
            comando,
            shell=True,
            check=True,
            timeout=10,
            capture_output=True,
            text=True,
        )
        return body_mensaje_comando_consola_con_resultado(
            comando.capitalize(),
            quitar_espacios_antes_palabra(quitar_saltos_linea(resultado.stdout)),
        )
    except CalledProcessError as e:
        if e.stderr:
            return body_mensaje_error_comando_consola(
                quitar_espacios_antes_palabra(quitar_saltos_linea(e.stderr))
            )
    except TimeoutExpired as e:
        if e.stderr:
            return body_mensaje_error_comando_consola(
                quitar_espacios_antes_palabra(quitar_saltos_linea(e.stderr))
            )
    except ValueError:
        return body_mensaje_comando_consola_sin_resultado(comando.capitalize())
    return body_mensaje_comando_consola_sin_resultado(comando.capitalize())
