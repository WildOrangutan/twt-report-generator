from typing import Iterable
from src.Event import Event

class ExportReader:

    def __init__(self, fileLineIterator: Iterable[str]):
        self.fileLineIterator = fileLineIterator
        next(fileLineIterator) # Skip header

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.fileLineIterator)
        event = Event.parse(line)
        return event
