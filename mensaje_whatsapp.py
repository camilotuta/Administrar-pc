"""Módulo para administrar los mensajes de WhatsApp por Twilio"""

# cSpell:ignore twilio whatsapp bateria dotenv proyects
import os

from dotenv import load_dotenv
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

# Carga las variables de entorno del archivo .env
load_dotenv(
    "C:/Users/tutaa/Workspace/Python/Proyects/Notificar Porcentaje Bateria/resources/env/.env"
)


SID = os.getenv("SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
client = Client(SID, AUTH_TOKEN)

FROM_WHATSAPP_NUMBER = os.getenv("FROM_WHATSAPP_NUMBER")
TO_WHATSAPP_NUMBER = os.getenv("TO_WHATSAPP_NUMBER")


def obtener_hora_ultimo_mensaje():
    """Se devuelve la fecha del ultimo mensaje enviado o recibido en el chat

    Returns:
        str: fecha ultimo mensaje
    """
    messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER)
    if messages:
        last_message = messages[0]
        if last_message.from_ == TO_WHATSAPP_NUMBER:
            return last_message.date_sent
    print("No se encontró hora ultimo mensaje.")
    return ""


def obtener_ultimo_mensaje():
    """Se devuelve el cuerpo del ultimo mensaje enviado o recibido por el chat

    Returns:
        str: ultimo mensaje del chat de WhatsApp
    """
    messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER)

    if messages:
        last_message = messages[0]
        if last_message.from_ == TO_WHATSAPP_NUMBER:
            return last_message.body
        return ""

    print("No se encontraron mensajes.")
    return ""


def enviar_mensaje(mensaje):
    """Se envía un mensaje al numero registrado en Twilio

    Args:
        mensaje (str): cuerpo del mensaje a enviar con Twilio a WhatsApp
    """
    try:
        client.messages.create(
            body=mensaje, from_=FROM_WHATSAPP_NUMBER, to=TO_WHATSAPP_NUMBER
        )
    except TwilioRestException as e:
        print(e)
