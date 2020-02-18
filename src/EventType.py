from enum import Enum
from src.ParseError import ParseError


class EventType(Enum):
    IN = "in"
    OUT = "out"

    @classmethod
    def parse(self, string):
        try:
            cleanString = string.strip()
            return self(cleanString)
        except Exception as e:
            raise ParseError(f"Failed to parse from '{cleanString}'") from e
