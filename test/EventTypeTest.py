from unittest import TestCase
from src.EventType import EventType


class ExportReaderTest(TestCase):

    def testIn(self):
        typeIn = EventType.parse(" in ")
        self.assertEquals(typeIn, EventType.IN)

    def testOut(self):
        typeOut = EventType.parse(" out ")
        self.assertEquals(typeOut, EventType.OUT)

