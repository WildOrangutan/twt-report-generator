from datetime import datetime
from dataclasses import dataclass
from src.EventType import EventType
from src.ParseError import ParseError


@dataclass
class Event:
    datetime: datetime
    eventType: EventType
