"""Modulo principal del programa donde se verifica cada acción del usuario para enviar un reporte
del estado de la bateria del portátil"""

# cSpell:ignore bateria whatsapp
import bateria
import mensaje_whatsapp
import mensajes

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
            ):
                mensaje_whatsapp.enviar_mensaje(mensajes.body_descargado())
            bateria_pasada = bateria.obtener_porcentaje_bateria()

        if (
            bateria.obtener_porcentaje_bateria() != bateria_pasada
            and bateria.obtener_porcentaje_bateria() == 100
            and bateria.bateria_esta_cargando()
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
            else:
                mensaje_whatsapp.enviar_mensaje(mensajes.body_mensaje_desconocido())
            hora_mensaje_pasado = mensaje_whatsapp.obtener_hora_ultimo_mensaje()
