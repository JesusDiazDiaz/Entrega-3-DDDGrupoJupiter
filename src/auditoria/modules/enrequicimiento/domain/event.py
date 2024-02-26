from dataclasses import dataclass, field
from datetime import datetime

from src.auditoria.seedwork.domain.event import DomainEvent


@dataclass
class InformationUpdated(DomainEvent):
    updated_at: datetime = None
