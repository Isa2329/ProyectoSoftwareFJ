# Importación de librerías para clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta para representar servicios
class Servicio(ABC):

    # Constructor principal
    def __init__(self, nombre, precio):

        # Validación del precio
        if precio <= 0:
            raise ValueError("El precio debe ser positivo")

        self.nombre = nombre
        self.precio = precio

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self):
        pass


# Clase para reservas de salas
class ReservaSala(Servicio):

    # Constructor de reserva de sala
    def __init__(self, nombre, precio, horas):

        super().__init__(nombre, precio)

        self.horas = horas

    # Método para calcular el costo total
    def calcular_costo(self):

        return self.precio * self.horas


# Clase para alquiler de equipos
class AlquilerEquipo(Servicio):

    # Constructor de alquiler
    def __init__(self, nombre, precio, dias):

        super().__init__(nombre, precio)

        self.dias = dias

    # Método para calcular el costo total
    def calcular_costo(self):

        return self.precio * self.dias


# Clase para asesorías especializadas
class Asesoria(Servicio):

    # Constructor de asesoría
    def __init__(self, nombre, precio, sesiones):

        super().__init__(nombre, precio)

        self.sesiones = sesiones

    # Método para calcular el costo total
    def calcular_costo(self):

        return self.precio * self.sesiones