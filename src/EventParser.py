from datetime import datetime
from src.ParseError import ParseError
from src.Event import Event
from src.EventType import EventType
from src.Task import Task


class EventParser:

    _DELIMITER = ";"
    _COLUMN_DATETIME = "time"
    _COLUMN_EVENT_TYPE = "type"
    _COLUMN_TASK = "task"

    _indexDatetime = -1
    _indexEventType = -1
    _indexTask = -1

    def __init__(self, header: str):
        self._initColumnIndexes(header)
        
    def _initColumnIndexes(self, header):
        # Example header: "time;type;task;text"
        headers = self._splitString(header)
        self._indexDatetime = self._getHeaderIndex(headers, self._COLUMN_DATETIME)
        self._indexEventType = self._getHeaderIndex(headers, self._COLUMN_EVENT_TYPE)
        self._indexTask = self._getHeaderIndex(headers, self._COLUMN_TASK)

    def _getHeaderIndex(self, headers, header):
        try:
            return headers.index(header)
        except ValueError as e:
            raise ParseError(f"Header '{header}' not found in '{headers}'") from e

    def parse(self, eventString: str) -> Event:
        # Example event string: "2020-01-06 08:18;in;Default;"
        strings = self._splitString(eventString)
        dateTime = self._parseDate(strings[self._indexDatetime])
        eventType = EventType.parse(strings[self._indexEventType])
        task = Task.parse(strings[self._indexTask])
        return Event(datetime=dateTime, eventType=eventType, task=task)

    def _splitString(self, string):
        values = string.split(self._DELIMITER)
        self._validateStringParts(values)
        return values

    def _validateStringParts(self, values):
        actualLength = len(values)
        expectedLength = 3
        if actualLength==0 or actualLength < expectedLength:
            msg = f"Expected at least {expectedLength} string parts, found {actualLength}"
            raise ParseError(msg)

    def _parseDate(self, string):
        dateTimeFormat = "%Y-%m-%d %H:%M"
        try:
            return datetime.strptime(string, dateTimeFormat)
        except Exception as e:
            raise ParseError(f"Failed to parse date from '{string}'") from e
