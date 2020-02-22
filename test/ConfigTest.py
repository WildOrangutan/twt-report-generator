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
    
    def testParseYaml(self):
        yaml = '''
        fullname: Batman
        '''
        # Atm it's fine if no error is raised
        Config.parseYaml(yaml)