"""Modulo para controlar y acceder a información del dispositivo"""
# cSpell:ignore whatsapp nobreak nrundll powrprof rundll pyautogui dotenv proyects clsctx comtypes
# cSpell:ignore pycaw bateria psutil secsleft

import os
import subprocess
from ctypes import POINTER, cast

import psutil
import mensaje
import mensaje_error
import screen_brightness_control as sbc
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

NOMBRE_USUARIO = os.environ.get("USERNAME").capitalize()


def apagar_pc(tiempo_minutos):
    """Se ejecuta el comando para apagar al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para apagar al pc
    """
    os.system(f"shutdown /s /t {tiempo_minutos * 60}")


def suspender_pc(tiempo_minutos):
    """Se ejecuta el comando para suspender al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para suspender al pc
    """
    os.system(f"timeout /t {tiempo_minutos*60} /nobreak\n")
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")


def reiniciar_pc(tiempo_minutos):
    """Se ejecuta el comando para reiniciar al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para reiniciar al pc
    """
    os.system(f"shutdown /r /t {tiempo_minutos * 60}")


def ejecutar_consola(comando):
    """Se ejecutará por la consola de Windows el comando recibido

    Args:
        comando (str): comando para ejecutarlo en consola
    """
    try:
        subprocess.run(
            comando, shell=True, check=True, stderr=subprocess.PIPE, timeout=10
        )
        return mensaje.body_mensaje_comando_consola((str(comando).capitalize()))
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return mensaje_error.body_mensaje_error_comando_consola(e.stderr)


def bloquear_pc(tiempo_minutos):
    """Se ejecutará por la consola de Windows el comando para bloquear la estación de trabajo.

    Args:
        tiempo_minutos (float): cuenta regresiva para reiniciar al pc
    """
    os.system(f"timeout /t {tiempo_minutos*60} /nobreak\n")
    os.system("rundll32.exe user32.dll,LockWorkStation")


def cambiar_brillo(nivel):
    """Cambia el brillo de la pantalla.

    Args:
        nivel (int): El nivel de brillo deseado (0-100).
    """
    nivel = 0 if (nivel < 0) else 100 if (nivel >= 100) else nivel
    sbc.set_brightness(nivel)


def obtener_brillo():
    """Obtiene el brillo actual de la pantalla.

    Returns:
        int: El nivel de brillo actual (0-100).
    """
    return int(sbc.get_brightness()[0])


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


def obtener_volumen():
    """Obtiene el volumen actual del sistema.

    Returns:
        float: El nivel de volumen actual (0.0-1.0).
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # pylint: disable=protected-access
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    return int(volume.GetMasterVolumeLevelScalar() * 100)


def obtener_porcentaje_bateria():
    """Devolver el porcentaje de la bateria del portátil

    Return: (int) porcentaje bateria actual
    """

    return int(psutil.sensors_battery().percent)


def bateria_esta_cargando():
    """Devolver si la bateria del portátil está cargando

    Return: (bool) ¿bateria está cargando?
    """
    return psutil.sensors_battery().power_plugged


def obtener_tiempo_restante_bateria():
    """Devolver el tiempo de uso que le queda a la batería

    Return: (str) horas, minutos, segundos de uso de batería
    """
    battery = psutil.sensors_battery()

    if battery is None:
        return "No se pudo obtener la información de la batería."

    secs_left = battery.secsleft

    if secs_left == psutil.POWER_TIME_UNLIMITED:
        return "Batería con tiempo ilimitado (conectado a corriente)."
    if secs_left == psutil.POWER_TIME_UNKNOWN:
        return "Tiempo de batería desconocido."

    hours, remainder = divmod(secs_left, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours}h {minutes}m {seconds}s"


def obtener_estado_bateria():
    """Devolver el estado actual de la bateria si esta conectado o desconectado

    Return: (str) Conectado o Desconectado
    """
    if bateria_esta_cargando():
        return "Conectado"
    return "Desconectado"
