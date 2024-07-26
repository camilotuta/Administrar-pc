"""Módulo para poner icono en el apartado de iconos ocultos en windows"""
# cSpell:ignore peticion pystray

import os
from threading import Thread

import pystray
from PIL import Image


def create_image():
    """crea la imagen del icono que aparecerá en el apartado

    Returns:
        Image: devuelve un objeto con todos los datos de la imagen
    """
    icon_path = r"C:\Users\tutaa\Workspace\Python\Projects\Administrar pc\resources\ico\icon.ico"
    image = Image.open(icon_path)
    return image


def on_quit(icon):
    """Finaliza la ejecución del icono y de la aplicación

    Args:
        icon (any): icono para finalizar su ejecución
    """
    icon.stop()
    os._exit(0)


def poner_icono_oculto():
    """Ejecuta el icono en el apartado de iconos ocultos en windows"""

    def enviar_peticion():
        icon_admin_app = pystray.Icon("test_icon", create_image(), "Admin Pc")
        icon_admin_app.menu = pystray.Menu(pystray.MenuItem("Salir", on_quit))
        icon_admin_app.run()

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()
