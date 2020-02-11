from enum import Enum

class EventType(Enum):
    IN = "in"
    OUT = "out"

    @classmethod
    def parse(self, string):
        return self(string.strip())
