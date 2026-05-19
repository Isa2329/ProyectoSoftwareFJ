from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio):

        if precio <= 0:
            raise ValueError("El precio debe ser positivo")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, precio, horas):

        super().__init__(nombre, precio)

        self.horas = horas

    def calcular_costo(self):

        return self.precio * self.horas


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio, dias):

        super().__init__(nombre, precio)

        self.dias = dias

    def calcular_costo(self):

        return self.precio * self.dias


class Asesoria(Servicio):

    def __init__(self, nombre, precio, sesiones):

        super().__init__(nombre, precio)

        self.sesiones = sesiones

    def calcular_costo(self):

        return self.precio * self.sesiones