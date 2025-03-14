'''
	Funzionalità per la gestione di liste.
'''


import random
from typing import Any, Union, Tuple


def create_random_list(list_length_range: Union[Tuple[int, 1 | 2], int] = (), values_range: Union[Tuple[int, 1 | 2], int] = ()) -> list[int]:
	'''
		Restituisce una lista casuale di interi dalla lunghezza casuale e dal range di valori specificato specificato.

		Se non viene specificato un range ma una cifra intera, si tratterà il range tra valore predefiniti.

		Se non viene specificato il range di lunghezza, la lista avrà una lunghezza casuale tra 1 e 1000.
		Se non viene specificato il range di valori, i valori saranno compresi tra 0 e 99.
	'''

	list_length: int
	minimum_value: int
	maximum_value: int

	if type(list_length_range) == int:
		if list_length_range <= 0:
			raise ValueError("list_length_range deve essere un intero positivo.")

		list_length = random.randint(0, list_length_range)


	elif type(list_length_range) == tuple:

		if list_length_range == ():
			list_length = random.randint(1, 1000)

		elif len(list_length_range) == 1:
			list_length = list_length_range[0]

		elif len(list_length_range) == 2:

			if list_length_range[0] <= 0:
				raise ValueError("list_length_range deve essere un intero positivo.")

			if list_length_range[0] >= list_length_range[1]:
				raise ValueError("Il primo valore di list_length_range deve essere minore al secondo.")

			list_length = random.randint(list_length_range[0], list_length_range[1])

		else:
			raise ValueError("list_length_range deve essere una tupla di 1 o 2 elementi.")

	else:
		raise ValueError("list_length_range deve essere un intero o una tupla.")

	if type(values_range) == int:

		minimum_value = 0
		maximum_value = values_range

	elif type(values_range) == tuple:

		if values_range == ():
			minimum_value = 0
			maximum_value = 99

		elif len(values_range) == 1:
			minimum_value = 0
			maximum_value = values_range[0]

		elif len(values_range) == 2:

			if values_range[0] >= values_range[1]:
				raise ValueError("Il primo valore di values_range deve essere minore al secondo.")

			minimum_value = values_range[0]
			maximum_value = values_range[1]

		else:
			raise ValueError("values_range deve essere una tupla di 1 o 2 elementi.")

	else:
		raise ValueError("values_range deve essere un intero o una tupla.")

	random_list: list[int] = []

	for _ in range(list_length):
		random_list.append(random.randint(minimum_value, maximum_value))	#* Inserimento nella lista casuale.

	return random_list


def bubble_sort(List: list[int]) -> list[int]:
	'''
		Riordina la list data.\n
		Complessita temporale inefficiente (O(n²)).
	'''

	for i in range(len(List) - 1):
		for j in range(len(List) - i - 1):
			if List[j] > List[j + 1]:
				List[j], List[j + 1] = List[j + 1], List[j]	#* Scambio del valore minore con il successivo.
	return List


def jenky_sort(List: list[int]) -> list[int]:
	''' '''

	swap: bool = True
	while swap is True:	# Mentre è stato effettuato uno scambio:
		swap = False

		for i in range(len(List) - 1):
			if List[i] > List[i + 1]:
				List[i], List[i + 1] = List[i + 1], List[i]	#* Scambio del valore minore con il successivo.
				swap = True

	return List


def duplicates_counter(list_to_count: list[Any]) -> dict[Any, int]:
	'''
		Ritorna un dizionario come chiavi i vari elementi della lista data e come valori il numero di occorrenze.
	'''

	counter: dict[None: int] = {}

	for element in list_to_count:
		if element in counter:
			counter[element] += 1	#* Incremento del valore del contatore
		else:
			counter[element] = 1	#* Inserimento di un nuovo valore nel contatore

	return counter
