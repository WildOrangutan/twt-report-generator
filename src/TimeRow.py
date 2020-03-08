from dataclasses import dataclass
from typing import List


@dataclass
class TimeRow:
    rowValues: List[str]

    def columnCount(self):
        return len(self.rowValues)

    @classmethod
    def fromValues(cls, *rowValues: str):
        return cls(list(rowValues))
    