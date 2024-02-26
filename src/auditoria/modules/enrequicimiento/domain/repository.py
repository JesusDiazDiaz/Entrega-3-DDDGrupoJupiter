from abc import ABC

from src.auditoria.seedwork.domain.repository import Repository


class PropertyRepository(Repository, ABC):
    ...