from dataclasses import dataclass, field

from .entity import Entity
from .event import DomainEvent


@dataclass
class AggregateRoot(Entity):
    """Aggregate root base class.

    Attributes:
        events: A list of events that have occurred in the aggregate root.

    See Also:
        - https://martinfowler.com/bliki/DDD_Aggregate.html

    """

    events: list[DomainEvent] = field(init=False, default_factory=list)

    def add_event(self, event: DomainEvent) -> None:
        self.events.append(event)

    def remove_event(self, event: DomainEvent) -> None:
        self.events.remove(event)