"""Se accede a la información del archivo .env"""
# cSpell:ignore dotenv whatsapp

import os

import dotenv_path  # pylint: disable=unused-import  # noqa: F401

NOMBRE_ENV = os.getenv("USER_NAME")
CORREO_ENV = os.getenv("USER_EMAIL")

SID_ENV = os.getenv("SID")
AUTH_TOKEN_ENV = os.getenv("AUTH_TOKEN")
FROM_WHATSAPP_NUMBER_ENV = os.getenv("FROM_WHATSAPP_NUMBER")
TO_WHATSAPP_NUMBER_ENV = os.getenv("TO_WHATSAPP_NUMBER")
