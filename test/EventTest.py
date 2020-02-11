import unittest
from src.Event import Event
from src.EventType import EventType
from datetime import datetime

class EventTest(unittest.TestCase):

    def testParse(self):
        string = "2020-01-06 08:18;in;Default;"

        actualEvent = Event.parse(string)

        expectedDate = datetime(year=2020, month=1, day=6, hour=8, minute=18)
        expectedType = EventType.IN
        expectedEvent = Event(datetime=expectedDate, eventType=expectedType)

        self.assertEquals(actualEvent, expectedEvent)

