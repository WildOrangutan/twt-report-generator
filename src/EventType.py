from enum import Enum
from src.ParseError import ParseError


class EventType(Enum):
    IN = "in"
    OUT = "out"

    @classmethod
    def parse(cls, string):
        try:
            cleanString = string.strip()
            return cls(cleanString)
        except Exception as e:
            raise ParseError(f"Failed to parse from '{cleanString}'") from e
