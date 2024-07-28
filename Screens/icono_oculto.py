"""Módulo para poner icono en el apartado de iconos ocultos en Windows"""
# cSpell:ignore peticion pystray automatica ejecucion

from os import _exit
from threading import Thread

from pystray import Menu, MenuItem, Icon
from funciones import opciones
from PIL import Image


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


def cambiar_texto_alerta_notificaciones():
    """Determina el texto para el menú de notificaciones basado en su estado actual.

    Returns:
        str: El texto que se mostrará en el menú.
    """
    if opciones.ENVIAR_ALERTA_AUTOMATICA:
        return "Desactivar Notificaciones"
    return "Activar Notificaciones"


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
                cambiar_texto_alerta_notificaciones(), cambiar_alerta_notificaciones
            ),
            MenuItem("Salir", finalizar_ejecucion),
        )
        icon_admin_app.run()

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()
