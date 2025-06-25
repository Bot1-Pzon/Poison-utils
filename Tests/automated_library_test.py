'''
	Test automatici della libreria Poison_utils.
'''

import os
import sys
import random

import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from Poison_utils import Console, Files, Lists, Math, Physics, Web_kit


class Console_Tests(unittest.TestCase):

	""" def test_clear(self):
		''' test if clear method runs without errors '''
		try:
			Console.clear()
		except Exception as screen_cleaning_error:
			self.fail(f"Console.clear() raised: \"{screen_cleaning_error}\"") """


	def stop_test(self):
		''' Test della funzione di arresto del programma. '''
		with self.assertRaises(SystemExit):
			Console.stop()


class Files_Tests(unittest.TestCase):

	""" Verify the existence of a file and its path. """

	def path_existence_test(self):
		self.assertTrue(Files.path_exist(__file__))
		self.assertFalse(Files.path_exist("non_existent_file.txt"))


class Lists_Tests(unittest.TestCase):

	def random_list_creation_test(self):

		maximum_list_length: int = random.randint(1, 100)
		minimum_list_length: int = random.randint(0, maximum_list_length)
		minimum_value: int = random.randint(0, 99)
		maximum_value: int = random.randint(minimum_value, 99)

		random_list = Lists.create_random_list(
			list_length_range = (minimum_list_length, maximum_list_length),
			values_range = (minimum_value, maximum_value)
		)

		self.assertTrue(minimum_list_length <= len(random_list) <= maximum_list_length)
		self.assertTrue(all(minimum_value <= x <= maximum_value for x in random_list))


	def bubble_sort_test(self):
		sorted_list = Lists.bubble_sort([3, 2, 1])
		self.assertEqual(sorted_list, [1, 2, 3])


	def test_duplicates_counter(self):
		counter = Lists.duplicates_counter([1, 2, 2, 3, 3, 3])
		self.assertEqual(counter, {1: 1, 2: 2, 3: 3})


class Math_Test(unittest.TestCase):

	def test_factorial(self):
		self.assertEqual(Math.factorial(5), 120)
		self.assertEqual(Math.factorial(0), 1)


	def test_fibonacci(self):
		self.assertEqual(Math.fibonacci(10), 34)
		self.assertEqual(Math.fibonacci(1), 1)


	def test_is_prime(self):
		self.assertTrue(Math.is_prime(7))
		self.assertFalse(Math.is_prime(4))


class Physics_Tests(unittest.TestCase):

	def test_measure_addition(self):
		m1 = Physics.Measure(10, 0.5, 'm')
		m2 = Physics.Measure(5, 0.2, 'm')
		result = m1 + m2
		self.assertEqual(result.measure, 15)
		self.assertEqual(result.uncertainty, 0.7)



if __name__ == '__main__':
	unittest.main()
