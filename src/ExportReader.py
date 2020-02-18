from typing import Iterable
from src.Event import Event
from src.EventParser import EventParser

class ExportReader:

    def __init__(self, fileLineIterator: Iterable[str]):
        self.__fileLineIterator = fileLineIterator
        self.__initEventParser()
    
    def __initEventParser(self):
        headerLine = next(self.__fileLineIterator)
        self.eventParser = EventParser(headerLine)

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.__fileLineIterator)
        event = self.eventParser.parse(line)
        return event
