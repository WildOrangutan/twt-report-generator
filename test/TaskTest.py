from unittest import TestCase
from src.Task import Task


class TaskTest(TestCase):

    def testWorkday(self):
        actualTask = Task.parse(" Holiday ")
        expectedTask = Task.HOLIDAY
        self.assertEqual(actualTask, expectedTask)

    def testHoliday(self):
        actualTask = Task.parse(" Work ")
        expectedTask = Task.WORK
        self.assertEqual(actualTask, expectedTask)
