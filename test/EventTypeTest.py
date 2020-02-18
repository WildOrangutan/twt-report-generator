import unittest
from src.EventType import EventType


class ExportReaderTest(unittest.TestCase):

    def testIn(self):
        typeIn = EventType.parse(" in ")
        self.assertEquals(typeIn, EventType.IN)

    def testOut(self):
        typeOut = EventType.parse(" out ")
        self.assertEquals(typeOut, EventType.OUT)

