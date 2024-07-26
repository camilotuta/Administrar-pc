"""Módulo para ejecutar funciones para controlar el volumen y el brillo del pc"""
# cSpell:ignore clsctx comtypes pycaw pyautogui

from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL
from pyautogui import typewrite
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from screen_brightness_control import get_brightness, set_brightness


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
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # pylint: disable=protected-access
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    nivel = 0 if (nivel < 0) else 100 if (nivel >= 100) else nivel

    volume.SetMasterVolumeLevelScalar(nivel / 100, None)


def obtener_volumen_actual():
    """Obtiene el volumen actual del sistema.

    Returns:
        float: El nivel de volumen actual (0.0-1.0).
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # pylint: disable=protected-access
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    return int(volume.GetMasterVolumeLevelScalar() * 100)


def escribir_con_teclado(texto):
    """Escribe el texto especificado utilizando el teclado virtual.

    Envía el texto especificado al teclado para que sea escrito tecleando manualmente.

    Args:
        texto (str): El texto que se desea escribir utilizando el teclado."""
    typewrite(texto)
