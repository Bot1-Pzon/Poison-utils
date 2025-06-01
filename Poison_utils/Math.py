'''
	Funzionalità per l'implementazione di varie funzioni matematiche.
'''


import math

from typing import Tuple

from Poison_utils import Console


@staticmethod
def factorial(n: int) -> int:
	''' Ritorna il fattoriale del numero dato. '''

	if n < 0:
		Console.Logs.error(f"Il fattoriale di \"{n} < 0\" non é supportato")

	r: int = 1
	for i in range(1, n + 1):
		r *= i
	return r


@staticmethod
def fibonacci(n: int) -> int:
	''' Ritorna l'n-esimo numero nella sequenza di Fibonacci. '''

	if n <= 0:
		return 0

	elif n == 1:
		return 1

	else:
		a, b = 0, 1

		for _ in range(n - 2):
			a, b = b, (a + b)

		return b


@staticmethod
def is_prime(n: int) -> bool:
	''' Ritorna vero se un numero è primo. '''

	if n < 2:
		return False

	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False

	return True


class Point:
	''' '''

	def __init__(self, x_: float = None, y_: float = None, /, *, coordinates: Tuple[float, float] = None,) -> None:

		if coordinates is not None and (x_ is None or y_ is None):
			self.x = coordinates[0]
			self.y = coordinates[1]

		elif (x_ is not None and y_ is not None) and coordinates is None:
			self.x = x_
			self.y = y_

		else:
			Console.Logs.fatal_error("Devi specificare le coordinate del punto")

	def __str__(self) -> str:
		return f"Point({self.x}, {self.y})"

	@staticmethod
	def calculate_distance(first_point: 'Point', second_point: 'Point') -> float:
		''' Calcala la distanza tra due punti. '''

		return math.dist((first_point.x, first_point.y), (second_point.x, second_point.y))


O: Point = Point(coordinates = (0, 0))


class Vector:
	'''  '''
	def __init__(self, origin: Tuple[int, int] | 'Point', module: float, direction: float):
		self.origin: 'Point' = Point(origin)

		if direction > 360:
			direction =  math.radians(direction / 360 + direction % 360)

		self.direction: float = direction
		self.module: float = module

		if self.direction < 0:
			self.x = self.module * math.cos(self.direction)
			self.y = self.module * math.sin(self.direction)

		elif self.direction == 0:
			self.x = self.module
			self.y = 0

		elif self.direction > 0:
			self.x = self.module * math.sin(self.direction)
			self.y = self.module * math.cos(self.direction)


	def __add__(self, other: 'Vector') -> 'Vector':
		''' Somma due vettori. '''

		resulting_x = self.x + other.x
		resulting_y = self.y + other.y
		resulting_module = math.sqrt(resulting_x ** 2 + resulting_y ** 2)
		resulting_direction = math.degrees(math.atan2(resulting_y, resulting_x))

		return Vector (
			origin = self.origin,
			direction = resulting_direction,
			module = resulting_module
		)
