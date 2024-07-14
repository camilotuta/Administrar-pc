"""Modulo para acceder a todos los mensajes por defecto para enviar con Twilio"""

# cSpell:ignore bateria conéctalo activacion desactivacion
import os
import bateria

NOMBRE_USUARIO = os.environ.get("USERNAME").capitalize()


def body_cargado():
    """Se devuelve el mensaje para cuando la bateria este al 100% de carga

    Returns:
        str: Mensaje de 100% de bateria
    """
    return (
        f"""
🔋✨ ¡Portátil al *{bateria.obtener_porcentaje_bateria()}%* de batería! 🌟

😁✨💻🔋

¡Hola *{NOMBRE_USUARIO}*!

Quería informarte que tu portátil está completamente cargado y listo para desconectar. 🚀 Es """
        + """increíble lo eficiente que es este dispositivo. ¡Estoy emocionado de usarlo al """
        + """máximo! 😎

*Gracias por tu atención.*
"""
    )


def body_descargado():
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
⚠️🔋 *¡Batería baja en el portátil!* ⚠️

😟🔋💻⚠️

¡Hola *{NOMBRE_USUARIO}*!

Quería informar que la batería de tu portátil está al *{bateria.obtener_porcentaje_bateria()}%*."""
        + f""" 🔋 Tiempo restante estimado: *{bateria.obtener_tiempo_restante()}*. Por favor, """
        + """conéctalo al cargador pronto para evitar interrupciones. 🙏

*Gracias por tu atención.*
"""
    )


def body_porcentaje():
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
🔋⚡ *Estado de la Batería: {bateria.obtener_porcentaje_bateria()}%, """
        + f"""{bateria.obtener_estado_bateria()}* 🔍

¡Hola *{NOMBRE_USUARIO}*!

Solo quería informarte sobre el estado actual de la batería de tu portátil. Estamos al """
        + f"""*{bateria.obtener_porcentaje_bateria()}%*, con un tiempo restante estimado de """
        + f"""*{bateria.obtener_tiempo_restante()}*. ¡Sigue así y mantén tu productividad en alto! 💪

*Gracias por tu atención.*
"""
    )


def body_estado():
    """Se devuelve el mensaje informando si la bateria está conectado o desconectado

    Returns:
        str: Mensaje de bateria conectada o desconectada
    """

    return (
        f"""
💻📊 *Estado Actual del Portátil: {bateria.obtener_estado_bateria()}* 🛡️

¡Hola *{NOMBRE_USUARIO}*!

Te quería informar sobre el estado actual de tu portátil: *{bateria.obtener_estado_bateria()}*."""
        + """ Es importante tener esto en cuenta para evitar cualquier inconveniente.

*Gracias por tu atención.*
"""
    )


def body_mensaje_desconocido():
    """Se devuelve el mensaje para cuando el usuario ingrese un mensaje desconocido

    Returns:
        str: Mensaje de error al procesar mensaje recibido
    """

    return (
        f"""
❓🚫 *¡Mensaje Desconocido!* ❓🚫

🤔📩💻❓

¡Hola *{NOMBRE_USUARIO}*!

Parece que hemos recibido un mensaje que no logramos entender o procesar correctamente. 😅 """
        + """Por favor, revisa el contenido y vuelve a intentarlo.

Puedes escribir el comando `ayuda` si necesitas conocer más opciones.

*Gracias por tu comprensión.*
"""
    )


def body_mensaje_ayuda():
    """Se devuelve el mensaje de ayuda al usuario

    Returns:
        str: Mensaje de ayuda para el usuario
    """
    return (
        f"""
💡📘 *Ayuda y Soporte* 📘💡

¡Hola *{NOMBRE_USUARIO}*!

Parece que necesitas un poco de ayuda. 
A continuación, te dejo algunas opciones y comandos que puedes utilizar:
        
1️⃣ *Consultar Estado de Batería:* Utiliza el comando `estado` para verificar si la batería está """
        + """conectada o desconectada.
        
2️⃣ *Porcentaje de Batería:* Utiliza el comando `bateria` para ver el porcentaje actual de la """
        + """batería.
        
3️⃣ *Activar Alertas:* Utiliza el comando `activar` para activar las alertas de batería.
        
4️⃣ *Desactivar Alertas:* Utiliza el comando `desactivar` para desactivar las alertas de batería.

5️⃣ *Comando en Consola:* Utiliza el comando `consola: [comando]` para ejecutarlo en la consola """
        + """de Windows.
        
6️⃣ *Comandos Personalizados:* Utiliza el comando `lista comandos` para mostrar los comandos"""
        + """ creados y ejecutarlos en la consola de Windows.

7️⃣ *Apagar el PC:* Utiliza el comando `apagar [minutos]` para apagar el PC.

8️⃣ *Reiniciar el PC:* Utiliza el comando `reiniciar [minutos]` para reiniciar el PC.
        
Si necesitas más información o tienes alguna otra consulta, no dudes en preguntar.

*Gracias por tu atención y confianza en nosotros.*
"""
    )


def body_activacion_notificaciones():
    """Se devuelve el mensaje para confirmar la activación de notificaciones

    Returns:
        str: Mensaje de confirmación de activación de notificaciones
    """

    return (
        f"""
🔔✅ *¡Notificaciones Activadas!* ✅🔔

¡Hola *{NOMBRE_USUARIO}*!

Las alertas de batería han sido activadas exitosamente. A partir de ahora, recibirás """
        + """notificaciones sobre el estado y el porcentaje de tu batería.

*Gracias por utilizar nuestro servicio.*
"""
    )


def body_desactivacion_notificaciones():
    """Se devuelve el mensaje para confirmar la desactivación de notificaciones

    Returns:
        str: Mensaje de confirmación de desactivación de notificaciones
    """

    return (
        f"""
🔕❌ *¡Notificaciones Desactivadas!* ❌🔕

¡Hola *{NOMBRE_USUARIO}*!

Las alertas de batería han sido desactivadas. Ya no recibirás notificaciones sobre el estado y el"""
        + """ porcentaje de tu batería.

*Gracias por utilizar nuestro servicio.*
"""
    )


def body_mensaje_apagando():
    """Mensaje cuando el PC se está apagando"""
    return (
        f"""
🖥️⚠️ *¡Apagando el PC!* ⚠️🖥️

¡Hola *{NOMBRE_USUARIO}*!

Tu computadora se está apagando ahora mismo. Asegúrate de guardar cualquier trabajo pendiente """
        + """antes de que se complete el proceso.

*Gracias por tu paciencia.*
"""
    )


def body_mensaje_reiniciando():
    """Mensaje cuando el PC se está reiniciando"""
    return (
        f"""
🔄🖥️ *¡Reiniciando el PC!* 🖥️🔄

¡Hola *{NOMBRE_USUARIO}*!

Tu computadora está reiniciándose en este momento. Esto solo tomará un momento. Volverá pronto a """
        + """estar disponible.

*Gracias por tu comprensión.*
"""
    )


def body_mensaje_error_apagado():
    """Mensaje de error al intentar apagar el PC"""
    return (
        f"""
❌⚠️ *Error al apagar el PC!* ⚠️❌

¡Hola *{NOMBRE_USUARIO}*!

Hubo un problema al intentar apagar tu computadora. Por favor, inténtalo de nuevo o consulta con"""
        + """ soporte técnico si el problema persiste.

*Gracias por tu comprensión.*
"""
    )


def body_mensaje_error_reiniciado():
    """Mensaje de error al intentar reiniciar el PC"""
    return (
        f"""
❌🔄 *Error al reiniciar el PC!* 🔄❌

¡Hola *{NOMBRE_USUARIO}*!

Hubo un problema al intentar reiniciar tu computadora. Por favor, verifica la situación o """
        + """contacta con soporte técnico para obtener ayuda.

*Gracias por tu comprensión.*
"""
    )


def body_ejecutando_comando_consola(comando):
    """Se devuelve el mensaje para cuando se ejecuta un comando en la consola de Windows

    Args:
        comando (str): El comando a ejecutar
        resultado (str): El resultado de la ejecución del comando

    Returns:
        str: Mensaje de ejecución de comando
    """
    return (
        f"""
🖥️⚙️ *Ejecutando Comando en Consola* ⚙️🖥️

¡Hola *{NOMBRE_USUARIO}*!

El comando `{comando}` se está ejecutando en la consola de Windows. Por favor, espera un momento"""
        + """mientras procesamos tu solicitud.

*Gracias por tu paciencia.*
"""
    )


def body_error_comando_consola(error):
    """Se devuelve el mensaje para cuando hay error al ejecutar un comando en la consola de Windows

    Args:
        error (str): El mensaje de error

    Returns:
        str: Mensaje de error de ejecución de comando
    """
    return (
        f"""
❌⚠️ *Error al Ejecutar Comando* ⚠️❌

¡Hola *{NOMBRE_USUARIO}*!

Hubo un problema al intentar ejecutar el comando en la consola de Windows. El error es el siguiente:
        
`{error.replace("\n","")}`

Por favor, verifica el comando y vuelve a intentarlo. Si el problema persiste, contacta con """
        + """soporte técnico para obtener ayuda.

*Gracias por tu comprensión.*
"""
    )


def body_lista_comandos(lista_archivos):
    """Se devuelve el mensaje con la lista de archivos en una carpeta

    Args:
        carpeta (str): Ruta de la carpeta

    Returns:
        str: Mensaje con la lista de archivos
    """
    return f"""
📂📋 *Lista de Comandos Personalizados* 📋📂

¡Hola *{NOMBRE_USUARIO}*!

Aquí tienes la lista de los comandos personalizados*:

{lista_archivos}

*Gracias por utilizar nuestro servicio.*
"""
