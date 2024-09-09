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
    try:
        esperar_conexion_internet()
        return Client(SID_ENV, AUTH_TOKEN_ENV)
    except:  # pylint: disable=bare-except  # noqa: E722
        conectar_cliente()
        return None


def obtener_hora_ultimo_mensaje():
    """Se devuelve la fecha del ultimo mensaje enviado o recibido en el chat

    Returns:
        datetime: fecha y hora del último mensaje
    """
    client = conectar_cliente()
    try:
        esperar_conexion_internet()
        messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER_ENV)
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER_ENV:
                return last_message.date_sent
        return ""
    except:  # pylint: disable=bare-except  # noqa: E722
        obtener_hora_ultimo_mensaje()


def obtener_ultimo_mensaje():
    """Se devuelve el cuerpo del ultimo mensaje enviado o recibido por el chat

    Returns:
        str: ultimo mensaje del chat de WhatsApp
    """
    client = conectar_cliente()

    try:
        esperar_conexion_internet()
        messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER_ENV)
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER_ENV:
                return last_message.body.lower()
            return ""
        return ""
    except:  # pylint: disable=bare-except  # noqa: E722
        obtener_ultimo_mensaje()


def enviar_mensaje(
    mensaje,
):
    """Se envía un mensaje al numero registrado en Twilio

    Args:
        mensaje (str): cuerpo del mensaje a enviar con Twilio a WhatsApp
    """
    client = conectar_cliente()

    def enviar_peticion():
        try:
            esperar_conexion_internet()
            client.messages.create(
                body=mensaje, from_=FROM_WHATSAPP_NUMBER_ENV, to=TO_WHATSAPP_NUMBER_ENV
            )
        except Exception as e:  # pylint: disable=broad-exception-caught
            mostrar_mensaje_sin_detener_ejecucion("ERROR AL ENVIAR MENSAJE", str(e))

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()
