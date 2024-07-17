"""Módulo para ejecutar todas las funciones de la aplicación con sus respectivas excepciones"""

# cSpell:ignore bateria whatsapp
from tkinter import messagebox

from archivo import RUTA_SCRIPTS, obtener_lista_archivos
from mensaje import (
    body_mensaje_activar_notificaciones,
    body_mensaje_apagar,
    body_mensaje_ayuda,
    body_mensaje_bloquear,
    body_mensaje_brillo,
    body_mensaje_cambiar_brillo,
    body_mensaje_cambiar_volumen,
    body_mensaje_desactivar_notificaciones,
    body_mensaje_estado,
    body_mensaje_lista_comandos,
    body_mensaje_porcentaje,
    body_mensaje_reiniciar,
    body_mensaje_suspender,
    body_mensaje_volumen,
)
from mensaje_error import (
    body_mensaje_error_activar_notificaciones,
    body_mensaje_error_apagar,
    body_mensaje_error_bloquear,
    body_mensaje_error_brillo,
    body_mensaje_error_desactivar_notificaciones,
    body_mensaje_error_estado,
    body_mensaje_error_lista_comandos,
    body_mensaje_error_porcentaje,
    body_mensaje_error_reiniciar,
    body_mensaje_error_suspender,
    body_mensaje_error_volumen,
)
from mensaje_whatsapp import enviar_mensaje
from sistema import (
    apagar_pc,
    bloquear_pc,
    ejecutar_consola,
    reiniciar_pc,
    suspender_pc,
    cambiar_brillo,
    cambiar_volumen,
)


def apagar(tiempo):
    """Apaga la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se apagará.

    Raises:
        Exception: En caso de error al apagar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        apagar_pc(int(tiempo))
        enviar_mensaje(body_mensaje_apagar())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_apagar())


def reiniciar(tiempo):
    """Reinicia la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se reiniciará.

    Raises:
        Exception: En caso de error al reiniciar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        reiniciar_pc(int(tiempo))
        enviar_mensaje(body_mensaje_reiniciar())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_reiniciar())


def suspender(tiempo):
    """Suspende la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se suspenderá.

    Raises:
        Exception: En caso de error al suspender la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        suspender_pc(int(tiempo))
        enviar_mensaje(body_mensaje_suspender())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_suspender())


def bloquear(tiempo):
    """Bloquea la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se bloqueará.

    Raises:
        Exception: En caso de error al bloquear la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        bloquear_pc(int(tiempo))
        enviar_mensaje(body_mensaje_bloquear())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_bloquear())


def cambiar_volumen_pc(nivel):
    """Cambia el volumen de la computadora al nivel especificado.

    Args:
        nivel (int): El nivel de volumen deseado.

    Raises:
        Exception: En caso de error al cambiar el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        cambiar_volumen(int(nivel))
        enviar_mensaje(body_mensaje_cambiar_volumen())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_volumen())


def cambiar_brillo_pc(nivel):
    """Cambia el brillo de la pantalla al nivel especificado.

    Args:
        nivel (int): El nivel de brillo deseado.

    Raises:
        Exception: En caso de error al cambiar el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        cambiar_brillo(int(nivel))
        enviar_mensaje(body_mensaje_cambiar_brillo())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_brillo())


def obtener_volumen():
    """Obtiene el nivel de volumen actual de la computadora.

    Raises:
        Exception: En caso de error al obtener el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """

    try:
        enviar_mensaje(body_mensaje_volumen())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_volumen())


def obtener_brillo():
    """Obtiene el nivel de brillo actual de la pantalla.

    Raises:
        Exception: En caso de error al obtener el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_brillo())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_brillo())


def ejecutar_en_consola(comando):
    """Ejecuta un comando en la consola y envía el resultado a través de WhatsApp.

    Args:
        comando (str): El comando que se ejecutará en la consola.
    """
    enviar_mensaje(ejecutar_consola(comando))


def bateria():
    """Obtiene el porcentaje de batería actual y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el porcentaje de batería, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_porcentaje())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_porcentaje())


def estado():
    """Obtiene el estado actual del sistema y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el estado del sistema, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_estado())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_estado())


def desactivar():
    """Desactiva las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al desactivar las notificaciones, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_desactivar_notificaciones())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_desactivar_notificaciones())


def activar():
    """Activa las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al activar las notificaciones, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_activar_notificaciones())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_activar_notificaciones())


def lista_comandos():
    """Envía una lista de comandos disponibles a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener la lista de comandos, se enviará un mensaje de error
        a través de WhatsApp.
    """
    try:
        enviar_mensaje(
            body_mensaje_lista_comandos(obtener_lista_archivos(RUTA_SCRIPTS))
        )
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_lista_comandos())


def ayuda():
    """Envía un mensaje de ayuda a través de WhatsApp.

    Raises:
        Exception: En caso de error al enviar el mensaje de ayuda, se mostrará un cuadro de mensaje
        de error.
    """
    try:
        enviar_mensaje(body_mensaje_ayuda())
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL ENVIAR MENSAJE DE AYUDA", str(e))
