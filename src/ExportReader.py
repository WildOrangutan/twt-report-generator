from typing import Iterable
from src.Event import Event
from src.EventParser import EventParser


class ExportReader:

    def __init__(self, fileLineIterator: Iterable[str]):
        self._fileLineIterator = fileLineIterator
        self._initEventParser()
    
    def _initEventParser(self):
        headerLine = next(self._fileLineIterator)
        self.eventParser = EventParser(headerLine)

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self._fileLineIterator)
        event = self.eventParser.parse(line)
        return event
