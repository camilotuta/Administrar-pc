"""Modulo principal del programa donde se verifica cada acción del usuario para enviar un reporte
del estado de la bateria del portátil"""

# cSpell:ignore bateria whatsapp activacion desactivacion automatica
import ejecutar
import sistema
import mensaje_whatsapp
import mensaje
import opciones
import texto


if __name__ == "__main__":
    mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_bienvenida())

    bateria_pasada = sistema.obtener_porcentaje_bateria()
    hora_mensaje_pasado = mensaje_whatsapp.obtener_hora_ultimo_mensaje()
    while True:
        if (
            sistema.obtener_porcentaje_bateria() != bateria_pasada
            and not sistema.bateria_esta_cargando()
        ):
            if (
                sistema.obtener_porcentaje_bateria() < 26
                and sistema.obtener_porcentaje_bateria() % 5 == 0
                and opciones.ENVIAR_ALERTA_AUTOMATICA
            ):
                mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_descargado())
            bateria_pasada = sistema.obtener_porcentaje_bateria()

        if (
            sistema.obtener_porcentaje_bateria() != bateria_pasada
            and sistema.obtener_porcentaje_bateria() == 100
            and sistema.bateria_esta_cargando()
            and opciones.ENVIAR_ALERTA_AUTOMATICA
        ):
            mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_cargado())
            bateria_pasada = sistema.obtener_porcentaje_bateria()

        if mensaje_whatsapp.obtener_hora_ultimo_mensaje() != hora_mensaje_pasado:
            # & BATERIA
            if texto.verificar_elemento_en_string(
                opciones.FUNCIONES_BATERIA,
                texto.quitar_acentos(mensaje_whatsapp.obtener_ultimo_mensaje().lower()),
            ):
                ejecutar.funciones_bateria[
                    opciones.FUNCIONES_BATERIA.index(
                        texto.quitar_acentos(
                            mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                        )
                    )
                ]()

            # & SISTEMA
            elif texto.verificar_elemento_en_string(
                opciones.FUNCIONES_SISTEMA,
                texto.quitar_acentos(mensaje_whatsapp.obtener_ultimo_mensaje().lower()),
            ):
                palabras = texto.quitar_acentos(
                    mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                ).split(" ")

                ejecutar.funciones_sistema[
                    opciones.FUNCIONES_SISTEMA.index(
                        texto.quitar_acentos(
                            mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                        )
                    )
                ](int(palabras[1]))

            # & CONTROL
            elif texto.verificar_elemento_en_string(
                opciones.FUNCIONES_CONTROL,
                texto.quitar_acentos(mensaje_whatsapp.obtener_ultimo_mensaje().lower()),
            ):
                palabras = texto.quitar_acentos(
                    mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                ).split(" ")
                if len(palabras) == 1:
                    ejecutar.funciones_control[
                        opciones.FUNCIONES_CONTROL.index(
                            texto.quitar_acentos(palabras[0])
                        )
                    ]()
                elif len(palabras) == 2:
                    ejecutar.funciones_control[
                        opciones.FUNCIONES_CONTROL.index(
                            texto.quitar_acentos(palabras[0] + " ")
                        )
                    ](int(palabras[1]))

            # & CONSOLA
            elif texto.verificar_elemento_en_string(
                opciones.FUNCIONES_CONSOLA,
                texto.quitar_acentos(mensaje_whatsapp.obtener_ultimo_mensaje().lower()),
            ):
                comando = (
                    mensaje_whatsapp.obtener_ultimo_mensaje()
                    .lower()
                    .replace("consola: ", "")
                )
                if len(comando) > 2:
                    ejecutar.funciones_consola[
                        opciones.FUNCIONES_CONSOLA.index(
                            texto.quitar_acentos(
                                mensaje_whatsapp.obtener_ultimo_mensaje()
                                .lower()
                                .split(" ")[0]
                            )
                        )
                    ](comando)

            # & SOPORTE
            elif texto.verificar_elemento_en_string(
                opciones.FUNCIONES_SOPORTE,
                texto.quitar_acentos(mensaje_whatsapp.obtener_ultimo_mensaje().lower()),
            ):
                ejecutar.funciones_soporte[
                    opciones.FUNCIONES_SOPORTE.index(
                        texto.quitar_acentos(
                            mensaje_whatsapp.obtener_ultimo_mensaje().lower()
                        )
                    )
                ]()
            else:
                mensaje_whatsapp.enviar_mensaje(mensaje.body_mensaje_desconocido())

            hora_mensaje_pasado = mensaje_whatsapp.obtener_hora_ultimo_mensaje()
