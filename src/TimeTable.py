from src.TimeRow import TimeRow
from dataclasses import dataclass
from typing import Iterable


@dataclass
class TimeTable:
    timeRows: Iterable[TimeRow]
    __columnCount = -1

    def __post_init__(self):
        self.__initColumnCount()
        self.__validateRows()

    def __initColumnCount(self):
        for timeRow in self.timeRows:
            self.__columnCount = timeRow.columnCount()
            return
        raise RuntimeError("No timeRows to get column count from")
    
    def __validateRows(self):
        for timeRow in self.timeRows:
            self.__validateRow(timeRow)

    def __validateRow(self, timeRow):
        expectedColumns = self.__columnCount
        actualColumns = timeRow.columnCount()
        if expectedColumns != actualColumns:
            raise ValueError(f"Column count mismatch. Expected {expectedColumns}, \
                    found {actualColumns}.")
