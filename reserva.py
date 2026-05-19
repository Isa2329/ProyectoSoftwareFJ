# Clase encargada de gestionar las reservas
class Reserva:

    # Constructor de la reserva
    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    # Método para confirmar la reserva
    def confirmar(self):

        self.estado = "Confirmada"

    # Método para cancelar la reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Método para mostrar información de la reserva
    def mostrar_reserva(self):

        return (
            f"{self.cliente.mostrar_datos()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )