import strawberry
import typing

from strawberry.types import Info
from bff_companies import utils
from bff_companies.dispatchers import Dispatch

from .esquemas import *


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_usuario(self, nombre: str, correo: str, contraseña: str, info: Info) -> UsuarioRespuesta:
        print(f"Nombre: {nombre}, Correo: {correo}, Contraseña: {contraseña}")
        payload = dict(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña
        )
        comando = dict(
            id=str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion="v1",
            type="ComandoCrearUsuario",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name="bff companies",
            data=payload
        )
        despachador = Dispatch()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-usuario",
                                                  "public/default/comando-crear-usuario")

        return UsuarioRespuesta(mensaje="Procesando Mensaje", codigo=203)
