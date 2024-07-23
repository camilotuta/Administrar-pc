from tkinter import messagebox
from threading import Thread


def mostrar_mensaje_sin_detener_ejecucion(titulo, mensaje):
    def crear_mensaje_error():
        messagebox.showerror(titulo, mensaje)

    message_thread = Thread(target=crear_mensaje_error)
    message_thread.start()
