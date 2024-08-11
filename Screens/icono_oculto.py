"""Módulo para poner icono en el apartado de iconos ocultos en Windows"""
# cSpell:ignore peticion pystray automatica ejecucion bateria condicion

from os import _exit
from threading import Thread

from funciones import funciones_bateria, opciones
from funciones.funciones_bateria import (
    activar_ahorro_bateria,
    desactivar_ahorro_bateria,
)
from PIL import Image
from pystray import Icon, Menu, MenuItem


def crear_imagen():
    """Crea la imagen del icono que aparecerá en el apartado de iconos ocultos.

    Returns:
        Image: Devuelve un objeto con todos los datos de la imagen.
    """
    icon_path = r"C:\Users\tutaa\Workspace\Python\Projects\Administrar pc\resources\ico\icon.ico"
    image = Image.open(icon_path)
    return image


def cambiar_alerta_notificaciones(icon):
    """Cambia el estado de las alertas automáticas y reinicia el icono.

    Args:
        icon (pystray.Icon): El icono actual que se está mostrando.
    """
    opciones.ENVIAR_ALERTA_AUTOMATICA = not opciones.ENVIAR_ALERTA_AUTOMATICA
    cerrar_icono(icon)
    poner_icono_oculto()


def cambiar_ahorro_bateria(icon):
    """Cambia el estado del ahorro de bateria actual, lo activa o lo desactiva

    Args:
        icon (pystray.Icon): El icono actual que se está mostrando.
    """
    if funciones_bateria.AHORRO_ACTIVADO:
        desactivar_ahorro_bateria()
    else:
        activar_ahorro_bateria()

    cerrar_icono(icon)
    poner_icono_oculto()


def cambiar_texto_alerta_notificaciones(condicion, texto_si, texto_no):
    """Determina el texto para el menú de notificaciones basado en su estado actual.

    Returns:
        str: El texto que se mostrará en el menú.
    """
    if condicion:
        return texto_si
    return texto_no


def cerrar_icono(icon):
    """Finaliza la ejecución del icono.

    Args:
        icon (pystray.Icon): El icono actual que se está mostrando.
    """
    icon.stop()


def finalizar_ejecucion(icon):
    """Finaliza la ejecución del icono y de la aplicación.

    Args:
        icon (pystray.Icon): El icono actual que se está mostrando.
    """
    cerrar_icono(icon)
    _exit(0)


def poner_icono_oculto():
    """Ejecuta el icono en el apartado de iconos ocultos en Windows."""

    def enviar_peticion():
        """Función interna para configurar y ejecutar el icono de la aplicación."""
        icon_admin_app = Icon("test_icon", crear_imagen(), "Admin Pc")
        icon_admin_app.menu = Menu(
            MenuItem(
                cambiar_texto_alerta_notificaciones(
                    opciones.ENVIAR_ALERTA_AUTOMATICA,
                    "Desactivar Notificaciones",
                    "Activar Notificaciones",
                ),
                cambiar_alerta_notificaciones,
            ),
            MenuItem(
                cambiar_texto_alerta_notificaciones(
                    funciones_bateria.AHORRO_ACTIVADO,
                    "Desactivar Ahorro Bateria",
                    "Activar Ahorro Bateria",
                ),
                cambiar_ahorro_bateria,
            ),
            MenuItem("Salir", finalizar_ejecucion),
        )
        icon_admin_app.run()

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()
