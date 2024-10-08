"""Modulo principal del programa donde se verifica cada acción del usuario para enviar un reporte
del estado de la bateria del portátil"""
# cSpell:ignore bateria whatsapp activacion desactivacion automatica ejecucion conexion

from funciones import funciones_bateria, opciones
from funciones.ejecutar_funciones import (
    bateria_cargada,
    bateria_descargada,
    mensaje_bienvenida,
    mensaje_desconocido,
)
from funciones.funciones_bateria import (
    bateria_esta_cargando,
    desactivar_ahorro_bateria,
    obtener_porcentaje_bateria,
)
from funciones.funciones_control import esperar_conexion_internet
from funciones.opciones import (
    FUNCIONES_BATERIA,
    FUNCIONES_CONSOLA,
    FUNCIONES_CONTROL,
    FUNCIONES_GENERAR,
    FUNCIONES_SISTEMA,
    FUNCIONES_SOPORTE,
    PROGRAMA_ACTIVO,
)
from interactuar.texto import (
    quitar_acentos,
    verificar_llave_diccionario_en_string,
    verificar_string_en_llave_diccionario,
)
from mensajes.mensaje_whatsapp import (
    obtener_sid_ultimo_mensaje,
    obtener_texto_ultimo_mensaje,
)
from mensajes.message_box import mostrar_mensaje_sin_detener_ejecucion
from Screens.icono_oculto import poner_icono_oculto

# TODO: colocar nuevas funciones en el mensaje de ayuda
# TODO: generador de qr


def main():
    """Ejecución principal"""

    poner_icono_oculto()
    mensaje_bienvenida()
    bateria_pasada = obtener_porcentaje_bateria()
    sid_ultimo_mensaje = obtener_sid_ultimo_mensaje()

    while PROGRAMA_ACTIVO:
        esperar_conexion_internet()
        if (
            obtener_porcentaje_bateria() != bateria_pasada
            and not bateria_esta_cargando()
        ):
            if (
                obtener_porcentaje_bateria() < 26
                and obtener_porcentaje_bateria() % 5 == 0
                and opciones.ENVIAR_ALERTA_AUTOMATICA
            ):
                bateria_descargada()
            bateria_pasada = obtener_porcentaje_bateria()

        if (
            obtener_porcentaje_bateria() != bateria_pasada
            and obtener_porcentaje_bateria() == 100
            and bateria_esta_cargando()
            and opciones.ENVIAR_ALERTA_AUTOMATICA
        ):
            bateria_cargada()
            bateria_pasada = obtener_porcentaje_bateria()

        if (
            obtener_sid_ultimo_mensaje()
            and obtener_sid_ultimo_mensaje() != sid_ultimo_mensaje
        ):
            # & BATERIA
            if verificar_string_en_llave_diccionario(
                FUNCIONES_BATERIA,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                FUNCIONES_BATERIA[quitar_acentos(obtener_texto_ultimo_mensaje())]()

            # & SISTEMA
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_SISTEMA,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                palabras = quitar_acentos(obtener_texto_ultimo_mensaje()).split(" ")
                if len(palabras) == 1:
                    FUNCIONES_SISTEMA[(quitar_acentos(palabras[0]))](0)
                elif len(palabras) == 2:
                    FUNCIONES_SISTEMA[(quitar_acentos(palabras[0]))](palabras[1])

            # & CONTROL
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_CONTROL,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                palabras = quitar_acentos(obtener_texto_ultimo_mensaje()).split(" ")
                if len(palabras) == 1:
                    FUNCIONES_CONTROL[(quitar_acentos(palabras[0]))]()
                elif len(palabras) == 2:
                    FUNCIONES_CONTROL[(quitar_acentos(palabras[0]) + " ")](palabras[1])
            # & GENERAR
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_GENERAR,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                palabras = quitar_acentos(obtener_texto_ultimo_mensaje()).split(" ")
                if len(palabras) == 2:
                    FUNCIONES_GENERAR[(quitar_acentos(palabras[0] + " "))](palabras[1])

            # & CONSOLA
            elif verificar_llave_diccionario_en_string(
                FUNCIONES_CONSOLA,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                palabras = quitar_acentos(obtener_texto_ultimo_mensaje()).split(" ")
                if len(palabras) == 1:
                    FUNCIONES_CONSOLA[(quitar_acentos(palabras[0]))]()
                elif len(palabras) >= 2:
                    FUNCIONES_CONSOLA[(quitar_acentos(palabras[0] + " "))](
                        quitar_acentos(obtener_texto_ultimo_mensaje()).replace(
                            palabras[0] + " ", ""
                        )
                    )

            # & SOPORTE
            elif verificar_string_en_llave_diccionario(
                FUNCIONES_SOPORTE,
                quitar_acentos(obtener_texto_ultimo_mensaje()),
            ):
                FUNCIONES_SOPORTE[(quitar_acentos(obtener_texto_ultimo_mensaje()))]()
            else:
                mensaje_desconocido()

            sid_ultimo_mensaje = obtener_sid_ultimo_mensaje()
        elif bateria_esta_cargando() and funciones_bateria.AHORRO_ACTIVADO:
            desactivar_ahorro_bateria()


if __name__ == "__main__":
    main()
