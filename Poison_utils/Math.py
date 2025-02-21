'''
	Funzionalità per l'implementazione di varie funzioni matematiche.
'''


from Poison_utils import Console


@staticmethod
def factorial(n: int) -> int:
	''' Ritorna il fattoriale del numero dato. '''

	if n < 0:
		Console.Logs.fatal_error(f'Il fattoriale di un {n} < 0 non é supportato')

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
