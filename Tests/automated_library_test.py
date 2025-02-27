'''
	Test automatici della libreria Poison_utils.
'''

import sys

sys.path.append('/home/poison_8o8/Pr0gr4ms/Projects/Poison-utils')

import unittest
from Poison_utils import Console, Files, Lists, Math, Physics, Web_kit


class Console_Test(unittest.TestCase):

	def test_clear(self):
		# Test if clear method runs without error
		try:
			Console.clear()
		except Exception as screen_cleaning_error:
			self.fail(f"Console.clear() raised: \"{screen_cleaning_error}\"")


	def test_stop(self):
		''' Test della funzione di arresto del programma. '''
		with self.assertRaises(SystemExit):
			Console.stop()


class Files_test(unittest.TestCase):

	def test_path_exist(self):
		self.assertTrue(Files.path_exist(__file__))
		self.assertFalse(Files.path_exist("non_existent_file.txt"))


class Lists_Test(unittest.TestCase):

	def test_create_random_list(self):
		random_list = Lists.create_random_list(10, 1, 10)
		self.assertEqual(len(random_list), 10)
		self.assertTrue(all(1 <= x <= 10 for x in random_list))


	def test_bubble_sort(self):
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


class Physics_Test(unittest.TestCase):

	def test_measure_addition(self):
		m1 = Physics.Measure(10, 0.5, 'm')
		m2 = Physics.Measure(5, 0.2, 'm')
		result = m1 + m2
		self.assertEqual(result.measure, 15)
		self.assertEqual(result.uncertainty, 0.7)


""" class TestWebKit(unittest.TestCase):

	def test_config(self):
		try:
			Web_kit.config(statics_path='statics')
		except Exception as e:
			self.fail(f"Web_kit.config() raised {e}") """


if __name__ == '__main__':
	unittest.main()
