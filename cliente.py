# Clase encargada de representar los clientes del sistema
class Cliente:

    # Constructor de la clase cliente
    def __init__(self, nombre, correo):

        # Validación del nombre
        if nombre == "":
            raise ValueError("El nombre está vacío")

        # Validación del correo
        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    # Método para mostrar los datos del cliente
    def mostrar_datos(self):

        return f"Cliente: {self.__nombre} - {self.__correo}"