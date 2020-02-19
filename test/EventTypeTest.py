from unittest import TestCase
from src.EventType import EventType


class EventTypeTest(TestCase):

    def testIn(self):
        typeIn = EventType.parse(" in ")
        self.assertEqual(typeIn, EventType.IN)

    def testOut(self):
        typeOut = EventType.parse(" out ")
        self.assertEqual(typeOut, EventType.OUT)

