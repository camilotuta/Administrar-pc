"""Módulo para ejecutar comandos por consola"""

from subprocess import CalledProcessError, TimeoutExpired, run
from mensajes.mensaje import (
    body_mensaje_comando_consola_con_resultado,
    body_mensaje_comando_consola_sin_resultado,
)
from mensajes.mensaje_error import body_mensaje_error_comando_consola


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
            (str(comando).capitalize()),
            resultado.stdout.replace("\n", "").replace("\r", ""),
        )
    except CalledProcessError as e:
        if e.stderr:
            return body_mensaje_error_comando_consola(
                (e.stderr).replace("\n", "").replace("\r", "")
            )
    except TimeoutExpired as e:
        if e.stderr:
            return body_mensaje_error_comando_consola(
                (e.stderr).replace("\n", "").replace("\r", "")
            )
    except ValueError:
        return body_mensaje_comando_consola_sin_resultado((str(comando).capitalize()))
    return body_mensaje_comando_consola_sin_resultado((str(comando).capitalize()))
