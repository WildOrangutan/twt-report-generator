import unittest


loader = unittest.TestLoader()
suite = loader.discover(start_dir="test/", pattern="*Test.py")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)