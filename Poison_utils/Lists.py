'''
    Funzionalità per la gestione di liste.
'''


import random
from typing import Any


@staticmethod
def create_random_list(list_length: int = None, minimum_value: int = 0, maximum_value: int = 999) -> list[int]:
    ''' Restituisce una lista casuale di interi dalla lunghezza e dal range di valori specificato specificato. '''

    if list_length is None:
        list_length = random.randint(1, 500)

    random_list: list[int] = []

    for _ in range(list_length):
        random_list.append(random.randint(minimum_value, maximum_value))	#* Inserimento nella lista casuale.

    return random_list


@staticmethod
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


@staticmethod
def jenky_sort(List: list[int]) -> list[int]:
    ''' '''

    swap: bool = True
    while swap is True:	#* Mentre è stato effettuato uno scambio:
        swap = False

        for i in range(len(List) - 1):
            if List[i] > List[i + 1]:
                List[i], List[i + 1] = List[i + 1], List[i]	#* Scambio del valore minore con il successivo.
                swap = True

    return List


@staticmethod
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
