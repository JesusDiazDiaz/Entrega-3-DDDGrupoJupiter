from dataclasses import dataclass, field

from .entity import Entity
from .event import IntegrationEvent , DomainEvent


@dataclass
class AggregateRoot(Entity):
    """

    """

    events: list[DomainEvent] = field(init=False, default_factory=list)

    def add_event(self, event: IntegrationEvent) -> None:
        self.events.append(event)

    def remove_event(self, event: IntegrationEvent) -> None:
        self.events.remove(event)