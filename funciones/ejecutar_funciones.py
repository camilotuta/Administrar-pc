"""Módulo para ejecutar todas las funciones de la aplicación con sus respectivas excepciones"""
# cSpell:ignore bateria whatsapp ejecucion peticion notis aleatearia codigo

from threading import Thread

from funciones.funciones_bateria import (
    activar_ahorro_bateria,
    desactivar_ahorro_bateria,
    obtener_estado_bateria,
    obtener_porcentaje_bateria,
    obtener_tiempo_restante_bateria,
)
from funciones.funciones_generar import generar_clave_aleatoria
from funciones.funciones_consola import ejecutar_consola
from funciones.funciones_control import (
    cambiar_brillo,
    cambiar_volumen,
    escribir_con_teclado,
    obtener_brillo_actual,
    obtener_volumen_actual,
    pausar_multimedia,
    presionar_con_teclado,
    reproducir_anterior_contenido,
    reproducir_multimedia,
    reproducir_siguiente_contenido,
)
from funciones.funciones_notificaciones import (
    activar_notificaciones,
    desactivar_notificaciones,
)
from funciones.funciones_sistema import (
    apagar_pc,
    bloquear_pc,
    reiniciar_pc,
    suspender_pc,
)
from interactuar.archivo import RUTA_SCRIPTS, obtener_lista_archivos
from mensajes.mensaje import (
    body_mensaje_activar_ahorro_bateria,
    body_mensaje_activar_notificaciones,
    body_mensaje_apagar,
    body_mensaje_ayuda,
    body_mensaje_bienvenida,
    body_mensaje_bloquear,
    body_mensaje_brillo,
    body_mensaje_cambiar_brillo,
    body_mensaje_cambiar_volumen,
    body_mensaje_cargado,
    body_mensaje_desactivar_ahorro_bateria,
    body_mensaje_desactivar_notificaciones,
    body_mensaje_descargado,
    body_mensaje_desconocido,
    body_mensaje_escribir_teclado,
    body_mensaje_estado,
    body_mensaje_lista_comandos,
    body_mensaje_pausar_multimedia,
    body_mensaje_porcentaje,
    body_mensaje_presionar_con_teclado,
    body_mensaje_reiniciar,
    body_mensaje_reproducir_anterior_contenido,
    body_mensaje_reproducir_multimedia,
    body_mensaje_reproducir_siguiente_contenido,
    body_mensaje_suspender,
    body_mensaje_volumen,
    body_mensaje_generar_clave,
)
from mensajes.mensaje_error import (
    body_mensaje_error_activar_ahorro_bateria,
    body_mensaje_error_activar_notificaciones,
    body_mensaje_error_apagar,
    body_mensaje_error_bloquear,
    body_mensaje_error_brillo,
    body_mensaje_error_desactivar_ahorro_bateria,
    body_mensaje_error_desactivar_notificaciones,
    body_mensaje_error_escribir_teclado,
    body_mensaje_error_estado,
    body_mensaje_error_lista_comandos,
    body_mensaje_error_pausar_multimedia,
    body_mensaje_error_porcentaje,
    body_mensaje_error_presionar_con_teclado,
    body_mensaje_error_reiniciar,
    body_mensaje_error_reproducir_anterior_contenido,
    body_mensaje_error_reproducir_multimedia,
    body_mensaje_error_reproducir_siguiente_contenido,
    body_mensaje_error_suspender,
    body_mensaje_error_volumen,
    body_mensaje_error_generar_clave,
)
from mensajes.mensaje_whatsapp import enviar_mensaje
from mensajes.message_box import mostrar_mensaje_sin_detener_ejecucion


def mensaje_bienvenida():
    """Envía el mensaje de Bienvenida"""
    try:
        enviar_mensaje(body_mensaje_bienvenida())
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL ENVIAR MENSAJE DE BIENVENIDA", str(e)
        )


def generar_clave(longitud):
    """Genera una nueva contraseña y envía un mensaje de confirmación o de error

    Args:
        longitud (int): La longitud de la nueva contraseña
    """
    try:
        longitud = int(longitud)
        longitud_clave = (
            longitud
            if longitud is not None and isinstance(longitud, int) and longitud > 8
            else 8
        )
        clave_nueva = generar_clave_aleatoria(longitud_clave)
        enviar_mensaje(body_mensaje_generar_clave(clave_nueva))
        enviar_mensaje(str(clave_nueva))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_generar_clave())


def mensaje_desconocido():
    """Envía el mensaje de mensaje desconocido"""
    try:
        enviar_mensaje(body_mensaje_desconocido())
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL ENVIAR MENSAJE DESCONOCIDO", str(e)
        )


def bateria_descargada():
    """Envía el mensaje de batería descargada"""
    try:
        enviar_mensaje(
            body_mensaje_descargado(
                obtener_porcentaje_bateria(), obtener_tiempo_restante_bateria()
            )
        )
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL ENVIAR MENSAJE DE BATERÍA DESCARGADA", str(e)
        )


def bateria_cargada():
    """Envía el mensaje de batería cargada"""
    try:
        enviar_mensaje(body_mensaje_cargado(obtener_porcentaje_bateria()))
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL ENVIAR MENSAJE DE BATERÍA CARGADA", str(e)
        )


def activar_ahorro():
    """Activa el modo de ahorro de batería y notifica el éxito o error.

    Envía un mensaje notificando que el modo de ahorro de batería ha sido activado.
    Si ocurre un error durante la activación, se enviará un mensaje de error.

    Raises:
        Exception: En caso de error al activar el ahorro de batería, se enviará un mensaje de error.
    """
    try:
        enviar_mensaje(body_mensaje_activar_ahorro_bateria())
        activar_ahorro_bateria()
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_activar_ahorro_bateria())


def desactivar_ahorro():
    """Desactiva el modo de ahorro de batería y notifica el éxito o error.

    Envía un mensaje notificando que el modo de ahorro de batería ha sido desactivado.
    Si ocurre un error durante la desactivación, se enviará un mensaje de error.

    Raises:
        Exception: En caso de error al desactivar el ahorro, se enviará un mensaje de error.
    """
    try:
        desactivar_ahorro_bateria()
        enviar_mensaje(body_mensaje_desactivar_ahorro_bateria())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_desactivar_ahorro_bateria())


def escribir_teclado(texto):
    """Escribe el texto especificado en el teclado y notifica el éxito o error.

    Envía el texto especificado al teclado y notifica que la operación ha sido exitosa.
    Si ocurre un error al intentar escribir el texto, se enviará un mensaje de error.

    Args:
        texto (str): El texto que se desea escribir en el teclado.

    Raises:
        Exception: En caso de error al escribir el texto, se enviará un mensaje de error.
    """
    try:
        escribir_con_teclado(texto)
        enviar_mensaje(body_mensaje_escribir_teclado(texto))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_escribir_teclado(texto))


def apagar(tiempo):
    """Apaga la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se apagará.

    Raises:
        Exception: En caso de error al apagar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_apagar())
        apagar_pc(tiempo)
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_apagar())


def reiniciar(tiempo):
    """Reinicia la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se reiniciará.

    Raises:
        Exception: En caso de error al reiniciar la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_reiniciar())
        reiniciar_pc(tiempo)
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_reiniciar())


def suspender(tiempo):
    """Suspende la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se suspenderá.

    Raises:
        Exception: En caso de error al suspender la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_suspender())
        suspender_pc(tiempo)
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_suspender())


def bloquear(tiempo):
    """Bloquea la computadora después de un tiempo especificado.

    Args:
        tiempo (int): El tiempo en segundos después del cual la computadora se bloqueará.

    Raises:
        Exception: En caso de error al bloquear la computadora, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_bloquear())
        bloquear_pc(tiempo)
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_bloquear())


def cambiar_volumen_pc(nivel):
    """Cambia el volumen de la computadora al nivel especificado.

    Args:
        nivel (int): El nivel de volumen deseado.

    Raises:
        Exception: En caso de error al cambiar el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        cambiar_volumen(int(nivel))
        enviar_mensaje(body_mensaje_cambiar_volumen(obtener_volumen_actual()))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_volumen())


def cambiar_brillo_pc(nivel):
    """Cambia el brillo de la pantalla al nivel especificado.

    Args:
        nivel (int): El nivel de brillo deseado.

    Raises:
        Exception: En caso de error al cambiar el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        cambiar_brillo(int(nivel))
        enviar_mensaje(body_mensaje_cambiar_brillo(obtener_brillo_actual()))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_brillo())


def obtener_volumen():
    """Obtiene el nivel de volumen actual de la computadora.

    Raises:
        Exception: En caso de error al obtener el volumen, se enviará un mensaje de error a través
        de WhatsApp.
    """

    try:
        enviar_mensaje(body_mensaje_volumen(obtener_volumen_actual()))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_volumen())


def obtener_brillo():
    """Obtiene el nivel de brillo actual de la pantalla.

    Raises:
        Exception: En caso de error al obtener el brillo, se enviará un mensaje de error a través
        de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_brillo(obtener_volumen_actual()))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_brillo())


def ejecutar_en_consola(comando):
    """Ejecuta un comando en la consola y envía el resultado a través de WhatsApp.

    Args:
        comando (str): El comando que se ejecutará en la consola.
    """

    def enviar_peticion():
        enviar_mensaje(ejecutar_consola(comando))

    peticion_thread = Thread(target=enviar_peticion)
    peticion_thread.start()


def bateria():
    """Obtiene el porcentaje de batería actual y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el porcentaje de batería, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        enviar_mensaje(
            body_mensaje_porcentaje(
                obtener_porcentaje_bateria(),
                obtener_estado_bateria(),
                obtener_tiempo_restante_bateria(),
            )
        )
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_porcentaje())


def estado():
    """Obtiene el estado actual del sistema y lo envía a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener el estado del sistema, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        enviar_mensaje(body_mensaje_estado(obtener_estado_bateria()))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_estado())


def desactivar_notis():
    """Desactiva las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al desactivar las notificaciones, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        desactivar_notificaciones()
        enviar_mensaje(body_mensaje_desactivar_notificaciones())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_desactivar_notificaciones())


def activar_notis():
    """Activa las notificaciones y envía un mensaje de confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al activar las notificaciones, se enviará un mensaje de error a
        través de WhatsApp.
    """
    try:
        activar_notificaciones()
        enviar_mensaje(body_mensaje_activar_notificaciones())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_activar_notificaciones())


def lista_comandos():
    """Envía una lista de comandos disponibles a través de WhatsApp.

    Raises:
        Exception: En caso de error al obtener la lista de comandos, se enviará un mensaje de error
        a través de WhatsApp.
    """
    try:
        enviar_mensaje(
            body_mensaje_lista_comandos(obtener_lista_archivos(RUTA_SCRIPTS))
        )
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_lista_comandos())


def ayuda():
    """Envía un mensaje de ayuda a través de WhatsApp.

    Raises:
        Exception: En caso de error al enviar el mensaje de ayuda, se mostrará un cuadro de mensaje
        de error.
    """
    try:
        enviar_mensaje(body_mensaje_ayuda())
    except Exception as e:  # pylint: disable=broad-exception-caught
        mostrar_mensaje_sin_detener_ejecucion(
            "ERROR AL ENVIAR MENSAJE DE AYUDA", str(e)
        )


def presionar(tecla):
    """Simula la presión de una tecla y envía una confirmación a través de WhatsApp.

    Args:
        tecla (str): La tecla que se simulará.

    Raises:
        Exception: En caso de error al simular la presión de la tecla, enviará un mensaje de error
        a través de WhatsApp.
    """
    try:
        presionar_con_teclado(tecla)
        enviar_mensaje(body_mensaje_presionar_con_teclado(tecla))
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_presionar_con_teclado(tecla))


def pausar():
    """Pausa la reproducción multimedia y envía una confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al pausar la reproducción multimedia, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        pausar_multimedia()
        enviar_mensaje(body_mensaje_pausar_multimedia())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_pausar_multimedia())


def reproducir():
    """Reanuda la reproducción multimedia y envía una confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al reanudar la reproducción multimedia, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        reproducir_multimedia()
        enviar_mensaje(body_mensaje_reproducir_multimedia())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_reproducir_multimedia())


def siguiente():
    """Reproduce el siguiente contenido multimedia y envía una confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al reproducir el siguiente contenido, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        reproducir_siguiente_contenido()
        enviar_mensaje(body_mensaje_reproducir_siguiente_contenido())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_reproducir_siguiente_contenido())


def anterior():
    """Reproduce el contenido multimedia anterior y envía una confirmación a través de WhatsApp.

    Raises:
        Exception: En caso de error al reproducir el contenido anterior, se enviará un mensaje de
        error a través de WhatsApp.
    """
    try:
        reproducir_anterior_contenido()
        enviar_mensaje(body_mensaje_reproducir_anterior_contenido())
    except Exception:  # pylint: disable=broad-exception-caught
        enviar_mensaje(body_mensaje_error_reproducir_anterior_contenido())
