import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

COMPANIES_HOST = os.getenv('BROKER_HOST', default="localhost")

def obtener_usuarios(root) -> typing.List["Usuario"]:
    usuarios_json = requests.get(f'http://{COMPANIES_HOST}:5005/').json()
    usuarios = []

    for usuario in usuarios_json:
        usuarios.append(
            Usuario(
                id=usuario.get('id'),
                nombre=usuario.get('nombre'),
                correo=usuario.get('correo'),
                contraseña=usuario.get('contraseña')
            )
        )

    return usuarios

@strawberry.type
class Usuario:
    id: str
    nombre: str
    correo: str
    contraseña: str


