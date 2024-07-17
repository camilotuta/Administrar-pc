"""Modulo para acceder a datos de las funciones de la aplicacion"""

# cSpell:ignore aplicacion bateria automatica activacion desactivacion

from ejecutar import (
    activar,
    apagar,
    ayuda,
    bateria,
    bloquear,
    cambiar_brillo_pc,
    cambiar_volumen_pc,
    desactivar,
    ejecutar_en_consola,
    estado,
    lista_comandos,
    obtener_brillo,
    obtener_volumen,
    reiniciar,
    suspender,
)

ENVIAR_ALERTA_AUTOMATICA = True
FUNCIONES_BATERIA = {
    "bateria": bateria,
    "estado": estado,
    "desactivar": desactivar,
    "activar": activar,
}

FUNCIONES_SISTEMA = {
    "apagar": apagar,
    "reiniciar": reiniciar,
    "suspender": suspender,
    "bloquear": bloquear,
}

FUNCIONES_CONTROL = {
    "volumen ": cambiar_volumen_pc,
    "volumen": obtener_volumen,
    "brillo ": cambiar_brillo_pc,
    "brillo": obtener_brillo,
}

FUNCIONES_CONSOLA = {"consola: ": ejecutar_en_consola}

FUNCIONES_SOPORTE = {
    "lista comandos": lista_comandos,
    "ayuda": ayuda,
}
