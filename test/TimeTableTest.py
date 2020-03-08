from unittest import TestCase
from src.TimeRow import TimeRow
from src.TimeTable import TimeTable


class TimeTableTest(TestCase):

    def testInvalidRows(self):
        timeRows = [
            TimeRow.fromValues("1", "2"),
            TimeRow.fromValues("3"),
        ]

        with self.assertRaises(ValueError):
            TimeTable(timeRows)

    def testNoRows(self):
        timeRows = []

        with self.assertRaises(RuntimeError):
            TimeTable(timeRows)

    def testSingleRow(self):
        timeRows = [
            TimeRow.fromValues("foreverSingleRow"),
        ]

        TimeTable(timeRows)

    def testMultipleRows(self):
        timeRows = [
            TimeRow.fromValues("a", "b"),
            TimeRow.fromValues("1", "2"),
        ]

        TimeTable(timeRows)