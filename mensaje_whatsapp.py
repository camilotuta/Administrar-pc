"""Módulo para administrar los mensajes de WhatsApp por Twilio"""

# cSpell:ignore twilio whatsapp bateria dotenv proyects
import os
from tkinter import messagebox
import dotenv_path  # pylint: disable=unused-import  # noqa: F401

from twilio.rest import Client

SID = os.getenv("SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_WHATSAPP_NUMBER = os.getenv("FROM_WHATSAPP_NUMBER")
TO_WHATSAPP_NUMBER = os.getenv("TO_WHATSAPP_NUMBER")


def conectar_cliente():
    """Se establece conexión con el servidor de twilio

    Return: Objeto con la conexión del servidor de twilio
    """
    try:
        return Client(SID, AUTH_TOKEN)
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL CONECTARSE CON EL SERVIDOR", str(e))
        return None


client = conectar_cliente()


def obtener_hora_ultimo_mensaje():
    """Se devuelve la fecha del ultimo mensaje enviado o recibido en el chat

    Returns:
        str: fecha ultimo mensaje
    """
    try:
        messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER)
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER:
                return last_message.date_sent
        return ""
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL OBTENER HORA DEL ULTIMO MENSAJE", str(e))
        return ""


def obtener_ultimo_mensaje():
    """Se devuelve el cuerpo del ultimo mensaje enviado o recibido por el chat

    Returns:
        str: ultimo mensaje del chat de WhatsApp
    """
    messages = client.messages.list(limit=1, to=FROM_WHATSAPP_NUMBER)

    try:
        if messages:
            last_message = messages[0]
            if last_message.from_ == TO_WHATSAPP_NUMBER:
                return last_message.body.lower()
            return ""
        return ""
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL OBTENER ULTIMO MENSAJE", str(e))
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
    except Exception as e:  # pylint: disable=broad-exception-caught
        messagebox.showerror("ERROR AL ENVIAR MENSAJE", str(e))
