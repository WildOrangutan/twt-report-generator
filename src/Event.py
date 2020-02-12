from datetime import datetime
from dataclasses import dataclass
from src.EventType import EventType
from src.ParseError import ParseError

@dataclass
class Event:
    datetime: datetime
    eventType: EventType

    @classmethod
    def parse(self, string):
        # 2020-01-06 08:18;in;Default;
        values = self.__splitString(self, string)
        dateTime = self.__parseDate(self, values[0])
        eventType = EventType.parse(values[1])
        return self(datetime=dateTime, eventType=eventType)

    def __splitString(self, string):
        values = string.split(';')
        length = len(values)
        if length==0 or length < 2:
            raise ParseError(f"Expected at least 2 string parts, found {length}")
        return values

    def __parseDate(self, string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        return datetime.strptime(string, dateTimeFormat)

        



