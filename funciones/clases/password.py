"""Genera una contraseña difícil de adivinar"""
# cSpell:ignore metodo numeros qwertyuiopasdfghjklzxcvbnm simbolos

import random


class Password:
    """clase que va a representar los pasos para crear una contraseña en condiciones"""

    LETRAS = "qwertyuiopasdfghjklzxcvbnm"
    NUMEROS = "1234567890"
    CARACTERES_ESPECIALES = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"

    def __init__(self, longitud=8) -> None:
        self._longitud = (
            longitud
            if longitud is not None and isinstance(longitud, int) and longitud > 8
            else 8
        )
        self._texto = ""
        self.agregar_letras()
        self.agregar_numeros()
        self.agregar_caracteres_especiales()

    @property
    def longitud(self):
        """getter de la longitud

        Returns:
            int: devuelve el tamaño de la contraseña final
        """
        return self._longitud

    @property
    def texto(self):
        """Getter de texto, contiene la contraseña final

        Returns:
            str: devuelve el texto con la contraseña actual
        """
        return self._texto

    @texto.setter
    def texto(self, texto):
        """Setter de texto

        Args:
            texto (str): Recibe un texto para que sea la nueva contraseña
        """
        self._texto = texto

    def mostrar_password(self):
        """Muestra por consola la contraseña actual"""
        print(f"La contraseña actual es: {self.texto}")

    def agregar_letras(self):
        """Añade letras al atributo texto"""
        for _ in range((self.longitud // 2)):
            if len(self.texto) < self.longitud:
                self.texto += (
                    Password.LETRAS[random.randint(0, len(Password.LETRAS) - 1)].upper()
                    if random.randint(0, 3) == 2
                    else Password.LETRAS[random.randint(0, len(Password.LETRAS) - 1)]
                )

    def agregar_caracteres(self, caracteres):
        """Agrega al atributo texto, caracteres que el usuario desee

        Args:
            caracteres (list[str]): recibe la lista de caracteres para ser agregados en el atributo
            texto
        """
        nueva_password = list(self.texto)
        for _ in range((self.longitud // 3)):
            if len(nueva_password) < self.longitud:
                nueva_password.insert(
                    random.randint(0, len(self.texto) - 1),
                    caracteres[random.randint(0, len(caracteres) - 1)],
                )
        self.texto = "".join(nueva_password)

    def agregar_numeros(self):
        """Utilizamos el metodo agregar_caracteres() para incluir numeros al atributo texto"""
        self.agregar_caracteres(Password.NUMEROS)

    def agregar_caracteres_especiales(self):
        """Utilizamos el metodo agregar_caracteres() para incluir simbolos al atributo texto"""
        self.agregar_caracteres(Password.CARACTERES_ESPECIALES)

    def __str__(self) -> str:
        return self.texto
