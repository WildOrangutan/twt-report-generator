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
        # Example string: 2020-01-06 08:18;in;Default;
        values = self.__splitString(string)
        dateTime = self.__parseDate(values[0])
        eventType = EventType.parse(values[1])
        return self(datetime=dateTime, eventType=eventType)

    @staticmethod
    def __splitString(string):
        values = string.split(';')
        length = len(values)
        if length==0 or length < 2:
            raise ParseError(f"Expected at least 2 string parts, found {length}")
        return values

    @staticmethod
    def __parseDate(string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        try:
            return datetime.strptime(string, dateTimeFormat)
        except Exception as e:
            raise ParseError(f"Failed to parse date from '{string}'") from e

        



