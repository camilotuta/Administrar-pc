"""Módulo para mostrar mensajes y no pausar la ejecucion del programa"""
# cSpell:ignore ejecucion

from tkinter import messagebox
from threading import Thread


def mostrar_mensaje_sin_detener_ejecucion(titulo, mensaje):
    """mostrar mensaje mediante messagebox y no pausar la ejecucion

    Args:
        titulo (str): titulo de la ventana del mensaje
        mensaje (str): contenido de la ventana del mensaje
    """

    def crear_mensaje_error():
        messagebox.showerror(titulo, mensaje)

    message_thread = Thread(target=crear_mensaje_error)
    message_thread.start()
