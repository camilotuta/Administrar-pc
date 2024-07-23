"""Modulo para acceder a todos los mensajes por defecto para enviar con Twilio"""
# cSpell:ignore bateria conéctalo activacion desactivacion dotenv

from data.user_data import NOMBRE_ENV


def body_mensaje_cambiar_volumen(volumen):
    """Mensaje de confirmación para ajustar el volumen"""
    return f"""
🔊 *Volumen Ajustado al {volumen}%* 🔊

¡Hola *{NOMBRE_ENV}*!

El volumen se ha ajustado correctamente. Si deseas realizar más cambios, no dudes en decírmelo.

*Gracias por usar el sistema.*
"""


def body_mensaje_cambiar_brillo(brillo):
    """Mensaje de confirmación para ajustar el brillo"""
    return f"""
💡 *Brillo Ajustado al {brillo}%* 💡

¡Hola *{NOMBRE_ENV}*!

El brillo se ha ajustado correctamente. Si necesitas hacer más ajustes, aquí estoy para ayudar.

*Gracias por usar el sistema.*
"""


def body_mensaje_volumen(volumen):
    """Mensaje para mostrar el volumen actual"""
    return f"""
🔊 *Volumen Actual: {volumen}%* 🔊

¡Hola *{NOMBRE_ENV}*!

El volumen actual es {volumen}. Si deseas realizar algún cambio, házmelo saber.

*Gracias por usar el sistema.*
"""


def body_mensaje_brillo(brillo):
    """Mensaje para mostrar el brillo actual"""
    return (
        f"""
💡 *Brillo Actual: {brillo}%* 💡

¡Hola *{NOMBRE_ENV}*!

El brillo actual es {brillo}. Si necesitas realizar algún ajuste, aquí estoy """
        + """para ayudar.

*Gracias por usar el sistema.*
"""
    )


def body_mensaje_comando_consola_con_resultado(comando, resultado):
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

¡Hola *{NOMBRE_ENV}*!

El comando `{comando}` se está ejecutando en la consola de Windows. Por favor, espera un momento"""
        + f"""mientras procesamos tu solicitud.

Resultado:

`{resultado}`

*Gracias por tu paciencia.*
"""
    )


def body_mensaje_comando_consola_sin_resultado(comando):
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

¡Hola *{NOMBRE_ENV}*!

El comando `{comando}` se está ejecutando en la consola de Windows. Por favor, espera un momento"""
        + """mientras procesamos tu solicitud.

*Gracias por tu paciencia.*
"""
    )


def body_mensaje_cargado(porcentaje_bateria):
    """Se devuelve el mensaje para cuando la bateria este al 100% de carga

    Returns:
        str: Mensaje de 100% de bateria
    """
    return (
        f"""
🔋✨ ¡Portátil al *{porcentaje_bateria}%* de batería! 🌟

😁✨💻🔋

¡Hola *{NOMBRE_ENV}*!

Quería informarte que tu portátil está completamente cargado y listo para desconectar. 🚀 Es """
        + """increíble lo eficiente que es este dispositivo. ¡Estoy emocionado de usarlo al """
        + """máximo! 😎

*Gracias por tu atención.*
"""
    )


def body_mensaje_descargado(porcentaje_bateria, tiempo_restante_bateria):
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
⚠️🔋 *¡Batería baja en el portátil!* ⚠️

😟🔋💻⚠️

¡Hola *{NOMBRE_ENV}*!

Quería informar que la batería de tu portátil está al *{porcentaje_bateria}%*."""
        + f""" 🔋 Tiempo restante estimado: *{tiempo_restante_bateria}*. Por"""
        + """ favor, conéctalo al cargador pronto para evitar interrupciones. 🙏

*Gracias por tu atención.*
"""
    )


def body_mensaje_porcentaje(
    porcentaje_bateria, estado_bateria, tiempo_restante_bateria
):
    """Se devuelve el mensaje para cuando la bateria este en menos de 25% de carga

    Returns:
        str: Mensaje de bateria proxima a descargarse
    """
    return (
        f"""
🔋⚡ *Estado de la Batería: {porcentaje_bateria}%, """
        + f"""{estado_bateria}* 🔍

¡Hola *{NOMBRE_ENV}*!

Solo quería informarte sobre el estado actual de la batería de tu portátil. Estamos al """
        + f"""*{porcentaje_bateria}%*, con un tiempo restante estimado de """
        + f"""*{tiempo_restante_bateria}*. ¡Sigue así y mantén tu productividad"""
        + """ en alto! 💪

*Gracias por tu atención.*
"""
    )


def body_mensaje_estado(estado_bateria):
    """Se devuelve el mensaje informando si la bateria está conectado o desconectado

    Returns:
        str: Mensaje de bateria conectada o desconectada
    """

    return (
        f"""
💻📊 *Estado Actual del Portátil: {estado_bateria}* 🛡️

¡Hola *{NOMBRE_ENV}*!

Te quería informar sobre el estado actual de tu portátil: *{estado_bateria}*."""
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

¡Hola *{NOMBRE_ENV}*!

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
    return f"""
💡📘 *Ayuda y Soporte* 📘💡

¡Hola *{NOMBRE_ENV}*!

Parece que necesitas un poco de ayuda. Aquí tienes algunos comandos que puedes utilizar:

🔋 *Funciones de Batería:*
1️⃣ *Consultar Estado de Batería:* `Estado`
2️⃣ *Porcentaje de Batería:* `Bateria`
3️⃣ *Activar Alertas:* `Activar`
4️⃣ *Desactivar Alertas:* `Desactivar`

💻 *Funciones del Sistema:*
1️⃣ *Apagar el PC:* `Apagar [minutos]`
2️⃣ *Reiniciar el PC:* `Reiniciar [minutos]`
3️⃣ *Suspender el PC:* `Suspender [minutos]`
4️⃣ *Bloquear el PC:* `Bloquear [minutos]`

🎚 *Funciones de Control:*
1️⃣ *Obtener Volumen:* `Volumen`
2️⃣ *Cambiar Volumen:* `Volumen [nivel 0-100]`
3️⃣ *Obtener Brillo:* `Brillo`
4️⃣ *Cambiar Brillo:* `Brillo [nivel 0-100]`

💻 *Funciones de Consola:*
1️⃣ *Comando en Consola:* `Consola: [comando]`

🛠 *Funciones de Soporte:*
1️⃣ *Comandos Personalizados:* `Lista comandos`
2️⃣ *Ayuda:* `Ayuda`

*Gracias por tu atención y confianza en nosotros.*
"""


def body_mensaje_activar_notificaciones():
    """Se devuelve el mensaje para confirmar la activación de notificaciones

    Returns:
        str: Mensaje de confirmación de activación de notificaciones
    """

    return (
        f"""
🔔✅ *¡Notificaciones Activadas!* ✅🔔

¡Hola *{NOMBRE_ENV}*!

Las alertas de batería han sido activadas exitosamente. A partir de ahora, recibirás """
        + """notificaciones sobre el estado y el porcentaje de tu batería.

*Gracias por utilizar nuestro servicio.*
"""
    )


def body_mensaje_desactivar_notificaciones():
    """Se devuelve el mensaje para confirmar la desactivación de notificaciones

    Returns:
        str: Mensaje de confirmación de desactivación de notificaciones
    """

    return (
        f"""
🔕❌ *¡Notificaciones Desactivadas!* ❌🔕

¡Hola *{NOMBRE_ENV}*!

Las alertas de batería han sido desactivadas. Ya no recibirás notificaciones sobre el estado y el"""
        + """ porcentaje de tu batería.

*Gracias por utilizar nuestro servicio.*
"""
    )


def body_mensaje_apagar():
    """Mensaje cuando el PC se está apagando"""
    return (
        f"""
🖥️⚠️ *¡Apagando el PC!* ⚠️🖥️

¡Hola *{NOMBRE_ENV}*!

Tu computadora se está apagando ahora mismo. Asegúrate de guardar cualquier trabajo pendiente """
        + """antes de que se complete el proceso.

*Gracias por tu paciencia.*
"""
    )


def body_mensaje_reiniciar():
    """Mensaje cuando el PC se está reiniciando"""
    return (
        f"""
🔄🖥️ *¡Reiniciando el PC!* 🖥️🔄

¡Hola *{NOMBRE_ENV}*!

Tu computadora está reiniciándose en este momento. Esto solo tomará un momento. Volverá pronto a """
        + """estar disponible.

*Gracias por tu comprensión.*
"""
    )


def body_mensaje_lista_comandos(lista_archivos):
    """Se devuelve el mensaje con la lista de archivos en una carpeta

    Args:
        carpeta (str): Ruta de la carpeta

    Returns:
        str: Mensaje con la lista de archivos
    """
    return f"""
📂📋 *Lista de Comandos Personalizados* 📋📂

¡Hola *{NOMBRE_ENV}*!

Aquí tienes la lista de los comandos personalizados:

{lista_archivos}

*Gracias por utilizar nuestro servicio.*
"""


def body_mensaje_suspender():
    """Mensaje para avisar que el PC está próximo a suspenderse

    Returns:
        str: Mensaje de aviso de suspensión
    """
    return (
        f"""
💤💻 *¡El PC se va a suspender pronto!* 💻💤

¡Hola *{NOMBRE_ENV}*!

Tu computadora está a punto de suspenderse para ahorrar energía. Por favor, guarda tu trabajo"""
        + """ para evitar cualquier pérdida de datos.

*Gracias por tu atención.*
"""
    )


def body_mensaje_bienvenida():
    """Mensaje de bienvenida al inicio de la aplicación

    Returns:
        str: Mensaje de bienvenida
    """
    return (
        f"""
👋✨ *¡Bienvenido a _Admin Pc_!* ✨👋

¡Hola *{NOMBRE_ENV}*!

Nos alegra tenerte con nosotros. Esta aplicación está lista para ayudarte con el manejo y """
        + """monitoreo de tu PC. Si necesitas ayuda, no dudes en preguntar.

*Gracias por confiar en nosotros.*
"""
    )


def body_mensaje_bloquear():
    """Mensaje indicando que el PC ha sido bloqueado.

    Returns:
        str: Mensaje de PC bloqueado.
    """
    return f"""
🔒💻 *¡PC Bloqueado!* 💻🔒

¡Hola *{NOMBRE_ENV}*!

Tu computadora ha sido bloqueada con éxito. Por favor, asegúrate de que tu sesión esté segura.

*Gracias por tu atención.*
"""
