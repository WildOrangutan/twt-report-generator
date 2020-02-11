from datetime import datetime
from dataclasses import dataclass
from src.EventType import EventType

@dataclass
class Event:
    datetime: datetime
    eventType: EventType

    @classmethod
    def parse(self, string):
        # 2020-01-06 08:18;in;Default;
        values = string.split(';')
        dateTime = self.__parseDate(self, values[0])
        eventType = EventType(values[1])
        return self(datetime=dateTime, eventType=eventType)

    def __parseDate(self, string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        return datetime.strptime(string, dateTimeFormat)

        



