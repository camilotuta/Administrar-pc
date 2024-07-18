"""Modulo de la pantalla principal del programa"""
# cSpell:ignore accion boton dwmapi hwnd pady windll

import tkinter as tk
from ctypes import windll
from tkinter import ttk

from funciones import opciones

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Admin Pc")
ventana.geometry("400x300")

# Configurar el fondo oscuro
ventana.configure(bg="#23272e")

hwnd = windll.user32.GetParent(ventana.winfo_id())
windll.dwmapi.DwmSetWindowAttribute(hwnd, 19, 2, 4)

# Aplicar un tema (opcional)
style = ttk.Style()
style.theme_use("clam")

# Estilos personalizados para el botón
style.configure(
    "TButton",
    font=("Helvetica", 12, "bold"),
    foreground="white",
    padding=10,
)
style.map(
    "TButton",
    background=[("active", "#7fa052")],
    foreground=[("active", "white")],
)


# Definir una función que será llamada cuando se presione el botón
def accion_boton_activar_programa():
    """cambia el valor de PROGRAMA_ACTIVO y el color dependiendo del valor que tengo
    PROGRAMA_ACTIVO"""
    opciones.PROGRAMA_ACTIVO = not opciones.PROGRAMA_ACTIVO
    if opciones.PROGRAMA_ACTIVO:
        style.configure(
            "TButton",
            background=["#7fa052", ("active", "#7fa052")],
        )
        boton_activar_programa.config(text=f"ACTIVADO:\n{opciones.PROGRAMA_ACTIVO}")

    else:
        style.configure(
            "TButton",
            background=["#ef5969", ("active", "#ef5969")],
        )
        boton_activar_programa.config(text=f"ACTIVADO:\n{opciones.PROGRAMA_ACTIVO}")


# Crear un botón estilizado y agregarlo a la ventana principal
boton_activar_programa = ttk.Button(
    ventana,
    text=f"ACTIVADO:\n{opciones.PROGRAMA_ACTIVO}",
    command=accion_boton_activar_programa,
    style="TButton",
)
boton_activar_programa.pack(pady=50)  # Empaquetar el botón con un margen vertical

# Crear una etiqueta con estilo y agregarla a la ventana principal
etiqueta = tk.Label(
    ventana,
    text="Bienvenido a Admin Pc",
    font=("Helvetica", 16),
    bg="#2E2E2E",
    fg="white",
)
etiqueta.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
