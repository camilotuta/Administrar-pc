"""Módulo para ejecutar funciones de la bateria, tales como: obtener % bateria, estado de bateria
tiempo restante de vida de la bateria y si la bateria está cargando"""
# cSpell:ignore bateria psutil secsleft energysaver esbattthreshold setactive setdcvalueindex

from os import system
from psutil import sensors_battery, POWER_TIME_UNKNOWN, POWER_TIME_UNLIMITED

AHORRO_ACTIVADO = False


def activar_ahorro_bateria():
    """Activa el modo de ahorro de batería

    Configura el sistema para que entre en modo de ahorro de batería
    Esta configuración se aplica al perfil de energía actual.
    """
    global AHORRO_ACTIVADO  # pylint: disable=[global-statement]
    AHORRO_ACTIVADO = True
    system(
        "powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 100"
    )
    system("powercfg /setactive SCHEME_CURRENT")


def desactivar_ahorro_bateria():
    """Desactiva el modo de ahorro de batería

    Configura el sistema para que no entre en modo de ahorro de batería
    Esta configuración se aplica al perfil de energía actual.
    """
    global AHORRO_ACTIVADO  # pylint: disable=[global-statement]
    AHORRO_ACTIVADO = False
    system("powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 0")
    system("powercfg /setactive SCHEME_CURRENT")


def obtener_porcentaje_bateria():
    """Devolver el porcentaje de la bateria del portátil

    Return: (int) porcentaje bateria actual
    """

    return int(sensors_battery().percent)


def bateria_esta_cargando():
    """Devolver si la bateria del portátil está cargando

    Return: (bool) ¿bateria está cargando?
    """
    return sensors_battery().power_plugged


def obtener_tiempo_restante_bateria():
    """Devolver el tiempo de uso que le queda a la batería

    Return: (str) horas, minutos, segundos de uso de batería
    """
    battery = sensors_battery()

    if battery is None:
        return "No se pudo obtener la información de la batería."

    secs_left = battery.secsleft

    if secs_left == POWER_TIME_UNLIMITED:
        return "Batería con tiempo ilimitado (conectado a corriente)."
    if secs_left == POWER_TIME_UNKNOWN:
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
