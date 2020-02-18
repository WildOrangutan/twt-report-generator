from datetime import datetime
from src.ParseError import ParseError
from src.Event import Event
from src.EventType import EventType


class EventParser:

    __DELIMITER = ";"
    __COLUMN_DATETIME = "time"
    __COLUMN_EVENT_TYPE = "type"

    __indexDatetime = -1
    __indexEventType = -1

    def __init__(self, header: str):
        self.__initColumnIndexes(header)
        
    def __initColumnIndexes(self, header):
        # Example header: "time;type;task;text"
        headers = self.__splitString(header)
        __indexDatetime = headers.index(self.__COLUMN_DATETIME)
        __indexEventType = headers.index(self.__COLUMN_EVENT_TYPE)

    def parse(self, eventString: str) -> Event:
        # Example event string: "2020-01-06 08:18;in;Default;"
        strings = self.__splitString(eventString)
        dateTime = self.__parseDate(strings[0])
        eventType = EventType.parse(strings[1])
        return Event(datetime=dateTime, eventType=eventType)

    def __splitString(self, string):
        values = string.split(self.__DELIMITER)
        length = len(values)
        if length==0 or length < 2:
            raise ParseError(f"Expected at least 2 string parts, found {length}")
        return values

    def __parseDate(self, string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        try:
            return datetime.strptime(string, dateTimeFormat)
        except Exception as e:
            raise ParseError(f"Failed to parse date from '{string}'") from e
