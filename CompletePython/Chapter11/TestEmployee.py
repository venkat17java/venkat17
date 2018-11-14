import unittest
from Employee import Employee 

class GiveRaiseTestCase(unittest.TestCase):
	
	def setUp(self):	
		self.e1 = Employee("venkat", "jalaneela", 5000)
	
	def test_default_raise(self):
		self.e1.give_raise()
		self.assertEqual(10000,self.e1.annualsalary)
		
	def test_give_custom_raise(self):
		self.e1.give_raise(7000)
		self.assertEqual(12000,self.e1.annualsalary)
		