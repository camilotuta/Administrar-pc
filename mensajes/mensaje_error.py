"""Modulo para mostrar los mensajes de error posibles al ejecutar una función dada"""
# cSpell:ignore dotenv bateria

from data.user_data import NOMBRE_ENV


def body_mensaje_error_porcentaje():
    """Mensaje de error al establecer un porcentaje"""
    return f"""
❌⚠️ *Error al establecer el porcentaje!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar establecer el porcentaje. Por favor, verifica los valores y vuelve a intentarlo. 
Si el problema persiste, contacta con soporte técnico.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_estado():
    """Mensaje de error al intentar cambiar el estado"""
    return f"""
❌⚠️ *Error al cambiar el estado!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar cambiar el estado. Por favor, revisa la configuración y vuelve a intentarlo. 
Si el problema persiste, contacta con soporte técnico.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_desactivar_notificaciones():
    """Mensaje de error al intentar desactivar notificaciones"""
    return f"""
❌🔕 *Error al desactivar notificaciones!* 🔕❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar desactivar las notificaciones. Por favor, inténtalo de nuevo o consulta con soporte técnico.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_activar_ahorro_bateria():
    """Mensaje de error al activar el ahorro de batería"""
    return f"""
❌⚠️ *Error al activar el ahorro de batería!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar activar el ahorro de batería. Por favor, verifica la configuración y vuelve a intentarlo. 
Si el problema persiste, contacta con soporte técnico.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_desactivar_ahorro_bateria():
    """Mensaje de error al desactivar el ahorro de batería"""
    return f"""
❌⚠️ *Error al desactivar el ahorro de batería!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar desactivar el ahorro de batería. Por favor, verifica la configuración y vuelve a intentarlo. 
Si el problema persiste, contacta con soporte técnico.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_activar_notificaciones():
    """Mensaje de error al intentar activar notificaciones"""
    return f"""
❌🔔 *Error al activar notificaciones!* 🔔❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar activar las notificaciones. Por favor, verifica la configuración y vuelve a intentarlo.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_lista_comandos():
    """Mensaje de error al intentar obtener la lista de comandos"""
    return f"""
❌📜 *Error al obtener la lista de comandos!* 📜❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar acceder a la lista de comandos. Por favor, revisa la conexión y vuelve a intentarlo.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_apagar():
    """Mensaje de error al intentar apagar el PC"""
    return f"""
❌⚠️ *Error al apagar el PC!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar apagar tu computadora. Por favor, inténtalo de nuevo o consulta con soporte técnico si el problema persiste.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_reiniciar():
    """Mensaje de error al intentar reiniciar el PC"""
    return f"""
❌🔄 *Error al reiniciar el PC!* 🔄❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar reiniciar tu computadora. Por favor, verifica la situación o contacta con soporte técnico para obtener ayuda.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_comando_consola(error):
    """Se devuelve el mensaje para cuando hay error al ejecutar un comando en la consola de Windows

    Args:
        error (str): El mensaje de error

    Returns:
        str: Mensaje de error de ejecución de comando
    """
    return f"""
❌⚠️ *Error al Ejecutar Comando* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar ejecutar el comando en la consola de Windows. El error es el siguiente:
        
`{error}`

Por favor, verifica el comando y vuelve a intentarlo. Si el problema persiste, contacta con soporte técnico para obtener ayuda.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_suspender():
    """Mensaje de error al intentar suspender el PC

    Returns:
        str: Mensaje de error de suspensión
    """
    return f"""
❌💤 *Error al suspender el PC!* 💤❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar suspender tu computadora. Por favor, inténtalo de nuevo o contacta con soporte técnico si el problema persiste.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_bloquear():
    """Mensaje de error al intentar bloquear el PC.

    Returns:
        str: Mensaje de error de bloqueo.
    """
    return f"""
❌🔒 *Error al bloquear el PC!* 🔒❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar bloquear tu computadora. Por favor, inténtalo de nuevo o consulta con soporte técnico si el problema persiste.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_volumen():
    """Mensaje de error al intentar ajustar el volumen"""
    return f"""
❌🔊 *Error al ajustar el volumen!* 🔊❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar ajustar el volumen. Por favor, verifica la configuración y vuelve a intentarlo.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_brillo():
    """Mensaje de error al intentar ajustar el brillo"""
    return f"""
❌💡 *Error al ajustar el brillo!* 💡❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar ajustar el brillo. Por favor, revisa la configuración y vuelve a intentarlo.

*Gracias por tu comprensión.*
"""


def body_mensaje_error_escribir_teclado(texto):
    """Mensaje de error al intentar escribir con el teclado"""
    return f"""
❌⚠️ *Error al escribir con el teclado!* ⚠️❌

¡Hola *{NOMBRE_ENV}*!

Hubo un problema al intentar escribir el siguiente texto en el teclado:

`{texto}`

Por favor, verifica el texto e inténtalo de nuevo. Si el problema persiste, contacta con soporte técnico.

*Gracias por tu comprensión.*
"""
