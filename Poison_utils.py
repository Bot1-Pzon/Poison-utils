'''
Poison's Utilities
-
Modulo con varie funzionalità creato da Poison_8o8.
'''

import os
import sys
from random import randint
from datetime import datetime	# Per le stampe temporali.

if __name__ == "__main__":

	print(f'\nErrore: "{os.path.normpath(os.path.basename(__file__))}" è un modulo.\nNon dovresti eseguire questo file direttamente.\n')
	sys.exit()

# =================================================================================================================== #

class Colors:
	"Funzionalità per la stampa colorata."

	reset = "\033[0m"
	bold = "\033[01m"
	disable = "\033[02m"
	underline = "\033[04m"
	blink = "\033[05m"
	reverse = "\033[07m"
	strike_through = "\033[09m"
	invisible = "\033[08m"

	class fg:
		white = "\033[50m"
		black = "\033[30m"
		red = "\033[31m"
		green = "\033[32m"
		orange = "\033[33m"
		blue = "\033[34m"
		purple = "\033[35m"
		cyan = "\033[36m"
		light_grey = "\033[37m"
		dark_grey = "\033[90m"
		light_red = "\033[91m"
		light_green = "\033[92m"
		yellow = "\033[93m"
		light_blue = "\033[94m"
		pink = "\033[95m"
		light_cyan = "\033[96m"

	class bg:
		black = "\033[40m"
		red = "\033[41m"
		green = "\033[42m"
		orange = "\033[43m"
		blue = "\033[44m"
		purple = "\033[45m"
		cyan = "\033[46m"
		light_grey = "\033[47m"

# =================================================================================================================== #

class Console:
	"Funzionalità per facilitare l'interazione con il terminale."

	debug = None
	logs = None
	logs_file_path = None
	logs_file = None
	screen_cleaning_method = None
	colored_output = None


	@staticmethod
	def error(error_message: str, *, show_to_console: bool = False, colored_output: bool = False, time_stamp: bool = True) -> None:
		''' Metodo per la presentazione degli errori non fatali.
		Per presentare errori fatali usare: "Console.fatal_error()". '''

		colored_output = Console.colored_output	# Sovrascrizione della variabile locale con la variabile della classe.
		time_stamp_value = datetime.now().strftime("%H:%M:%S")	# Time stamp per i log.

		if Console.logs is True :
			with open(Console.logs_file_path, "a") as logs_file:
				logs_file.write(f"\t[{time_stamp_value}] - Errore: {error_message}.\n")

		if Console.debug is True or show_to_console is True:
			if Console.colored_output is True or colored_output is True:
				if time_stamp is True:
					print(f"\n{Colors.bold}{Colors.bg.orange}  >{Colors.reset} {Colors.fg.green}[{time_stamp_value}] - {error_message}.{Colors.reset}\n")

				else:
					print(f"\n{Colors.bold}{Colors.bg.orange}  >{Colors.reset} {Colors.fg.green}{error_message}.{Colors.reset}\n")

			else:	# Se la stampa colorato non è attiva:
				if time_stamp is True:
					print(f"\n  > [{time_stamp_value}] - {error_message}.\n")

				else:
					print(f"\n  > {error_message}.\n")


	@staticmethod
	def fatal_error(error_message: str, *, colored_output: bool = False) -> None:

		if Console.logs is True and os.path.exists(Console.logs_file_path):
			time_stamp_value = datetime.now().strftime("%H:%M:%S")	# Time stamp per i log.

			with open(Console.logs_file_path, "a") as logs_file:
				logs_file.write(f"\t[{time_stamp_value}] - FATAL ERROR: {error_message}.\n")

		print()
		print(f"{Colors.bold}{Colors.bg.orange}{Colors.fg.red}<{Colors.reset}{Colors.fg.red}", end="")
		for i in range(125):
			print("\u2588", end="")
		print(f"{Colors.bold}{Colors.bg.orange}>{Colors.reset}\n")

		if Console.colored_output is True or colored_output is True:	# Se l'output colorato è stato abilitato in generale o per questo errore:
			raise Exception(f"{Colors.underline}{Colors.fg.red}{error_message}{Colors.reset}{Colors.fg.red}.{Colors.reset}\n\n")	#* Lancio dell errore.

		else:
			raise Exception(f"{error_message}.\n\n")


	@staticmethod
	def config(*, debug: bool = False,  logs: bool = False, logs_file_path: str = None, screen_cleaning_method: str = "auto", colored_output: bool = True) -> None:
		''' Metodo di configurazione della funzionalità Console.

		- È possibile attivare il debug: "Console.config(debug=True)".
		- È possibile attivare i logs: "Console.config(logs=True)".
		- È possibile specificare il percorso presso il quale si desidera venga creata la cartella contenente i file edi log: "Console.config(logs_file_path="*")".
		- È possibile specificare il metodo di pulizia dello schermo compatibile con la console: "Console.config(screen_cleaning_method="*")", (sono disponibili "auto", "cls" e "clear").
		- È possibile attivare l'output colorato: "Console.config(colored_output=True)". '''

		Console.colored_output = colored_output

		if screen_cleaning_method in ("auto", "cls", "clear"):	# Se il metodo di pulizia dello schermo è fra i supportati:
			Console.screen_cleaning_method = screen_cleaning_method

		else:	# Se il metodo di pulizia dello schermo non è fra i supportati:

			Console.fatal_error(f'''Errore durante l'esecuzione del metodo: "Console.config()":
Sono supportati solo i parametri "auto", "cls" e "clear", non "{screen_cleaning_method}" inserito dall'utente''')

		if logs is True:
			initial_time_stamp = datetime.now().strftime("%d/%m/%Y - %H:%M")

			logs_directory_name = "Logs"
			logs_file_name = "logs.log"

			if logs_file_path is None:	# Se il percorso file dei log non è stato impostato:
				Console.fatal_error('Specificare il percorso del file di log presso il metodo: "Console.config(logs_file_path=...)"')

			if not os.path.exists(logs_file_path):	# Se il percorso file dei log non esiste:
				Console.fatal_error(f'Il percorso: "{logs_file_path}" non esiste, specificarne un altro a: "Console.config(logs_file_path=...)')

			if not os.path.exists(os.path.join(logs_file_path, logs_directory_name)):	# Se la cartella dei logs non esiste:
					os.makedirs(os.path.join(logs_file_path, logs_directory_name))	#* Crea la cartella dei logs.

			logs_file_path = os.path.join(logs_file_path, logs_directory_name, logs_file_name)

			#TODO: {os.path.realpath(__file__)} Se esiste un metodo mostrare il file principale, non la libreria.

			time_header = f'\n< ==== | {initial_time_stamp} | ==== >\nEsecuzione del file: "{os.path.normpath(os.path.realpath(__file__))}".\n\n'

			if not os.path.exists(logs_file_path):	# Se il file di log non esiste:
				time_stamp_value = datetime.now().strftime("%H:%M:%S")
				time_header = f'< ==== | {initial_time_stamp} | ==== >\nEsecuzione del file: "{os.path.normpath(os.path.realpath(__file__))}".\n\n\t[{time_stamp_value}] - File dei logs creato.\n'

			with open(logs_file_path, "a") as logs_file:	#* Creazione del file dei log.
				logs_file.write(time_header)	#* Scrittura dell'intestazione temporale nel file dei log.

			Console.logs_file = File(logs_file_path)

			Console.logs_file_path = logs_file_path

		Console.debug = debug
		Console.logs = logs


	@staticmethod
	def log(console_message: str, *, show_to_console: bool = False, time_stamp: bool = False) -> None:
		''' Funzionalità per la stampa di informazioni utili a terminale a fini di debug, abilitatile con "Console.config(debug=True)".

		Il parametro "show_to_console" sovrascriverà la configurazione solo per l'istanza dove la sua funzione è stata chiamata. '''

		time_stamp_value = datetime.now().strftime("%H:%M:%S")

		if Console.debug is None:
			Console.fatal_error('Mancata esecuzione del metodo: "Console.config()"', colored_output = True)

		elif Console.debug is True or show_to_console is True:

			if Console.colored_output is True:

				if time_stamp is True:
					#* Stampa colorata con intestazione temporale.
					print(f"\n{Colors.bold}{Colors.bg.orange}  >{Colors.reset} {Colors.fg.green}[{time_stamp_value}] - {console_message}.{Colors.reset}\n")

				else:
					print(f"\n{Colors.bold}{Colors.bg.orange}  >{Colors.reset} {Colors.fg.green}{console_message}.{Colors.reset}\n")

			else:

				if time_stamp is True:
					print(f"\n  > [{time_stamp_value}] - {console_message}.\n")

				else:
					print(f"\n  > {console_message}.\n")

		if Console.logs is True:
			if os.path.exists(Console.logs_file_path):
				with open(Console.logs_file_path, "a") as logs_file:
					logs_file.write(f"\t[{time_stamp_value}] - {console_message}.\n")

			else:
				Console.fatal_error(f'Impossibile accedere al file: "{Console.logs_file_path}", precedentemente creato')

		elif Console.logs is None:
			Console.fatal_error('Mancata esecuzione del metodo: "Console.config()"')


	@staticmethod
	def stop() -> None:
		'''Funzionalità per arrestare il programma'''
		Console.log("Il programma è stato terminato tramite istruzione")
		sys.exit()


	@staticmethod
	def clear() -> None:
		"Metodo per la pulizia del terminale."

		if Console.screen_cleaning_method == None:
			Console.fatal_error('Specificare il metodo di pulizia della schermo presso il metodo: "Console.config(screen_cleaning_method=...)"')

		elif Console.screen_cleaning_method == "auto":
			if os.name == 'posix':
				os.system('clear')	# Metodo di pulizia per sistemi Unix/Linux/macOS.

			elif os.name == 'nt':
				os.system('cls')	# Metodo di pulizia per sistemi Windows.

		elif Console.screen_cleaning_method == "clear":
			os.system("clear")

		elif Console.screen_cleaning_method == "cls":
			os.system("cls")

		else:
			Console.fatal_error(f'Errore: Il parametro: "{Console.screen_cleaning_method}" impostato in: "Console.config(screen_cleaning_method=...)" non è supportato')


	@staticmethod
	def del_lines(lines_number: int = 2) -> None:
		"Eliminazione di un numero dato di linee dal terminale."

		if lines_number < 1:
			Console.fatal_error(f'Il minimo di line eliminabili è 1, non "{lines_number}"')

		for i in range(lines_number):
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			sys.stdout.flush()


	@staticmethod
	def function_timer(_function: callable):
		"Funzionalità per la misurazione del tempo di esecuzione di una funzione."

		def wrapper(*all_positional_arguments, **all_keywords_arguments):
			start_time = datetime.now()

			function_results = _function(*all_positional_arguments, **all_keywords_arguments)

			end_time = datetime.now()

			execution_time = end_time - start_time

			Console.log(f'La funzione "{_function.__name__}({_function(*all_positional_arguments, **all_keywords_arguments)})" ha impiegato {execution_time} secondi per eseguire', show_to_console=True)

			return function_results
		return wrapper


	@staticmethod
	def create_virtual_environment(virtual_environment_path: str = "./" , virtual_environment_name: str = '.venv'):
		" Funzionalità per la creazione di un ambiente virtuale. "

		virtual_environment_path = os.path.join(virtual_environment_path, virtual_environment_name)

		if os.path.exists(virtual_environment_path):
			Console.fatal_error(f'Il percorso "{virtual_environment_path}" esiste gia')

		import venv
		venv.create(virtual_environment_path, clear=True)
		Console.log(f'Ambiente virtuale creato in: "{virtual_environment_path}"')


	@staticmethod
	def file_path_input(pre_input_text: str = ""):
		" Autocompletatore per i percorsi file "

		# Generato da I.A.

		try:
			from prompt_toolkit import prompt	# type: ignore
			from prompt_toolkit.completion import PathCompleter	# type: ignore
			from prompt_toolkit.styles import Style	# type: ignore

		except ModuleNotFoundError:
			Console.fatal_error('Mancate il modulo: "prompt_toolkit"')
   

		results = prompt(pre_input_text, completer = PathCompleter(only_directories = False, expanduser = True))
		return results


	class Cursor:
		" Sottoclasse per l'interazione con il cursore. "

		@staticmethod
		def move_to(x: int, y: int) -> None:
			"Funzionalità per lo spostamento del cursore nel terminale."
			# Preso da: https://github.com/gravmatt/py-term.

			if not (x > 0 and y > 0):	# Se le coordinate sono negative o nulle:
				Console.fatal_error(f'Le coordinate minime inseribili sono: "(1; 1)" non "({x}; {y})"')

			else:
				sys.stdout.write(f'\033[{y};{x}f')	#* Spostamento del cursore.
				sys.stdout.flush()


		@staticmethod
		def reset() -> None:
			sys.stdout.write('\033[H')
			sys.stdout.flush()

# =================================================================================================================== #

class File:
	" Classe per gestire i file. "

	def __init__(self, path: str) -> None:

		if  not os.path.exists(path):	# Se il percorso file non esiste:
			Console.fatal_error(f'Il percorso file: "{path}" non esiste')

		self.path = os.path.normpath(os.path.realpath(path))

		self.name = os.path.basename(self.path)

		self.extension = os.path.splitext(self.path)[1]

		self.directory_name = os.path.basename(os.path.dirname(self.path))

		with open(self.path, "r") as file:
			self.content = file.read()


	def write(self, content: str, binary: bool = True) -> None:
		" Scrivere nel file. "

		self.content = content

		if binary is True:
			writing_method = "wb"
			encoding = None
			content = bytes(self.content, "utf-8")

		else:
			writing_method = "w"
			encoding = "utf-8"

		with open(self.path, writing_method, encoding = encoding) as file:
			file.write(content)

		content = rf"{content}"
		if len(content) > 25:
			Console.log(f'Scrittura di "{content[0:25]}..." al file "{self.path}" completata')

		else:
			Console.log(f'Scrittura di "{content}" al file "{self.path}" completata')


	def delete(self) -> None:
		" Eliminare il file e l'istanza associata. "

		os.remove(self.path)	#* Eliminare il file.
		Console.log(f'File "{self.path}" eliminato')
		del self	#* Eliminare l'istanza.


	def __str__(self) -> str:
		return f'''[{self.name} -> '{self.path}']'''


	@staticmethod
	def path_exist(path: str) -> bool:
		''' Verificare se il percorso esiste.
  			\n(wrapper di "os.path.exists()") '''
		return os.path.exists(path)


	@staticmethod
	def create_complete_path(path: str, file_name: str = None) -> "File":
		''' Crea il percorso e il file se non esistono.\n
			Si possono specificare il percorso file e il nome del fiele separatamente. '''

		if file_name != None:
			path = os.path.join(path, file_name)

		if os.path.exists(path):
			Console.fatal_error(f'Il percorso "{path}" esiste gia')

		if not os.path.exists(os.path.dirname(path)):	# Se la cartella contenitrice non esiste:
			os.makedirs(os.path.dirname(path))	#* Creazione cartella contenitrice
			Console.log(f'Cartella "{os.path.dirname(path)}" creata')

		if file_name == None:
			os.makedirs(path)
			Console.log(f'Cartella "{path}" creata')

		else:
			file = open(path, "x")
			file.close()
			Console.log(f'File "{path}" creato')
			return File(path)


	@staticmethod
	def delete_file_at_path(path: str) -> None:
		''' Eliminare il file al percorso dato '''

		if os.path.exists(path):
			os.remove(path)
			Console.log(f'File "{path}" eliminato')

		else:
			Console.fatal_error(f'Il file "{path}" non esiste')

# =================================================================================================================== #

class Web_kit:
	"Funzionalità per lo sviluppo di server web."

	statics_path = None

	@staticmethod
	def config(*, statics_path: str = "static") -> None:
		'''Metodo di configurazione della funzionalità Web_kit.

		- È possibile specificare il percorso delle risorse statiche.'''

		if os.path.exists(statics_path):
			Web_kit.statics_path = statics_path

		else:
			Console.fatal_error(f'Il percorso "{statics_path}" non esiste')


	@staticmethod
	def page_render(page_file_name: str) -> str:
		''' Funzionalità che permette il rendering di documenti ".html" specificando il nome del file.

		- page_file_name: Nome del file della pagina che si intende caricare. '''

		page_file_path = os.path.join(Web_kit.statics_path, page_file_name)

		if os.path.exists(page_file_path):
			with open(page_file_path, "r") as page_file:
				page_content = page_file.read()	#* Rendering della pagina.

			Console.log(f'Pagina "{page_file_name}" caricata da: "{page_file_path}" con successo.')
			return page_content

		else:
			Console.error(f'Errore: "{page_file_path}" non esiste')
			return f'Errore: "{page_file_path}" non esiste.'

# =================================================================================================================== #

class List:
	"Funzionalità per la gestione di liste."

	@staticmethod
	def create_random_list(list_length: int, minimum_value: int, maximum_value: int) -> list[int]:
		"Funzionalità per la creazione di una lista casuale dalla lunghezza e range dei valori specificati."

		random_list = []
		for i in range(list_length):
			random_list.append(randint(minimum_value, maximum_value))	#* Inserimento nella lista casuale.

		return random_list


	@staticmethod
	def bubble_sort(List: list[int]) -> list[int]:
		''' Funzionalità per il riordinamento delle liste, inefficiente O(n²). '''

		for i in range(len(List) - 1):
			for j in range(len(List) - i - 1):
				if List[j] > List[j + 1]:
					List[j], List[j + 1] = List[j + 1], List[j]	#* Scambio del valore minore con il successivo.
		return List


	@staticmethod
	def jenky_sort(List: list[int]) -> list[int]:
		''' '''

		swap:bool = True
		while swap is True:	#* Mentre è stato effettuato uno scambio:
			swap = False

			for i in range(len(List) - 1):
				if List[i] > List[i + 1]:
					List[i], List[i + 1] = List[i + 1], List[i]	#* Scambio del valore minore con il successivo.
					swap = True

		return List


	@staticmethod
	def duplicates_counter(List: list) -> dict:
		" Ritorna un dizionario con il numero di occorrenze di ogni elemento nella lista data. "

		counter:dict = {}

		for element in List:
			if element in counter:
				counter[element] += 1	#* Incremento del valore del contatore
			else:
				counter[element] = 1	#* Inserimento di un nuovo valore nel contatore

		return counter

# =================================================================================================================== #

class Math:
	"Funzionalità per l'implementazione di varie funzioni matematiche."

	@staticmethod
	def factorial(x: int) -> int:
		" Funzionalità per il calcolo del fattoriale di un intero."

		r: int = 1
		for i in range(1, x + 1):
			r =+ r * i
		return r


	@staticmethod
	def fibonacci(n: int) -> int:
		" Ritorna l'n-esimo numero nella sequenza di Fibonacci. "

		if n <= 0:
			return 0

		elif n == 1:
			return 1

		else:
			fibonacci_sequence: list[int] = [0, 1]

			for i in range(2, n + 71):
				fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

			return fibonacci_sequence[n]

# =================================================================================================================== #

class Physic:

	supported_units = ("km", "hm", "dam", "m", "dm", "cm", "mm", "km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²")

	def __init__(self, measure: int | float, uncertainty: int | float, unit: str) -> None:

		if not isinstance(measure, (int, float)):
			Console.fatal_error(f'La misura "{measure}" non è un numero supportato')

		if not isinstance(uncertainty, (int, float)):
			Console.fatal_error(f'''L'incertezza "{uncertainty}" non è un numero supportato''')

		if not isinstance(unit, str):
			Console.fatal_error(f'''L'unità "{unit}" non è una stringa supportata''')

		if unit not in self.supported_units:
			Console.fatal_error(f'''L'unità "{unit}" non è supportata''')

		self.measure = measure
		self.uncertainty = uncertainty
		self.unit = unit


	def __add__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di tipo: "{type(self)}" e "{other}" di tipo "{type(other)}"')

		if self.unit != other.unit:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di unità "{self.unit}" e "{other}" di unità "{other.unit}"')

		resulting_measure = self.measure + other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __sub__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di tipo: "{type(self)}" e "{other}" di tipo"{type(other)}"')

		if self.unit != other.unit:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di unità "{self.unit}" e "{other}" di unità "{other.unit}"')

		resulting_measure = self.measure - other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __mul__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di tipo: "{type(self)}" e "{other}" di tipo"{type(other)}"')

		if self.unit != other.unit:
			Console.fatal_error(f'Non sono supportate la moltiplicazione tra tra "{self}" di unità "{self.unit}" e "{other}" di unità "{other.unit}"')

		resulting_measure = self.measure * other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		resulting_unit = f"{self.unit}²"

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = resulting_unit)


	def __truediv__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.fatal_error(f'Non sono supportate le operazioni tra "{self}" di tipo: "{type(self)}" e "{other}" di tipo"{type(other)}"')

		if self.unit != other.unit:
			Console.fatal_error(f'Non sono supportate la moltiplicazione tra tra "{self}" di unità "{self.unit}" e "{other}" di unità "{other.unit}"')

		resulting_measure = self.measure / other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __str__(self) -> str:
		return f"({self.measure} ± {self.uncertainty}){self.unit}"

# =================================================================================================================== #

def swap(a, b):
	a, b = b, a
	return a, b

# =================================================================================================================== #

# Metadati:

__doc__ = "docstring w.i.p."
__version__ = "1.0.3"

spell = '''Ain't it hard to stumble
and land in the wrong side of the lagoon,
ain't it hard to stumble
and hope that death didn't get you so soon.

- Poison_8o8'''
