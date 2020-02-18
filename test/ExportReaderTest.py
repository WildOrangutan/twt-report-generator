import unittest
from datetime import datetime
from src.Event import Event
from src.EventType import EventType
from src.ExportReader import ExportReader


class ExportReaderTest(unittest.TestCase):

    def iterator(self):
        eventLines = ["time;type;task;text", "2000-01-02 03:04;in;Hello;",
                "3000-02-03 04:05;out;World;"]
        lineIter = iter(eventLines)

        reader = ExportReader(lineIter)

        self.assertEquals(
            Event(
                datetime=datetime(year=2000, month=1, day=2, hour=3, minute=4),
                eventType=EventType.IN
            ),
            next(reader)
        )
        self.assertEquals(
            Event(
                datetime=datetime(year=3000, month=2, day=3, hour=4, minute=5),
                eventType=EventType.OUT
            ),
            next(reader)
        )
        with self.assertRaises(StopIteration):
            next(reader)

