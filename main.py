import logging

from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import Asesoria
from reserva import Reserva

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("===== SISTEMA SOFTWARE FJ =====")

try:

    cliente1 = Cliente("Maria", "maria@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 50000, 2)

    reserva1 = Reserva(cliente1, servicio1)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    logging.error(e)

try:

    cliente2 = Cliente("", "correo.com")

except Exception as e:

    print("Error:", e)

    logging.error(e)

try:

    servicio2 = AlquilerEquipo("Computador", -20000, 3)

except Exception as e:

    print("Error:", e)

    logging.error(e)

print("El sistema sigue funcionando correctamente")