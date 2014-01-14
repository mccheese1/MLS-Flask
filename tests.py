import os
import unittest

from app import app

class TestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['CSRF_ENABLED'] = False
		self.app = app.test_client()


	def tearDown(self):
		pass


	def test_example(self):
		assert True = True
		

if __name__ == '__main__':
    unittest.main()