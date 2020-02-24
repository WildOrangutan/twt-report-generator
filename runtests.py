from unittest import TestLoader, TextTestRunner


loader = TestLoader()
suite = loader.discover(start_dir="test/", pattern="*Test.py")
runner = TextTestRunner(verbosity=2)

result = runner.run(suite)

success = result.wasSuccessful()
exitCode = 0 if success else 1
exit(exitCode)