from datetime import datetime
from src.ParseError import ParseError
from src.Event import Event
from src.EventType import EventType
from src.Task import Task


class EventParser:

    __DELIMITER = ";"
    __COLUMN_DATETIME = "time"
    __COLUMN_EVENT_TYPE = "type"
    __COLUMN_TASK = "task"

    __indexDatetime = -1
    __indexEventType = -1
    __indexTask = -1

    def __init__(self, header: str):
        self.__initColumnIndexes(header)
        
    def __initColumnIndexes(self, header):
        # Example header: "time;type;task;text"
        headers = self.__splitString(header)
        self.__indexDatetime = self.__getHeaderIndex(headers, self.__COLUMN_DATETIME)
        self.__indexEventType = self.__getHeaderIndex(headers, self.__COLUMN_EVENT_TYPE)
        self.__indexTask = self.__getHeaderIndex(headers, self.__COLUMN_TASK)

    def __getHeaderIndex(self, headers, header):
        try:
            return headers.index(header)
        except ValueError as e:
            raise ParseError(f"Header '{header}' not found in '{headers}'") from e

    def parse(self, eventString: str) -> Event:
        # Example event string: "2020-01-06 08:18;in;Default;"
        strings = self.__splitString(eventString)
        dateTime = self.__parseDate(strings[self.__indexDatetime])
        eventType = EventType.parse(strings[self.__indexEventType])
        task = Task.parse(strings[self.__indexTask])
        return Event(datetime=dateTime, eventType=eventType, task=task)

    def __splitString(self, string):
        values = string.split(self.__DELIMITER)
        self.__validateStringParts(values)
        return values

    def __validateStringParts(self, values):
        actualLength = len(values)
        expectedLength = 3
        if actualLength==0 or actualLength < expectedLength:
            msg = f"Expected at least {expectedLength} string parts, found {actualLength}"
            raise ParseError(msg)

    def __parseDate(self, string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        try:
            return datetime.strptime(string, dateTimeFormat)
        except Exception as e:
            raise ParseError(f"Failed to parse date from '{string}'") from e
