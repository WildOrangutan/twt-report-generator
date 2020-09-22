from src.TimeRow import TimeRow
from dataclasses import dataclass
from typing import Iterable


@dataclass
class TimeTable:
    timeRows: Iterable[TimeRow]
    _columnCount = -1

    def __post_init__(self):
        self._initColumnCount()
        self._validateRows()

    def _initColumnCount(self):
        for timeRow in self.timeRows:
            self._columnCount = timeRow.columnCount()
            return
        raise RuntimeError("No timeRows to get column count from")
    
    def _validateRows(self):
        for timeRow in self.timeRows:
            self._validateRow(timeRow)

    def _validateRow(self, timeRow):
        expectedColumns = self._columnCount
        actualColumns = timeRow.columnCount()
        if expectedColumns != actualColumns:
            raise ValueError(f"Column count mismatch. Expected {expectedColumns}, \
                    found {actualColumns}.")
