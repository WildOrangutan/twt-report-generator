from unittest import TestCase
from datetime import datetime
from src.Event import Event
from src.EventType import EventType
from src.ExportReader import ExportReader
from src.Task import Task


class ExportReaderTest(TestCase):

    def testIterator(self):
        eventLines = ["time;type;task;text", "2000-01-02 03:04;in;Work;",
                "3000-02-03 04:05;out;Holiday;"]
        lineIter = iter(eventLines)

        reader = ExportReader(lineIter)

        self.assertEqual(
            Event(
                datetime=datetime(year=2000, month=1, day=2, hour=3, minute=4),
                eventType=EventType.IN,
                task=Task.WORK
            ),
            next(reader)
        )
        self.assertEqual(
            Event(
                datetime=datetime(year=3000, month=2, day=3, hour=4, minute=5),
                eventType=EventType.OUT,
                task=Task.HOLIDAY
            ),
            next(reader)
        )
        with self.assertRaises(StopIteration):
            next(reader)

