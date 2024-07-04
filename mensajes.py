"""Modulo para acceder a todos los mensajes por defecto para enviar con Twilio"""

# cSpell:ignore bateria conéctalo
import os
import bateria

NOMBRE_USUARIO = os.environ.get("USERNAME").capitalize()


def body_cargado():
    """Se devuelve el mensaje para cuando la bateria este al 100% de carga

    Returns:
        str: Mensaje de 100% de bateria
    """
    return (
        f"""
🔋✨ ¡Portátil al *{bateria.obtener_porcentaje_bateria()}%* de batería! 🌟

😁✨💻🔋

¡Hola *{NOMBRE_USUARIO}*!

Quería informarte que tu portátil está completamente cargado y listo para desconectar. 🚀 Es """
        + """increíble lo eficiente que es este dispositivo. ¡Estoy emocionado de usarlo al """
        + """máximo! 😎

*Gracias por tu atención.*
"""
    )


def body_descargado():
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
⚠️🔋 *¡Batería baja en el portátil!* ⚠️

😟🔋💻⚠️

¡Hola *{NOMBRE_USUARIO}*!

Quería informar que la batería de tu portátil está al *{bateria.obtener_porcentaje_bateria()}%*."""
        + f""" 🔋 Tiempo restante estimado: *{bateria.obtener_tiempo_restante()}*. Por favor, """
        + """conéctalo al cargador pronto para evitar interrupciones. 🙏

*Gracias por tu atención.*
"""
    )


def body_porcentaje():
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
🔋⚡ *Estado de la Batería: {bateria.obtener_porcentaje_bateria()}%, """
        + f"""{bateria.obtener_estado_bateria()}* 🔍

¡Hola *{NOMBRE_USUARIO}*!

Solo quería informarte sobre el estado actual de la batería de tu portátil. Estamos al """
        + f"""*{bateria.obtener_porcentaje_bateria()}%*, con un tiempo restante estimado de """
        + f"""*{bateria.obtener_tiempo_restante()}*. ¡Sigue así y mantén tu productividad en alto! 💪

*Gracias por tu atención.*
"""
    )


def body_estado():
    """Se devuelve el mensaje informando si la bateria está conectado o desconectado

    Returns:
        str: Mensaje de bateria conectada o desconectada
    """

    return (
        f"""
💻📊 *Estado Actual del Portátil: {bateria.obtener_estado_bateria()}* 🛡️

¡Hola *{NOMBRE_USUARIO}*!

Te quería informar sobre el estado actual de tu portátil: *{bateria.obtener_estado_bateria()}*."""
        + """ Es importante tener esto en cuenta para evitar cualquier inconveniente.

*Gracias por tu atención.*
"""
    )


def body_mensaje_desconocido():
    """Se devuelve el mensaje para cuando el usuario ingrese un mensaje desconocido

    Returns:
        str: Mensaje de error al procesar mensaje recibido
    """

    return (
        f"""
❓🚫 *¡Mensaje Desconocido!* ❓🚫

🤔📩💻❓

¡Hola *{NOMBRE_USUARIO}*!

Parece que hemos recibido un mensaje que no logramos entender o procesar correctamente. 😅 """
        + """Por favor, revisa el contenido y vuelve a intentarlo.

*Gracias por tu comprensión.*
"""
    )
