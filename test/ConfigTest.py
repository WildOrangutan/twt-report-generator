from src.Config import Config
from unittest import TestCase


class ConfigTest(TestCase):

    def testFullNameValidation(self):
        Config("Super Mario")

        with self.assertRaises(ValueError):
            Config(None)

        with self.assertRaises(ValueError):
            Config("")

        with self.assertRaises(ValueError):
            Config(" ")