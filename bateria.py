"""Módulo para acceder a los datos de la bateria"""

# cSpell:ignore bateria psutil secsleft
import psutil


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


def obtener_tiempo_restante():
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
