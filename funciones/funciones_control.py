"""Módulo para ejecutar funciones para controlar el volumen y el brillo del pc"""
# cSpell:ignore bluetooth clsctx comtypes nexttrack playpause prevtrack pyautogui pycaw bthserv
# cSpell:ignore  setdefaulttimeout conexion ejecucion

import time
from ctypes import POINTER, cast
from socket import AF_INET, SOCK_STREAM, error, setdefaulttimeout, socket
from time import sleep

from comtypes import CLSCTX_ALL
from mensajes.message_box import mostrar_mensaje_sin_detener_ejecucion
from pyautogui import press, typewrite
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from screen_brightness_control import get_brightness, set_brightness

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # pylint: disable=protected-access
volume = cast(interface, POINTER(IAudioEndpointVolume))


def esperar_conexion_internet():
    """Mantiene un contador mientras encuentra conexión a internet, con límite de tiempo"""
    while not conectado_internet():
        sleep(2)
    return True


def conectado_internet():
    """Comprueba si el dispositivo tiene conexión a internet

    Returns:
        bool: True si el dispositivo tiene internet y False si hay algún error
    """
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect(("8.8.8.8", 53))
        conn.close()
        return True
    except error:
        return False


def cambiar_brillo(nivel):
    """Cambia el brillo de la pantalla.

    Args:
        nivel (int): El nivel de brillo deseado (0-100).
    """
    nivel = 0 if (nivel < 0) else 100 if (nivel >= 100) else nivel
    set_brightness(nivel)


def obtener_brillo_actual():
    """Obtiene el brillo actual de la pantalla.

    Returns:
        int: El nivel de brillo actual (0-100).
    """
    return int(get_brightness()[0])


def cambiar_volumen(nivel):
    """Cambia el volumen del sistema.

    Args:
        nivel (float): El nivel de volumen deseado (0.0-1.0).
    """

    nivel = 0 if (nivel < 0) else 100 if (nivel >= 100) else nivel

    volume.SetMasterVolumeLevelScalar(nivel / 100, None)


def obtener_volumen_actual():
    """Obtiene el volumen actual del sistema.

    Returns:
        float: El nivel de volumen actual (0.0-1.0).
    """

    return int(volume.GetMasterVolumeLevelScalar() * 100)


def escribir_con_teclado(texto):
    """Escribe el texto especificado utilizando el teclado virtual.

    Envía el texto especificado al teclado para que sea escrito tecleando manualmente.

    Args:
        texto (str): El texto que se desea escribir utilizando el teclado."""
    typewrite(texto)


def presionar_con_teclado(tecla):
    """Presiona una tecla especificada.

    Args:
        tecla (str): La tecla que se desea presionar.
    """
    press(tecla)


def pausar_multimedia():
    """Pausa o reanuda la reproducción multimedia."""
    press("playpause")


def reproducir_multimedia():
    """Reproduce o pausa la reproducción multimedia."""
    press("playpause")


def reproducir_siguiente_contenido():
    """Reproduce la siguiente pista multimedia."""
    press("nexttrack")


def reproducir_anterior_contenido():
    """Reproduce la pista multimedia anterior."""
    press("prevtrack")
