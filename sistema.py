"""Modulo para controlar el apagado y el reinicio del dispositivo"""
# cSpell:ignore whatsapp

import os

import subprocess
import mensajes


def apagar_pc(tiempo_minutos):
    """Se ejecuta el comando para apagar al pc en el tiempo recibido

    Args:
        tiempo_minutos (float): cuenta regresiva para apagar al pc
    """
    os.system(f"shutdown /s /t {tiempo_minutos * 60}")


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
        # Ejecutar el comando y capturar la salida y los errores
        subprocess.run(
            comando,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return mensajes.body_ejecutando_comando_consola((str(comando).capitalize()))
    except subprocess.CalledProcessError as e:
        return mensajes.body_error_comando_consola(e.stderr)
