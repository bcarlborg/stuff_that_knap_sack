import unittest
from PersonTestClass import Person

class PersonTests(unittest.TestCase):
	def test_one(self):
		paul = Person(name="paul", age=10, last_name="pete", eye_color="blue")
		self.assertEqual(paul.get_age(), 10)

if __name__ == '__main__':
    unittest.main()
