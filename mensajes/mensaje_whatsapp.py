"""Módulo para administrar los mensajes de WhatsApp por Twilio"""
# cSpell:ignore twilio whatsapp bateria dotenv proyects ejecucion peticion conexion

from threading import Thread

from data.user_data import (
    AUTH_TOKEN_ENV,
    FROM_WHATSAPP_NUMBER_ENV,
    SID_ENV,
    TO_WHATSAPP_NUMBER_ENV,
)
from mensajes.message_box import mostrar_mensaje_sin_detener_ejecucion
from twilio.rest import Client
from funciones.funciones_control import esperar_conexion_internet


def conectar_cliente():
    """Se establece conexión con el servidor de twilio

    Return: Objeto con la conexión del servidor de twilio
    """
    esperar_conexion_internet()
    try:
        return Client(SID_ENV, AUTH_TOKEN_ENV)
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL CONECTARSE CON EL SERVIDOR", str(e)
        )
        return None


client = conectar_cliente()


def obtener_hora_ultimo_mensaje():
    """Se devuelve la fecha del ultimo mensaje enviado o recibido en el chat

    Returns:
        str: fecha ultimo mensaje
    """
    esperar_conexion_internet()
    try:
        messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER_ENV)
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER_ENV:
                return last_message.date_sent
        return ""
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL OBTENER HORA DEL ULTIMO MENSAJE", str(e)
        )
        return ""


def obtener_ultimo_mensaje():
    """Se devuelve el cuerpo del ultimo mensaje enviado o recibido por el chat

    Returns:
        str: ultimo mensaje del chat de WhatsApp
    """

    esperar_conexion_internet()
    try:
        messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER_ENV)
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER_ENV:
                return last_message.body.lower()
            return ""
        return ""
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion("ERROR AL OBTENER ULTIMO MENSAJE", str(e))
        return ""


def enviar_mensaje(mensaje):
    """Se envía un mensaje al numero registrado en Twilio

    Args:
        mensaje (str): cuerpo del mensaje a enviar con Twilio a WhatsApp
    """

    esperar_conexion_internet()

    def enviar_peticion():
        try:
            client.messages.create(
                body=mensaje, from_=FROM_WHATSAPP_NUMBER_ENV, to=TO_WHATSAPP_NUMBER_ENV
            )
        except Exception as e:  # pylint: disable=broad-exception-caught
            mostrar_mensaje_sin_detener_ejecucion("ERROR AL ENVIAR MENSAJE", str(e))

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()
