import unittest
from src.EventType import EventType

class ExportReaderTest(unittest.TestCase):

    def testIn(self):
        typeIn = EventType("in")
        self.assertEquals(typeIn, EventType.IN)

    def testOut(self):
        typeOut = EventType("out")
        self.assertEquals(typeOut, EventType.OUT)

