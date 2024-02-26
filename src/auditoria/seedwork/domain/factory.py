from abc import abstractmethod, ABC
from .repository import Mapper


class Factory(ABC):
    @abstractmethod
    def update(self, obj: any, mapper: Mapper=None):
        ...