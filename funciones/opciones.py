"""Modulo para acceder a datos de las funciones de la aplicacion"""
# cSpell:ignore aplicacion bateria automatica activacion desactivacion notis

from funciones.ejecutar_funciones import (
    activar_ahorro,
    generar_clave,
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
    pausar,
    presionar,
    reiniciar,
    reproducir,
    anterior,
    siguiente,
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
FUNCIONES_GENERAR = {
    "clave ": generar_clave,
    # "qr: ": generar_qr,
}

FUNCIONES_CONTROL = {
    "volumen ": cambiar_volumen_pc,
    "volumen": obtener_volumen,
    "brillo ": cambiar_brillo_pc,
    "brillo": obtener_brillo,
    "escribir ": escribir_teclado,
    "presionar ": presionar,
    "siguiente": siguiente,
    "anterior": anterior,
    "pausar": pausar,
    "reproducir": reproducir,
}

FUNCIONES_CONSOLA = {"consola: ": ejecutar_en_consola}

FUNCIONES_SOPORTE = {
    "lista comandos": lista_comandos,
    "ayuda": ayuda,
}
