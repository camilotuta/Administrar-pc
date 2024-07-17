"""Modulo principal del programa donde se verifica cada acción del usuario para enviar un reporte
del estado de la bateria del portátil"""

# cSpell:ignore bateria whatsapp activacion desactivacion automatica
from mensaje import (
    body_mensaje_bienvenida,
    body_mensaje_cargado,
    body_mensaje_descargado,
    body_mensaje_desconocido,
)
from mensaje_whatsapp import (
    enviar_mensaje,
    obtener_hora_ultimo_mensaje,
    obtener_ultimo_mensaje,
)
from opciones import (
    ENVIAR_ALERTA_AUTOMATICA,
    FUNCIONES_BATERIA,
    FUNCIONES_CONSOLA,
    FUNCIONES_CONTROL,
    FUNCIONES_SISTEMA,
    FUNCIONES_SOPORTE,
)
from sistema import bateria_esta_cargando, obtener_porcentaje_bateria
from texto import (
    quitar_acentos,
    verificar_llave_diccionario_en_string,
)

if __name__ == "__main__":
    enviar_mensaje(body_mensaje_bienvenida())

    bateria_pasada = obtener_porcentaje_bateria()
    hora_mensaje_pasado = obtener_hora_ultimo_mensaje()
    while True:
        if (
            obtener_porcentaje_bateria() != bateria_pasada
            and not bateria_esta_cargando()
        ):
            if (
                obtener_porcentaje_bateria() < 26
                and obtener_porcentaje_bateria() % 5 == 0
                and ENVIAR_ALERTA_AUTOMATICA
            ):
                enviar_mensaje(body_mensaje_descargado())
            bateria_pasada = obtener_porcentaje_bateria()

        if (
            obtener_porcentaje_bateria() != bateria_pasada
            and obtener_porcentaje_bateria() == 100
            and bateria_esta_cargando()
            and ENVIAR_ALERTA_AUTOMATICA
        ):
            enviar_mensaje(body_mensaje_cargado())
            bateria_pasada = obtener_porcentaje_bateria()

        if obtener_hora_ultimo_mensaje() != hora_mensaje_pasado:
            # & BATERIA
            if verificar_llave_diccionario_en_string(
                FUNCIONES_BATERIA,
                quitar_acentos(obtener_ultimo_mensaje().lower()),
            ):
                FUNCIONES_BATERIA[quitar_acentos(obtener_ultimo_mensaje().lower())]()

            # & SISTEMA
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_SISTEMA,
                quitar_acentos(obtener_ultimo_mensaje().lower()),
            ):
                palabras = quitar_acentos(obtener_ultimo_mensaje().lower()).split(" ")
                if len(palabras) == 1:
                    FUNCIONES_SISTEMA[(quitar_acentos(palabras[0]))](0)
                elif len(palabras) == 2:
                    FUNCIONES_SISTEMA[(quitar_acentos(palabras[0]))](palabras[1])

            # & CONTROL
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_CONTROL,
                quitar_acentos(obtener_ultimo_mensaje().lower()),
            ):
                palabras = quitar_acentos(obtener_ultimo_mensaje().lower()).split(" ")
                if len(palabras) == 1:
                    FUNCIONES_CONTROL[(quitar_acentos(palabras[0]))]()
                elif len(palabras) == 2:
                    FUNCIONES_CONTROL[(quitar_acentos(palabras[0] + " "))](palabras[1])

            # & CONSOLA
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_CONSOLA,
                quitar_acentos(obtener_ultimo_mensaje().lower()),
            ):
                comando = obtener_ultimo_mensaje().lower().replace("consola: ", "")
                if len(comando) > 2:
                    FUNCIONES_CONSOLA[
                        (
                            quitar_acentos(
                                obtener_ultimo_mensaje().lower().split(" ")[0]
                            )
                            + " "
                        )
                    ](comando)

            # & SOPORTE
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_SOPORTE,
                quitar_acentos(obtener_ultimo_mensaje().lower()),
            ):
                FUNCIONES_SOPORTE[(quitar_acentos(obtener_ultimo_mensaje().lower()))]()
            else:
                enviar_mensaje(body_mensaje_desconocido())

            hora_mensaje_pasado = obtener_hora_ultimo_mensaje()
