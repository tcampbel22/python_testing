# # Test file for the sum function
import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
	def test_list_int(self):
		data = [1, 2, 3]
		result = sum(data)
		self.assertEqual(result, 6)
	def test_list_fraction(self):
		data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
		result = sum(data)
		self.assertEqual(result, 1)
	def test_bad_type(self):
		data = [1, 2, 3]
		with self.assertRaises(TypeError):
			result = sum(data)
	# def test_sum(self):
	# 	self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

	# def test_sum_tuple(self):
	# 	self.assertEqual(sum((1, 2, 2)), 6, "Should be 6)")

if __name__ == "__main__":
	unittest.main()