from src.properties.seedwork.application.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from src.properties.seedwork.application.commands import Comando
from src.properties.seedwork.domain.event import EventoDominio

from src.properties.modules.sagas.application.commands.auditoria import RegistrarUsuario, ValidarUsuario
from src.properties.modules.sagas.application.commands.pagos import PagarReserva, RevertirPago
from src.properties.modules.sagas.application.commands.gds import ConfirmarReserva, RevertirConfirmacion
from src.properties.modules.sagas.application.commands.comandos.crear_reserva import CrearReserva
from src.properties.modules.sagas.application.commands.aprobar_reserva import AprobarReserva
from src.properties.modules.sagas.application.commands.cancelar_reserva import CancelarReserva
from src.properties.modules.vuelos.dominio.eventos.reservas import ReservaCreada, ReservaCancelada, ReservaAprobada, \
    CreacionReservaFallida, AprobacionReservaFallida
from src.properties.modules.sagas.domain.events.pagos import ReservaPagada, PagoRevertido
from src.properties.modules.sagas.domain.events.gds import ReservaGDSConfirmada, ConfirmacionGDSRevertida, \
    ConfirmacionFallida


class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearReserva, evento=ReservaCreada, error=CreacionReservaFallida,
                        compensacion=CancelarReserva),
            Transaccion(index=2, comando=PagarReserva, evento=ReservaPagada, error=PagoFallido,
                        compensacion=RevertirPago),
            Transaccion(index=3, comando=ConfirmarReserva, evento=ReservaGDSConfirmada, error=ConfirmacionFallida,
                        compensacion=ConfirmacionGDSRevertida),
            Transaccion(index=4, comando=AprobarReserva, evento=ReservaAprobada, error=AprobacionReservaFallida,
                        compensacion=CancelarReserva),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de domain
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")