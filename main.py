"""Modulo principal del programa donde se verifica cada acción del usuario para enviar un reporte
del estado de la bateria del portátil"""

# cSpell:ignore bateria whatsapp activacion desactivacion automatica
import archivo
import sistema
import bateria
import mensaje_whatsapp
import mensajes

ENVIAR_ALERTA_AUTOMATICA = True

if __name__ == "__main__":
    bateria_pasada = bateria.obtener_porcentaje_bateria()
    hora_mensaje_pasado = mensaje_whatsapp.obtener_hora_ultimo_mensaje()
    while True:
        if (
            bateria.obtener_porcentaje_bateria() != bateria_pasada
            and not bateria.bateria_esta_cargando()
        ):
            if (
                bateria.obtener_porcentaje_bateria() < 26
                and bateria.obtener_porcentaje_bateria() % 5 == 0
                and ENVIAR_ALERTA_AUTOMATICA
            ):
                mensaje_whatsapp.enviar_mensaje(mensajes.body_descargado())
            bateria_pasada = bateria.obtener_porcentaje_bateria()

        if (
            bateria.obtener_porcentaje_bateria() != bateria_pasada
            and bateria.obtener_porcentaje_bateria() == 100
            and bateria.bateria_esta_cargando()
            and ENVIAR_ALERTA_AUTOMATICA
        ):
            mensaje_whatsapp.enviar_mensaje(mensajes.body_cargado())
            bateria_pasada = bateria.obtener_porcentaje_bateria()

        if mensaje_whatsapp.obtener_hora_ultimo_mensaje() != hora_mensaje_pasado:
            if (
                "bateria" in mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                or "batería" in mensaje_whatsapp.obtener_ultimo_mensaje().lower()
            ):
                mensaje_whatsapp.enviar_mensaje(mensajes.body_porcentaje())
            elif "estado" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                mensaje_whatsapp.enviar_mensaje(mensajes.body_estado())
            elif "ayuda" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                mensaje_whatsapp.enviar_mensaje(mensajes.body_mensaje_ayuda())
            elif "desactivar" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                ENVIAR_ALERTA_AUTOMATICA = False
                mensaje_whatsapp.enviar_mensaje(
                    mensajes.body_desactivacion_notificaciones()
                )
            elif "activar" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                ENVIAR_ALERTA_AUTOMATICA = True
                mensaje_whatsapp.enviar_mensaje(
                    mensajes.body_activacion_notificaciones()
                )
            elif "apagar" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                palabras = mensaje_whatsapp.obtener_ultimo_mensaje().lower().split(" ")
                if len(palabras) == 1:
                    mensaje_whatsapp.enviar_mensaje(mensajes.body_mensaje_apagando())
                    sistema.apagar_pc(0)
                elif len(palabras) == 2:
                    try:
                        mensaje_whatsapp.enviar_mensaje(
                            mensajes.body_mensaje_apagando()
                        )
                        sistema.apagar_pc(int(palabras[1]))
                    except Exception:
                        mensaje_whatsapp.enviar_mensaje(
                            mensajes.body_mensaje_error_apagado()
                        )

            elif "reiniciar" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                palabras = mensaje_whatsapp.obtener_ultimo_mensaje().lower().split(" ")
                if len(palabras) == 1:
                    mensaje_whatsapp.enviar_mensaje(mensajes.body_mensaje_reiniciando())
                    sistema.reiniciar_pc(0)
                elif len(palabras) == 2:
                    try:
                        mensaje_whatsapp.enviar_mensaje(
                            mensajes.body_mensaje_reiniciando()
                        )
                        sistema.reiniciar_pc(int(palabras[1]))
                    except Exception:
                        mensaje_whatsapp.enviar_mensaje(
                            mensajes.body_mensaje_error_reiniciado()
                        )

            elif "consola: " in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                comando = (
                    mensaje_whatsapp.obtener_ultimo_mensaje()
                    .lower()
                    .replace("consola: ", "")
                )
                mensaje_whatsapp.enviar_mensaje(sistema.ejecutar_consola(comando))

            elif "lista comandos" in mensaje_whatsapp.obtener_ultimo_mensaje().lower():
                mensaje_whatsapp.enviar_mensaje(
                    mensajes.body_lista_comandos(
                        archivo.obtener_lista_archivos(archivo.RUTA_SCRIPTS)
                    )
                )
            else:
                mensaje_whatsapp.enviar_mensaje(mensajes.body_mensaje_desconocido())
            hora_mensaje_pasado = mensaje_whatsapp.obtener_hora_ultimo_mensaje()
