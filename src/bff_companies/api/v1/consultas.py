import strawberry
from .esquemas import *

@strawberry.type
class Query:
    usuarios: typing.List[Usuario] = strawberry.field(resolver=obtener_usuarios)

