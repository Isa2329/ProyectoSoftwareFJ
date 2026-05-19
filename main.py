# Importación de librerías
import logging

# Importación de clases
from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import Asesoria
from reserva import Reserva

# Configuración del sistema de logs
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Inicio del sistema
print("===== SISTEMA SOFTWARE FJ =====")

# Primera prueba válida
try:

    cliente1 = Cliente("Maria", "maria@gmail.com")

    servicio1 = ReservaSala("Sala VIP", 50000, 2)

    reserva1 = Reserva(cliente1, servicio1)

    reserva1.confirmar()

    print(reserva1.mostrar_reserva())

except Exception as e:

    print("Error:", e)

    logging.error(e)

# Segunda prueba inválida
try:

    cliente2 = Cliente("", "correo.com")

except Exception as e:

    print("Error:", e)

    logging.error(e)

# Tercera prueba inválida
try:

    servicio2 = AlquilerEquipo("Computador", -20000, 3)

except Exception as e:

    print("Error:", e)

    logging.error(e)

# Mensaje final del sistema
print("El sistema sigue funcionando correctamente")