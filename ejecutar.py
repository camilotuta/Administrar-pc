"""Módulo para ejecutar todas las funciones de la aplicación con sus respectivas excepciones"""

# cSpell:ignore bateria whatsapp
from tkinter import messagebox
import mensaje_whatsapp
import sistema
import archivo
import mensaje
import mensaje_error


def apagar(tiempo):
    """Apaga la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se apagará.

    Raises:
        Exception: En caso de error al apagar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        sistema.apagar_pc(tiempo)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_apagar())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_apagar())


def reiniciar(tiempo):
    """Reinicia la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se reiniciará.

    Raises:
        Exception: En caso de error al reiniciar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        sistema.reiniciar_pc(tiempo)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_reiniciar())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_reiniciar())


def suspender(tiempo):
    """Suspende la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se suspenderá.

    Raises:
        Exception: En caso de error al suspender la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        sistema.suspender_pc(tiempo)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_suspender())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_suspender())


def bloquear(tiempo):
    """Bloquea la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se bloqueará.

    Raises:
        Exception: En caso de error al bloquear la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        sistema.bloquear_pc(tiempo)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_bloquear())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_bloquear())


def cambiar_volumen(nivel):
    """Cambia el volumen de la computadora al nivel especificado.

    Args:
        nivel (int): El nivel de volumen deseado.

    Raises:
        Exception: En caso de error al cambiar el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        sistema.cambiar_volumen(nivel)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_cambiar_volumen())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_volumen())


def cambiar_brillo(nivel):
    """Cambia el brillo de la pantalla al nivel especificado.

    Args:
        nivel (int): El nivel de brillo deseado.

    Raises:
        Exception: En caso de error al cambiar el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        sistema.cambiar_brillo(nivel)
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_cambiar_brillo())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_brillo())


def obtener_volumen():
    """Obtiene el nivel de volumen actual de la computadora.

    Raises:
        Exception: En caso de error al obtener el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_volumen())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_volumen())


def obtener_brillo():
    """Obtiene el nivel de brillo actual de la pantalla.

    Raises:
        Exception: En caso de error al obtener el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_brillo())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_brillo())


def ejecutar_consola(comando):
    """Ejecuta un comando en la consola y envía el resultado a través de WhatsApp.

    Args:
        comando (str): El comando que se ejecutará en la consola.
    """
    mensaje_whatsapp.enviar_mensaje(sistema.ejecutar_consola(comando))


def bateria():
    """Obtiene el porcentaje de batería actual y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el porcentaje de batería, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_porcentaje())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_porcentaje())


def estado():
    """Obtiene el estado actual del sistema y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el estado del sistema, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_estado())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(mensaje_error.body_mensaje_error_estado())


def desactivar():
    """Desactiva las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al desactivar las notificaciones, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(
            mensaje.body_mensaje_desactivar_notificaciones()
        )
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(
            mensaje_error.body_mensaje_error_desactivar_notificaciones()
        )


def activar():
    """Activa las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al activar las notificaciones, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_activar_notificaciones())
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(
            mensaje_error.body_mensaje_error_activar_notificaciones()
        )


def lista_comandos():
    """Envía una lista de comandos disponibles a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener la lista de comandos, se enviará un mensaje de error
        a través de WhatsApp.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(
            mensaje.body_mensaje_lista_comandos(
                archivo.obtener_lista_archivos(archivo.RUTA_SCRIPTS)
            )
        )
    except Exception:  # pylint: disable=broad-exception-caught
        mensaje_whatsapp.enviar_mensaje(
            mensaje_error.body_mensaje_error_lista_comandos()
        )


def ayuda():
    """Envía un mensaje de ayuda a través de WhatsApp.

    Raises:
        Exception: En caso de error al enviar el mensaje de ayuda, se mostrará un cuadro de mensaje
        de error.
    """
    try:
        mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_ayuda())
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL ENVIAR MENSAJE DE AYUDA", str(e))


funciones_bateria = [bateria, estado, desactivar, activar]

funciones_soporte = [
    lista_comandos,
    ayuda,
]


funciones_sistema = [
    apagar,
    reiniciar,
    suspender,
    bloquear,
]
funciones_control = [
    cambiar_volumen,
    obtener_volumen,
    cambiar_brillo,
    obtener_brillo,
]
funciones_consola = [ejecutar_consola]
