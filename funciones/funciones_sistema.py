"""Módulo para ejecutar funciones del sistema tales como apagar, suspender, reiniciar, bloquear"""
# cSpell:ignore nobreak powrprof rundll

from os import system


def apagar_pc(tiempo_minutos):
    """Se ejecuta el comando para apagar al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para apagar al pc
    """
    system(f"shutdown /s /t {tiempo_minutos * 60}")


def suspender_pc(tiempo_minutos):
    """Se ejecuta el comando para suspender al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para suspender al pc
    """
    system(f"timeout /t {tiempo_minutos*60} /nobreak\n")
    system("rundll32.exe powrprof.dll,SetSuspendState Sleep")


def reiniciar_pc(tiempo_minutos):
    """Se ejecuta el comando para reiniciar al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para reiniciar al pc
    """
    system(f"shutdown /r /t {tiempo_minutos * 60}")


def bloquear_pc(tiempo_minutos):
    """Se ejecutará por la consola de Windows el comando para bloquear la estación de trabajo.

    Args:
        tiempo_minutos (float): cuenta regresiva para reiniciar al pc
    """
    system(f"timeout /t {tiempo_minutos*60} /nobreak\n")
    system("rundll32.exe user32.dll,LockWorkStation")
