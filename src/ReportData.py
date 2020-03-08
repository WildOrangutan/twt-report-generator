from dataclasses import dataclass
from typing import IO
from src.TimeTable import TimeTable


@dataclass
class ReportData:
    name: str
    date: str
    fileOutputStream: IO
    timeTable: TimeTable
    workDaysCount: int
    holidaysCount: int
    publicHolidaysCount: int
    sickDaysCount: int
