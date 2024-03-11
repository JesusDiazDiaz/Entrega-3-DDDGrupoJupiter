from abc import ABC

from src.pipeline.seedwork.domain.repository import Repository


class PropertyRepository(Repository, ABC):
    ...