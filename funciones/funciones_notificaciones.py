"""Módulo para configurar las notificaciones automáticas de la aplicación"""
# cSpell:ignore automatica notifiaciones

from funciones import opciones


def desactivar_notificaciones():
    """Cambia el estado de la variable ENVIAR_ALERTA_AUTOMATICA a False"""
    opciones.ENVIAR_ALERTA_AUTOMATICA = False


def activar_notificaciones():
    """Cambia el estado de la variable ENVIAR_ALERTA_AUTOMATICA a True"""
    opciones.ENVIAR_ALERTA_AUTOMATICA = True
