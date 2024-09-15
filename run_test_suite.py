import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

all_tests = loader.discover('tests', pattern='test_*.py')

suite.addTests(all_tests)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
