from src.properties.seedwork.application.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from src.properties.seedwork.application.commands import Command
from src.properties.seedwork.domain.event import DomainEvent

from src.properties.modules.sagas.application.commands.properties import PropertiesRegistry, PropertiesDeactivate
from src.properties.modules.sagas.application.commands.pipeline import ValidationRegister, ValidationDeactivate
from src.properties.modules.sagas.application.commands.auditoria import EnrichmentRegister, EnrichmentDeactivate


class CoordinadorIngesta(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CreateDatalakeFile, evento=DatalakeFileCreated, error=DatalakeFileFailed,
                        compensacion=DatalakeFileCanceled),
            Transaccion(index=2, comando=CreateValidation, evento=DataValidationCreated, error=DataValidationFailed,
                        compensacion=DataValidationCanceled),
            Transaccion(index=3, comando=CreateEnrichment, evento=DataEnrichmentCreated, error=DataEnrichmentFailed,
                        compensacion=DataEnrichmentCanceled),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: DomainEvent, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de domain
def oir_mensaje(mensaje):
    if isinstance(mensaje, DomainEvent):
        coordinador = CoordinadorIngesta()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")