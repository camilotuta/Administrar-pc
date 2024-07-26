"""Modulo para acceder a datos de las funciones de la aplicacion"""
# cSpell:ignore aplicacion bateria automatica activacion desactivacion notis

from funciones.ejecutar_funciones import (
    activar_ahorro,
    activar_notis,
    apagar,
    ayuda,
    bateria,
    bloquear,
    cambiar_brillo_pc,
    cambiar_volumen_pc,
    desactivar_ahorro,
    desactivar_notis,
    ejecutar_en_consola,
    escribir_teclado,
    estado,
    lista_comandos,
    obtener_brillo,
    obtener_volumen,
    reiniciar,
    suspender,
)

PROGRAMA_ACTIVO = True
ENVIAR_ALERTA_AUTOMATICA = True
FUNCIONES_BATERIA = {
    "bateria": bateria,
    "estado": estado,
    "desactivar notificaciones": desactivar_notis,
    "activar notificaciones": activar_notis,
    "desactivar ahorro": desactivar_ahorro,
    "activar ahorro": activar_ahorro,
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
    "escribir ": escribir_teclado,
}

FUNCIONES_CONSOLA = {"consola: ": ejecutar_en_consola}

FUNCIONES_SOPORTE = {
    "lista comandos": lista_comandos,
    "ayuda": ayuda,
}
