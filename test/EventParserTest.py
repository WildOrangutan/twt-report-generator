from unittest import TestCase
from datetime import datetime
from src.Event import Event
from src.ParseError import ParseError
from src.EventParser import EventParser
from src.EventType import EventType


class EventParserTest(TestCase):

    def testInvalidHeader(self):
        header = "monkeys;love;bananas;"
        
        with self.assertRaises(ParseError):
            EventParser(header)

    def testParse(self):
        header = "time;type;task;text"
        event = "2000-01-02 03:04;in;Hello;"
        eventParser = EventParser(header)

        actualEvent = eventParser.parse(event)

        expectedDate = datetime(year=2000, month=1, day=2, hour=3, minute=4)
        expectedType = EventType.IN
        expectedEvent = Event(datetime=expectedDate, eventType=expectedType)
        self.assertEqual(actualEvent, expectedEvent)
