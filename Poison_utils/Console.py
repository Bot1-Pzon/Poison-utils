'''
	Funzionalità per facilitare l'interazione con il terminale.
'''

import os
import sys

import datetime

from Poison_utils import Files, Dependencies


global_debug_mode: bool = False
global_use_of_logs: bool = False
global_use_of_time_stamps: bool = False
global_colored_output: bool = None


def config(*, debug: bool = True,  logs: bool = True, logs_path: str = None, do_we_use_time_stamps: bool = False, colored_output: bool = True) -> None:
	'''
		Metodo di configurazione della funzionalità \n

		Spiegazione dei parametri:\n

		- debug: Attiva o disattiva la modalità debug.\n
		- logs: Attiva o disattiva il logging si a file che a terminale.\n
		- logs_path: Specifica il percorso dove salvare i file di log.\n
		- do_we_use_time_stamps: Attiva o disattiva le stampe temporali.\n
		- colored_output: Attiva o disattiva la stampa colorata.
	'''

	global global_debug_mode, global_use_of_logs, global_colored_output, global_use_of_time_stamps
	global_colored_output = colored_output

	if logs is True:
		global_use_of_logs = True

		if logs_path is None:
			Logs.create_logs_folder()

		else:
			Logs.create_logs_folder(logs_path)

	global_debug_mode = debug
	global_use_of_time_stamps = do_we_use_time_stamps


def clear() -> None:
	'''
		Pulisce il terminale.\n
		Wrapper di "os.system('clear')" o "os.system('cls')" a seconda del sistema operativo.
	'''

	if os.name == 'posix':
		os.system('clear')	# Metodo di pulizia per sistemi Unix/Linux/macOS.

	elif os.name == 'nt':
		os.system('cls')	# Metodo di pulizia per sistemi Windows.

	else:
		Logs.fatal_error(f'Nel sistema operativo \"{os.name}\" la pulizia dello schermo non è supportata')


def stop() -> None:
	'''
		Arresta il programma.\n
		Wrapper di "sys.exit()."
	'''
	Logs.log("Il programma è stato terminato tramite istruzione")
	sys.exit()


class Colors:
	''' Funzionalità per manipolare l'output del terminale, ad esempio con la stampa colorata. '''

	reset = '\033[0m'
	bold = '\033[01m'
	disable = '\033[02m'
	underline = '\033[04m'
	blink = '\033[05m'
	reverse = '\033[07m'
	strike_through = '\033[09m'
	invisible = '\033[08m'

	class fg:
		''' Colore del testo. '''
		white = '\033[50m'
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		orange = '\033[33m'
		blue = '\033[34m'
		purple = '\033[35m'
		cyan = '\033[36m'
		light_grey = '\033[37m'
		dark_grey = '\033[90m'
		light_red = '\033[91m'
		light_green = '\033[92m'
		yellow = '\033[93m'
		light_blue = '\033[94m'
		pink = '\033[95m'
		light_cyan = '\033[96m'

	class bg:
		''' Colore dello sfondo. '''

		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		orange = '\033[43m'
		blue = '\033[44m'
		purple = '\033[45m'
		cyan = '\033[46m'
		light_grey = '\033[47m'


class Logs:
	''' Funzionalità per il logging di informazioni, sia a terminale che a file. '''

	logs_files_list: list[Files.File] = []
	logs_file_path: str = None


	@staticmethod
	def create_logs_folder(logs_path: str = "./", logs_directory_name: str = "Logs", logs_file_name: str = "logs.log") -> None:

		''' Crea la cartella e i file di log. '''

		initial_time_stamp = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")

		main_file_path = os.path.normpath(os.path.realpath(sys.argv[0]))	# Ottieni il percorso del file principale
		time_header = f'< ==== | {initial_time_stamp} | ==== >\nEsecuzione del file: "{main_file_path}".\n\n'

		if logs_path is None:	# Se il percorso file dei log non è stato impostato:
			Logs.fatal_error('Specificare il percorso del file di log presso il metodo: "config(logs_file_path=...)"')

		if not os.path.exists(logs_path):	# Se il percorso file dei log non esiste:
			Logs.fatal_error(f'Il percorso: "{logs_path}" non esiste, specificarne un altro a: "config(logs_file_path=...)')

		if not os.path.exists(os.path.normpath(os.path.join(logs_path, logs_directory_name))):	# Se la cartella dei logs non esiste:
			time_stamp_value = datetime.datetime.now().strftime("%H:%M:%S")
			os.makedirs(os.path.normpath(os.path.join(logs_path, logs_directory_name)))	#* Crea la cartella dei logs.
			time_header = time_header + f'\t[{time_stamp_value}] - Cartella dei log creato presso: \"{os.path.normpath(os.path.join(logs_path, logs_directory_name))}\".\n'

		logs_path = os.path.join(logs_path, logs_directory_name, logs_file_name)

		if not os.path.exists(logs_path):	# Se il file di log non esiste:
			time_stamp_value = datetime.datetime.now().strftime("%H:%M:%S")
			time_header =  time_header + f'\t[{time_stamp_value}] - File dei logs creato presso: \"{os.path.normpath(logs_path)}\".\n'

		else:
			time_header = '\n' + time_header

		with open(logs_path, "a") as logs_file:	#* Creazione del file dei log.
			logs_file.write(time_header)	#* Scrittura dell'intestazione temporale nel file dei log.

		if len(Logs.logs_files_list) > 0:
			Logs.log(f"File dei logs parallelo creato presso: \"{os.path.normpath(logs_path)}\"")

		Logs.logs_files_list.append(Files.File(logs_path))

		Logs.logs_file_path = logs_path


	@staticmethod
	def write_to_log_files(message: str, time_stamp: str = None, end_of_message: str = None) -> None:
		''' Scrive ai vari file di log. '''

		if not os.path.exists(Logs.logs_file_path):

			Logs.fatal_error(f"Il file di log \"{Logs.logs_file_path}\" non esiste")

		if time_stamp is None:
			time_stamp_value = datetime.datetime.now().strftime('%H:%M:%S')

		else:
			time_stamp_value = time_stamp

		message.replace('\n', ' ')	#* Sostituzione dei caratteri di nuova linea con spazi.

		if end_of_message is None:
			message = f"\t[{time_stamp_value}] - {message}.\n"

		else:
			message = f"\t[{time_stamp_value}] - {message + end_of_message}"

		for log_file in Logs.logs_files_list:
			try:
				with open(log_file.path, 'a', encoding = 'utf-8') as logs_file:
					logs_file.write(message)	#* Scrittura al file.

			except Exception as logs_file_handling_error:
				Logs.fatal_error(f"Durante la scrittura nel file di log \"{log_file.path}\" si è verificato il seguente errore:\n\n\"{logs_file_handling_error}\"")


	@staticmethod
	def log(console_message: str, /, *, show_to_console: bool = False, time_stamp: bool = None, end: str = None) -> None:
		'''
			Stampa di informazioni utili a terminale a fini di debug, abilitatile con \"config(debug = True)\".\n
			Il parametro "show_to_console" sovrascriverà la configurazione solo per l'istanza dove la sua funzione è stata chiamata.
		'''

		time_stamp_value = datetime.datetime.now().strftime("%H:%M:%S")

		if global_debug_mode is None:
			Logs.fatal_error("Mancata esecuzione del metodo: \"config()\"")

		elif global_debug_mode is True or show_to_console is True:

			if global_colored_output is True:

				if time_stamp is True:

					if end is None:
						print(f"\n[{time_stamp_value}]{Colors.bold} - {Colors.bg.orange}> {Colors.reset} {Colors.fg.green}[{time_stamp_value}] - {console_message}.{Colors.reset}")	#* Stampa colorata con intestazione temporale.

					else:
						print(f"\n[{time_stamp_value}]{Colors.bold} - {Colors.bg.orange}> {Colors.reset} {Colors.fg.green}[{time_stamp_value}] - {console_message}.{Colors.reset}", end = end)

				else:

					if end is None:
						print(f"\n{Colors.bold}{Colors.bg.orange}> {Colors.reset} {Colors.fg.green}{console_message}.{Colors.reset}")

					else:
						print(f"\n{Colors.bold}{Colors.bg.orange}> {Colors.reset} {Colors.fg.green}{console_message}{Colors.reset}", end = end)

			else:	# Se la stampa colorata è disabilitata:

				if time_stamp is True:

					if end is None:
						print(f"\n> [{time_stamp_value}] - {console_message}.")

					else:
						print(f"\n> [{time_stamp_value}] - {console_message}", end = end)

				else:	# Se l'intestazione temporale è disabilitata:

					if end is None:
						print(f"\n> {console_message}.")

					else:
						print(f"\n> {console_message}", end = end)

		if global_use_of_logs is True:

			if end is None:
				Logs.write_to_log_files(console_message, time_stamp_value)

			else:
				Logs.write_to_log_files(console_message, time_stamp_value, end_of_message = end)

		elif global_use_of_logs is None:
			Logs.fatal_error("Mancata esecuzione del metodo: \"config()\"")


	@staticmethod
	def function_timer(_function: callable):
		''' Misura e logga il tempo di esecuzione di una funzione. '''

		def wrapper(*all_positional_arguments, **all_keywords_arguments):
			start_time = datetime.datetime.now()

			function_results = _function(*all_positional_arguments, **all_keywords_arguments)

			end_time = datetime.datetime.now()

			execution_time = end_time - start_time

			Logs.log(f"La funzione \"{_function.__name__}({_function(*all_positional_arguments, **all_keywords_arguments)})\" ha impiegato {execution_time} secondi per eseguire", show_to_console = True)

			return function_results
		return wrapper


	@staticmethod
	def error(error_message: str, /, *, show_to_console: bool = False, colored_output: bool = False, time_stamp: bool = None) -> None:
		'''
			Logga un errore non fatale.\n
			Per presentare errori fatali usare: \"Logs.fatal_error()\".
		'''

		if time_stamp is None:
			time_stamp = global_use_of_time_stamps

		colored_output = colored_output	# Sovrascrizione della variabile locale con la variabile della classe.
		time_stamp_value = datetime.datetime.now().strftime("%H:%M:%S")	# Time stamp per i log.

		if global_use_of_logs is True:	# Se i log sono attivi:
			Logs.write_to_log_files(f"ERROR: {error_message}", time_stamp_value)

		if global_debug_mode is True or show_to_console is True:
			if global_colored_output is True or colored_output is True:
				if time_stamp is True:
					print(f"\n[{time_stamp_value}]{Colors.bold} - {Colors.bg.red}ERROR{Colors.reset}: {Colors.fg.light_red}[{time_stamp_value}] - {error_message}.{Colors.reset}")

				else:
					print(f"\n{Colors.bold}{Colors.bg.red}ERROR{Colors.reset}{Colors.bold}:{Colors.reset} {Colors.fg.light_red}{error_message}.{Colors.reset}")

			else:	# Se la stampa colorato non è attiva:
				if time_stamp is True:
					print(f"\nERROR: [{time_stamp_value}] - {error_message}.")

				else:
					print(f"\nERROR: {error_message}.")


	@staticmethod
	def fatal_error(error_message: str, *, colored_output: bool = False, do_we_write_to_log_file: bool = True) -> None:
		'''
			Logga un errore fatale e interrompe il programma.\n
			Per presentare errori non fatali usare: "Logs.error()".\n
			Wrapper di: "raise Exception(error_message)".
		'''
		if global_use_of_logs is True and do_we_write_to_log_file is True:	# Se i log sono attivi:
			time_stamp_value = datetime.datetime.now().strftime("%H:%M:%S")	#* valore temporale per i log.

			Logs.write_to_log_files(f"FATAL ERROR: {error_message}", time_stamp_value)

		print()
		print(f"{Colors.bold}{Colors.bg.orange}{Colors.fg.red}<{Colors.reset}{Colors.fg.red}", end="")
		print("\u2588" * 125, end="")
		print(f"{Colors.bold}{Colors.bg.orange}>{Colors.reset}\n")

		if global_colored_output is True or colored_output is True:	# Se l'output colorato è stato abilitato in generale o per questo errore:
			raise Exception(f"{Colors.underline}{Colors.fg.red}{error_message}{Colors.reset}{Colors.fg.red}.{Colors.reset}\n\n")	#* Lancio dell errore.

		else:
			raise Exception(f"{error_message}.\n\n")


class Cursor:
	''' Classe per l'interazione con il cursore. '''

	@staticmethod
	def move_to(x: int, y: int) -> None:
		''' Sposta il cursore del terminale alle coordinate date. '''
		# Preso da: https://github.com/gravmatt/py-term.

		if not (x > 0 and y > 0):	# Se le coordinate sono negative o nulle:
			Logs.fatal_error(f"Le coordinate minime inseribili sono: \"(1; 1)\" non \"({x}; {y})\"")

		else:
			sys.stdout.write(f'\033[{y};{x}f')	#* Spostamento del cursore.
			sys.stdout.flush()


	@staticmethod
	def reset() -> None:
		''' Riposiziona il cursore nella posizione iniziale. '''

		sys.stdout.write('\033[H')
		sys.stdout.flush()


	@staticmethod
	def delete_lines(lines_number: int = 2) -> None:
		''' Cancella il numero dato di linee dal terminale. '''

		if lines_number < 1:
			Logs.fatal_error(f"Il minimo di line eliminabili è 1, non \"{lines_number}\"")

		for i in range(lines_number):
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			sys.stdout.flush()


def file_path_input(pre_input_text: str = '') -> str:
	'''
		Auto-completatore per i percorsi file.\n
		Necessita del modulo "prompt_toolkit" per funzionare correttamente.
	'''

	if Dependencies.is_library_importable('prompt_toolkit') is False:
		Dependencies.install_component('prompt_toolkit')

	try:
		from prompt_toolkit import prompt
		from prompt_toolkit.completion import PathCompleter

	except ModuleNotFoundError:
		Logs.fatal_error("Mancate il modulo: \"prompt_toolkit\"")

	except Exception as prompt_toolkit_import_error:
		Logs.fatal_error(f"Durante l'importazione del modulo \"prompt_toolkit\" si è verificato il seguente errore:\n\n\"{prompt_toolkit_import_error}\"")

	else:
		results = prompt(pre_input_text, completer = PathCompleter(only_directories = False, expanduser = True))
		return os.path.normpath(results)
