'''
	Poison's Utilities
	-
	Modulo con varie funzionalità creato da Poison_8o8.
'''

import os

if __name__ == '__main__':

	print(f"\n\033[31mErrore\033[0m: \033[44m\033[01m{os.path.normpath(os.path.basename(__file__))}\033[0m è un modulo.\nNon dovresti eseguire questo file direttamente.\n")
	sys_exit()

from sys import (
	exit as sys_exit,
	stdout as sys_stdout
)

from shutil import (
	move as shutil_move,
	copy as shutil_copy,
	rmtree as shutil_remove_tree
)

from subprocess import (
	run as run_subprocess,
	check_output as check_subprocess_output,
	CalledProcessError
)

from random import randint as random_integer
from datetime import datetime	# Per le stampe temporali.
from importlib.util import find_spec


# Metadati:
__doc__ = "docstring w.i.p."
__version__ = '2.0.3'

spell = """Ain't it hard to stumble
and land in the wrong side of the lagoon,
ain't it hard to stumble
and hope that death didn't get you so soon.

- Poison_8o8"""

# =================================================================================================================== #

class Console:
	''' Funzionalità per facilitare l'interazione con il terminale. '''

	debug: bool = False
	do_we_use_logs: bool = False
	do_we_use_time_stamps: bool = False
	terminal_cleaning_method: str = 'auto'
	colored_output: bool = None


	@staticmethod
	def config(*, debug: bool = True,  logs: bool = True, logs_path: str = None, do_we_use_time_stamps: bool = False, screen_cleaning_method: str = "auto", colored_output: bool = True) -> None:
		'''
			Metodo di configurazione della funzionalità Console.\n

			Spiegazione dei parametri:\n

			- debug: Attiva o disattiva la modalità debug.\n
			- logs: Attiva o disattiva il logging si a file che a terminale.\n
			- logs_path: Specifica il percorso dove salvare i file di log.\n
			- do_we_use_time_stamps: Attiva o disattiva le stampe temporali.\n
			- screen_cleaning_method: Specifica il metodo di pulizia dello schermo.\n
			- colored_output: Attiva o disattiva la stampa colorata.
		'''

		Console.colored_output = colored_output

		if screen_cleaning_method in ("auto", "cls", "clear"):	# Se il metodo di pulizia dello schermo è fra i supportati:
			Console.terminal_cleaning_method = screen_cleaning_method

		else:	# Se il metodo di pulizia dello schermo non è fra i supportati:
			Console.Logs.Errors.fatal_error(f"Errore durante l'esecuzione del metodo: \"Console.config()\":\nSono supportati solo i parametri (\"auto\", \"cls\" e \"clear\"), non \"{screen_cleaning_method}\" inserito dall'utente")

		if logs is True:
			Console.do_we_use_logs = True

			if logs_path is None:
				Console.Logs.create_logs_folder()

			else:
				Console.Logs.create_logs_folder(logs_path)

		Console.debug = debug
		Console.do_we_use_time_stamps = do_we_use_time_stamps


	@staticmethod
	def clear() -> None:
		'''
			Pulisce il terminale.\n
			Wrapper di "os.system('clear')" o "os.system('cls')" a seconda del sistema operativo.
		'''

		if Console.terminal_cleaning_method is None:
			Console.Logs.Errors.fatal_error('Specificare il metodo di pulizia della schermo presso il metodo: "Console.config(screen_cleaning_method=...)"')

		elif Console.terminal_cleaning_method == "auto":
			if os.name == 'posix':
				os.system('clear')	# Metodo di pulizia per sistemi Unix/Linux/macOS.

			elif os.name == 'nt':
				os.system('cls')	# Metodo di pulizia per sistemi Windows.

			else:
				Console.Logs.Errors.fatal_error(f'Nel sistema operativo \"{os.name}\" la pulizia dello schermo non è supportata')

		elif Console.terminal_cleaning_method == "clear":
			os.system("clear")

		elif Console.terminal_cleaning_method == "cls":
			os.system("cls")

		else:
			Console.Logs.Errors.fatal_error(f"Errore: Il parametro: \"{Console.terminal_cleaning_method}\" impostato in: \"Console.config(screen_cleaning_method=...)\" non è supportato")


	@staticmethod
	def stop() -> None:
		'''
			Arresta il programma.\n
			Wrapper di "sys.exit()."
		'''
		Console.Logs.log("Il programma è stato terminato tramite istruzione")
		sys_exit()


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

		logs_files_list: list["File"] = []
		logs_file_path: str = None


		@staticmethod
		def create_logs_folder(logs_path: str = "./", logs_directory_name: str = "Logs", logs_file_name: str = "logs.log") -> None:

			''' Crea la cartella e i file di log. '''

			initial_time_stamp = datetime.now().strftime("%d/%m/%Y - %H:%M")

			#TODO: {os.path.realpath(__file__)} Se esiste un metodo mostrare il file principale, non la libreria.
			time_header = f'< ==== | {initial_time_stamp} | ==== >\nEsecuzione del file: "{os.path.normpath(os.path.realpath(__file__))}".\n\n'

			if logs_path is None:	# Se il percorso file dei log non è stato impostato:
				Console.Logs.Errors.fatal_error('Specificare il percorso del file di log presso il metodo: "Console.config(logs_file_path=...)"')

			if not os.path.exists(logs_path):	# Se il percorso file dei log non esiste:
				Console.Logs.Errors.fatal_error(f'Il percorso: "{logs_path}" non esiste, specificarne un altro a: "Console.config(logs_file_path=...)')

			if not os.path.exists(os.path.normpath(os.path.join(logs_path, logs_directory_name))):	# Se la cartella dei logs non esiste:
				time_stamp_value = datetime.now().strftime("%H:%M:%S")
				os.makedirs(os.path.normpath(os.path.join(logs_path, logs_directory_name)))	#* Crea la cartella dei logs.
				time_header = time_header + f'\t[{time_stamp_value}] - Cartella dei log creato presso: \"{os.path.normpath(os.path.join(logs_path, logs_directory_name))}\".\n'

			logs_path = os.path.join(logs_path, logs_directory_name, logs_file_name)

			if not os.path.exists(logs_path):	# Se il file di log non esiste:
				time_stamp_value = datetime.now().strftime("%H:%M:%S")
				time_header =  time_header + f'\t[{time_stamp_value}] - File dei logs creato presso: \"{os.path.normpath(logs_path)}\".\n'

			else:
				time_header = '\n' + time_header

			with open(logs_path, "a") as logs_file:	#* Creazione del file dei log.
				logs_file.write(time_header)	#* Scrittura dell'intestazione temporale nel file dei log.

			if len(Console.Logs.logs_files_list) > 0:
				Console.Logs.log(f"File dei logs parallelo creato presso: \"{os.path.normpath(logs_path)}\"")

			Console.Logs.logs_files_list.append(File(logs_path))

			Console.Logs.logs_file_path = logs_path
			Console.do_we_use_logs = True


		@staticmethod
		def write_to_log_files(message: str, time_stamp: str = None, end_of_message: str = None) -> None:
			''' Scrive ai vari file di log. '''

			if not os.path.exists(Console.Logs.logs_file_path):

				Console.Logs.Errors.fatal_error(f"Il file di log \"{Console.Logs.logs_file_path}\" non esiste")

			if time_stamp is None:
				time_stamp_value = datetime.now().strftime('%H:%M:%S')

			else:
				time_stamp_value = time_stamp

			if end_of_message is None:
				message = f"\t[{time_stamp_value}] - {message}.\n"

			else:
				message = f"\t[{time_stamp_value}] - {message + end_of_message}"

			for log_file in Console.Logs.logs_files_list:
				try:
					with open(log_file.path, "a", encoding = 'utf-8') as logs_file:
						logs_file.write(message)	#* Scrittura al file.

				except Exception as logs_file_handling_error:
					Console.Logs.Errors.fatal_error(f"Durante la scrittura nel file di log \"{log_file.path}\" si è verificato il seguente errore: \"{logs_file_handling_error}\"")


		@staticmethod
		def log(console_message: str, /, *, show_to_console: bool = False, time_stamp: bool = None, end: str = None) -> None:
			'''
				Stampa di informazioni utili a terminale a fini di debug, abilitatile con \"Console.config(debug = True)\".\n
				Il parametro "show_to_console" sovrascriverà la configurazione solo per l'istanza dove la sua funzione è stata chiamata.
			'''

			time_stamp_value = datetime.now().strftime("%H:%M:%S")

			if Console.debug is None:
				Console.Logs.Errors.fatal_error("Mancata esecuzione del metodo: \"Console.config()\"", colored_output = True)

			elif Console.debug is True or show_to_console is True:

				if Console.colored_output is True:

					if time_stamp is True:

						if end is None:
							print(f"\n[{time_stamp_value}]{Console.Colors.bold} - {Console.Colors.bg.orange}> {Console.Colors.reset} {Console.Colors.fg.green}[{time_stamp_value}] - {console_message}.{Console.Colors.reset}")	#* Stampa colorata con intestazione temporale.

						else:
							print(f"\n[{time_stamp_value}]{Console.Colors.bold} - {Console.Colors.bg.orange}> {Console.Colors.reset} {Console.Colors.fg.green}[{time_stamp_value}] - {console_message}.{Console.Colors.reset}", end = end)

					else:

						if end is None:
							print(f"\n{Console.Colors.bold}{Console.Colors.bg.orange}> {Console.Colors.reset} {Console.Colors.fg.green}{console_message}.{Console.Colors.reset}")

						else:
							print(f"\n{Console.Colors.bold}{Console.Colors.bg.orange}> {Console.Colors.reset} {Console.Colors.fg.green}{console_message}{Console.Colors.reset}", end = end)

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

			if Console.do_we_use_logs is True:

				if end is None:
					Console.Logs.write_to_log_files(console_message, time_stamp_value)

				else:
					Console.Logs.write_to_log_files(console_message, time_stamp_value, end_of_message = end)

			elif Console.do_we_use_logs is None:
				Console.Logs.Errors.fatal_error("Mancata esecuzione del metodo: \"Console.config()\"")


		@staticmethod
		def function_timer(_function: callable):
			''' Misura e logga il tempo di esecuzione di una funzione. '''

			def wrapper(*all_positional_arguments, **all_keywords_arguments):
				start_time = datetime.now()

				function_results = _function(*all_positional_arguments, **all_keywords_arguments)

				end_time = datetime.now()

				execution_time = end_time - start_time

				Console.Logs.log(f"La funzione \"{_function.__name__}({_function(*all_positional_arguments, **all_keywords_arguments)})\" ha impiegato {execution_time} secondi per eseguire", show_to_console = True)

				return function_results
			return wrapper


		class Errors:
			''' Sottoclasse per la gestione degli errori. '''

			@staticmethod
			def error(error_message: str, /, *, show_to_console: bool = False, colored_output: bool = False, time_stamp: bool = None) -> None:
				'''
					Logga un errore non fatale.\n
					Per presentare errori fatali usare: \"Console.Logs.Errors.fatal_error()\".
				'''

				if time_stamp is None:
					time_stamp = Console.do_we_use_time_stamps

				colored_output = Console.colored_output	# Sovrascrizione della variabile locale con la variabile della classe.
				time_stamp_value = datetime.now().strftime("%H:%M:%S")	# Time stamp per i log.

				if Console.do_we_use_logs is True:	# Se i log sono attivi:
					Console.Logs.write_to_log_files(f"ERROR: {error_message}", time_stamp_value)

				if Console.debug is True or show_to_console is True:
					if Console.colored_output is True or colored_output is True:
						if time_stamp is True:
							print(f"\n[{time_stamp_value}]{Console.Colors.bold} - {Console.Colors.bg.red}ERROR{Console.Colors.reset}: {Console.Colors.fg.light_red}[{time_stamp_value}] - {error_message}.{Console.Colors.reset}")

						else:
							print(f"\n{Console.Colors.bold}{Console.Colors.bg.red}ERROR{Console.Colors.reset}{Console.Colors.bold}:{Console.Colors.reset} {Console.Colors.fg.light_red}{error_message}.{Console.Colors.reset}")

					else:	# Se la stampa colorato non è attiva:
						if time_stamp is True:
							print(f"\nERROR: [{time_stamp_value}] - {error_message}.")

						else:
							print(f"\nERROR: {error_message}.")


			@staticmethod
			def fatal_error(error_message: str, *, colored_output: bool = False, do_we_write_to_log_file: bool = True) -> None:
				'''
					Logga un errore fatale e interrompe il programma.\n
					Per presentare errori non fatali usare: "Console.Logs.Errors.error()".\n
					Wrapper di: "raise Exception(error_message)".
				'''
				if Console.do_we_use_logs is True and do_we_write_to_log_file is True:	# Se i log sono attivi:
					time_stamp_value = datetime.now().strftime("%H:%M:%S")	#* valore temporale per i log.

					Console.Logs.write_to_log_files(f"FATAL ERROR: {error_message}", time_stamp_value)

				print()
				print(f"{Console.Colors.bold}{Console.Colors.bg.orange}{Console.Colors.fg.red}<{Console.Colors.reset}{Console.Colors.fg.red}", end="")
				print("\u2588" * 125, end="")
				print(f"{Console.Colors.bold}{Console.Colors.bg.orange}>{Console.Colors.reset}\n")

				if Console.colored_output is True or colored_output is True:	# Se l'output colorato è stato abilitato in generale o per questo errore:
					raise Exception(f"{Console.Colors.underline}{Console.Colors.fg.red}{error_message}{Console.Colors.reset}{Console.Colors.fg.red}.{Console.Colors.reset}\n\n")	#* Lancio dell errore.

				else:
					raise Exception(f"{error_message}.\n\n")


	class Cursor:
		''' Sottoclasse per l'interazione con il cursore. '''

		@staticmethod
		def move_to(x: int, y: int) -> None:
			''' Sposta il cursore del terminale alle coordinate date. '''
			# Preso da: https://github.com/gravmatt/py-term.

			if not (x > 0 and y > 0):	# Se le coordinate sono negative o nulle:
				Console.Logs.Errors.fatal_error(f"Le coordinate minime inseribili sono: \"(1; 1)\" non \"({x}; {y})\"")

			else:
				sys_stdout.write(f'\033[{y};{x}f')	#* Spostamento del cursore.
				sys_stdout.flush()


		@staticmethod
		def reset() -> None:
			''' Riposiziona il cursore nella posizione iniziale. '''

			sys_stdout.write('\033[H')
			sys_stdout.flush()


		@staticmethod
		def delete_lines(lines_number: int = 2) -> None:
			''' Cancella il numero dato di linee dal terminale. '''

			if lines_number < 1:
				Console.Logs.Errors.fatal_error(f"Il minimo di line eliminabili è 1, non \"{lines_number}\"")

			for i in range(lines_number):
				sys_stdout.write("\033[F")
				sys_stdout.write("\033[K")
				sys_stdout.flush()


	@staticmethod
	def file_path_input(pre_input_text: str = '') -> str:
		''' Auto-completatore per i percorsi file '''

		if Dependencies.is_library_imported('prompt_toolkit') is False:
			Dependencies.install_components('prompt_toolkit')

		try:
			from prompt_toolkit import prompt # type: ignore
			from prompt_toolkit.completion import PathCompleter # type: ignore

		except ModuleNotFoundError:
			Console.Logs.Errors.fatal_error("Mancate il modulo: \"prompt_toolkit\"")

		except Exception as prompt_toolkit_error_import_error:
			Console.Logs.Errors.fatal_error(f"Durante l'importazione del modulo \"prompt_toolkit\" si sono verificati i seguenti errori: \"{prompt_toolkit_error_import_error}\"")


		results = prompt(pre_input_text, completer = PathCompleter(only_directories = False, expanduser = True))
		return os.path.normpath(results)


# =================================================================================================================== #

class File:
	''' Funzionalità per la gestione e interazione con i file. '''

	def __init__(self, path: str) -> None:

		if not os.path.exists(path):	# Se il percorso file non esiste:
			Console.Logs.Errors.fatal_error(f"Il percorso file: \"{path}\" non esiste")

		if not os.path.isfile(path):	# Se il percorso non punta ad un file:
			Console.Logs.Errors.fatal_error(f"Il percorso file: \"{path}\" non punta ad un file")

		self.path = os.path.normpath(os.path.realpath(path))

		self.name = os.path.basename(self.path)

		self.extension = os.path.splitext(self.path)[1]

		self.directory_name = os.path.basename(os.path.dirname(self.path))

		try:
			with open(self.path, "r") as file:
				self.content = file.read()

		except Exception as file_reading_error:
			Console.Logs.Errors.fatal_error(f"Durante la lettura del file \"{self.path}\" si è verificato il seguente errore: \"{file_reading_error}\"")


	def write(self, content: str, binary: bool = False) -> None:
		''' Scrittura a file. '''

		self.content = content

		if binary is True:
			writing_method = "wb"
			encoding = None
			content = bytes(self.content, 'utf-8')

		else:
			writing_method = "w"
			encoding = 'utf-8'

		with open(self.path, writing_method, encoding = encoding) as file:
			file.write(content)

		content = rf"{content}"
		if len(content) > 25:
			Console.Logs.log(f"Scrittura al file \"{self.path}\" completata")

		else:
			Console.Logs.log(f"Scrittura di \"{content}\" al file \"{self.path}\" completata")


	def delete(self) -> None:
		''' Elimina il file e la sua istanza associata. '''

		os.remove(self.path)	#* Eliminare il file.
		Console.Logs.log(f'File "{self.path}" eliminato')
		del self	#* Eliminare l'istanza.


	def __str__(self) -> str:
		''' Rappresentazione in stringa di un file, comprende il suo nome e percorso. '''
		return f"[{self.name} -> '{self.path}']"


	@staticmethod
	def path_exist(path: str) -> bool:
		'''
			Ritorna True se il percorso esiste.\n
			Wrapper di "os.path.exists()".
		'''
		return os.path.exists(path)


	@staticmethod
	def create_complete_path(path: str, file_name: str = None) -> "File":
		'''
			Crea il percorso completo di cartelle e file.\n
			Se si desidera creare solo cartelle non specificare \"file_name\".
		'''

		if file_name is not None:
			path = os.path.normpath(os.path.join(path, file_name))

		else:
			path = os.path.normpath(path)

		if file_name is not None:	# Se il nome del file è stato specificato:
			path = os.path.join(path, file_name)	#* Aggiungilo al percorso da creare.

		if os.path.exists(path):	# Se il percorso file non esiste:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{path}\" esiste gia")	#* Lancia un errore.

		if not os.path.exists(os.path.dirname(path)):	# Se la cartella contenitrice non esiste:
			os.makedirs(os.path.dirname(path))	#* Creazione cartella contenitrice.
			Console.Logs.log(f"Cartella \"{os.path.dirname(path)}\" creata")

		if file_name is None:
			os.makedirs(path)
			Console.Logs.log(f'Cartella "{path}" creata')

		else:
			try:
				file = open(path, "x")
				file.close()

			except Exception as file_handling_error:
				Console.Logs.Errors.fatal_error(f"Durante la creazione del file: \"{path}\" si è verificato il seguente errore: \"{file_handling_error}\"")

			else:
				Console.Logs.log(f'File "{path}" creato')
				return File(path)


	@staticmethod
	def delete_file_at_path(path: str) -> None:
		'''
			Elimina il file al percorso dato.\n
			wrapper di "os.remove()".
		'''

		if not os.path.exists(path):	# Se il percorso non esiste:
			Console.Logs.Errors.error(f"Impossibile eliminare il \"{path}\" perché non esiste")
			return

		elif os.path.isfile(path):
			is_file = True

		elif os.path.isdir(path):
			is_file = False

		else:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{path}\" non è stato riconosciuto ne come file ne come cartella")

		if is_file is True:

			try:
				os.remove(path)	#* Eliminazione del file.

			except Exception as file_handling_error:
				Console.Logs.Errors.fatal_error(f"Durante l'eliminazione del file \"{path}\" si sono verificati i seguenti errori: \"{file_handling_error}\"")

			else:
				Console.Logs.log(f"File \"{path}\" eliminato")

		else:
			try:
				shutil_remove_tree(path)	#* Eliminazione della cartella.

			except Exception as file_handling_error:
				Console.Logs.Errors.fatal_error(f"Durante l'eliminazione della cartella \"{path}\" si sono verificati i seguenti errori: \"{file_handling_error}\"")

			else:
				Console.Logs.log(f"Cartella \"{path}\" eliminata")


	@staticmethod
	def move_file(from_path: str, to_path: str) -> None:
		''' Sposta il file dal percorso specificato a quello dato. '''

		if not os.path.exists(from_path):	# Se il percorso da muovere non esiste:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{from_path}\" non esiste")

		if not os.path.isfile(from_path):	# Se il percorso da muovere non rappresenta un file:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{from_path}\" non rappresenta un file")

		if os.path.exists(to_path):	# Se il percorso di destinazione esiste:
			Console.Logs.Errors.error(f"Impossibile spostare (\"{from_path}\" -> \"{to_path}\") in quanto gia presente alla destinazione")

		try:
			shutil_move(from_path, to_path)

		except Exception as file_handling_error:
			Console.Logs.Errors.fatal_error(f"Durante il movimento del file (\"{from_path}\" -> \"{to_path}\") si sono verificati i seguenti errori: \"{file_handling_error}\"")

		else:
			Console.Logs.log(f"Avvenuto spostamento file: (\"{from_path}\" -> \"{to_path}\")")


	@staticmethod
	def copy_file(from_path: str, to_path: str) -> None:
		''' Copia il file dal percorso specificato a quello dato. '''

		if not os.path.exists(from_path):	# Se il percorso da copiare non esiste:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{from_path}\" non esiste")

		if os.path.exists(to_path):	# Se il percorso di destinazione esiste:
			Console.Logs.Errors.error(f"Impossibile copiare (\"{from_path}\" -> \"{to_path}\") in quanto gia presente alla destinazione")

		try:
			shutil_copy(from_path, to_path)

		except Exception as file_copying_error:
			Console.Logs.Errors.fatal_error(f"Durante la copiatura del file (\"{from_path}\" -> \"{to_path}\") si sono verificati i seguenti errori: \"{file_copying_error}\"")

		else:
			Console.Logs.log(f"Avvenuta copiatura file: (\"{from_path}\" -> \"{to_path}\")")

# =================================================================================================================== #

class Web_kit:
	''' Funzionalità per lo sviluppo di server web. '''

	statics_path = None

	@staticmethod
	def config(*, statics_path: str = 'statics') -> None:
		'''
			Metodo di configurazione della funzionalità Web_kit.\n
			- È possibile specificare il percorso delle risorse statiche.
		'''

		if os.path.exists(statics_path):
			Web_kit.statics_path = statics_path

		else:
			Console.Logs.Errors.fatal_error(f"Il percorso \"{statics_path}\" non esiste")


	@staticmethod
	def page_render(page_file_name: str) -> str:
		'''
			Funzionalità che permette il rendering di documenti ".html" specificando il nome del file.
			- page_file_name: Nome del file della pagina che si intende caricare.
		'''

		page_file_path = os.path.join(Web_kit.statics_path, page_file_name)

		if os.path.exists(page_file_path):
			with open(page_file_path, "r") as page_file:
				page_content = page_file.read()	#* Rendering della pagina.

			Console.Logs.log(f"Pagina \"{page_file_name}\" caricata da: \"{page_file_path}\" con successo.")
			return page_content

		else:
			Console.Logs.Errors.error(f"Errore: \"{page_file_path}\" non esiste")
			return f'Errore: "{page_file_path}" non esiste.'

# =================================================================================================================== #

class List:
	''' Funzionalità per la gestione di liste. '''

	@staticmethod
	def create_random_list(list_length: int = None, minimum_value: int = 0, maximum_value: int = 999) -> list[int]:
		''' Restituisce una lista casuale di interi dalla lunghezza e dal range di valori specificato specificato. '''

		if list_length is None:
			list_length = random_integer(1, 500)

		random_list: list[int] = []

		for _ in range(list_length):
			random_list.append(random_integer(minimum_value, maximum_value))	#* Inserimento nella lista casuale.

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
	def duplicates_counter(list_to_count: list) -> dict[int: int]:
		''' Ritorna un dizionario con il numero di occorrenze di ogni elemento nella lista data. '''

		counter: dict[int: int] = {}

		for element in list_to_count:
			if element in counter:
				counter[element] += 1	#* Incremento del valore del contatore
			else:
				counter[element] = 1	#* Inserimento di un nuovo valore nel contatore

		return counter

# =================================================================================================================== #

class Math:
	''' Funzionalità per l'implementazione di varie funzioni matematiche. '''

	@staticmethod
	def factorial(n: int) -> int:
		''' Ritorna il fattoriale del numero dato. '''

		if n < 0:
			Console.Logs.Errors.fatal_error(f'Il fattoriale di un {n} < 0 non é supportato')

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

# =================================================================================================================== #

class Physic:
	''' Classe per il calcolo con grandezze fisiche tenendo conto delle incertezze. '''

	supported_units = ('km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm', 'km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²')

	def __init__(self, measure: int | float, uncertainty: int | float, unit: str) -> None:

		if not isinstance(measure, (int, float)):
			Console.Logs.Errors.fatal_error(f"La misura \"{measure}\" non è un numero supportato")

		if not isinstance(uncertainty, (int, float)):
			Console.Logs.Errors.fatal_error(f"L'incertezza \"{uncertainty}\" non è un numero supportato")

		if not isinstance(unit, str):
			Console.Logs.Errors.fatal_error(f"L'unità \"{unit}\" non è una stringa supportata")

		if unit not in self.supported_units:
			Console.Logs.Errors.fatal_error(f"L'unità \"{unit}\" non è supportata")

		self.measure = measure
		self.uncertainty = uncertainty
		self.unit = unit


	def __add__(self, other: 'Physic') -> 'Physic':

		if type(self) is not Physic or type(other) is not Physic:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure + other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __sub__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure - other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __mul__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.Errors.fatal_error(f"Non sono supportate la moltiplicazione tra tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure * other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		resulting_unit = f"{self.unit}²"

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = resulting_unit)


	def __truediv__(self, other: "Physic") -> "Physic":

		if type(self) is not Physic or type(other) is not Physic:
			Console.Logs.Errors.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.Errors.fatal_error(f"Non sono supportate la moltiplicazione tra tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure / other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		return Physic(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __str__(self) -> str:
		return f"({self.measure} ± {self.uncertainty}){self.unit}"

# =================================================================================================================== #

class Dependencies:
	''' Classe per la gestione delle dipendenze. '''

	@staticmethod
	def is_library_imported(library_name: str) -> bool:
		''' Ritorna vero se una libreria è installata. '''

		spec = find_spec(library_name)
		return spec is not None


	def is_package_installed(package_name: str, /, *, log: bool = True) -> bool:
		''' Ritorna vero se un pacchetto Python risulta installato. '''

		try:
			check_subprocess_output(['pip', 'show', package_name])

			if log is True:
				Console.Logs.log(f"Il pacchetto \"{package_name}\" risulta installato")
			return True

		except CalledProcessError:
			if log is True:
				Console.Logs.log(f"Il pacchetto \"{package_name}\" non risulta installato")
			return False

		except Exception as package_installation_error:
			Console.Logs.Errors.fatal_error(f"Durante l'installazione del pacchetto \"{package_name}\" si sono verificati i seguenti errori: \"{package_installation_error}\"")


	@staticmethod
	def install_components(components: str | list[str]) -> None:
		''' Installa componenti Python (librarie e pacchetti) con pip. '''

		if isinstance(components, str):

			components = [components]

		for component in components:

			Console.Logs.log(f"Inizio installazione della componente \"{component}\"")

			if Dependencies.is_library_imported(component) or Dependencies.is_package_installed(component, log = False):
				Console.Logs.Errors.error(f"Impossibile installare la componente \"{component}\" perché risulta gia installata")
				return

			try:
				run_subprocess(["pip", "install", component])

			except Exception as library_installation_error:
				Console.Logs.Errors.fatal_error(f"Durante l'installazione della componente \"{components}\" si sono è verificato il seguente errore: \"{library_installation_error}\"")

			else:
				Console.Logs.log(f"Installata la componente \"{component}\"")

# =================================================================================================================== #

def create_virtual_environment(virtual_environment_path: str = "./" , virtual_environment_name: str = '.venv',*, activate: bool = False) -> None:
	'''
		Crea un ambiente virtuale Python e presso il percorso specificato.
		È possibile specificare in nome dell'ambiente virtuale.
	'''

	virtual_environment_path = os.path.normpath(os.path.join(virtual_environment_path, virtual_environment_name))

	Console.Logs.log(f"Inizio creazione dell'ambiente virtuale presso \"{virtual_environment_path}\"")

	if os.path.exists(virtual_environment_path):
		Console.Logs.Errors.fatal_error(f"Il percorso \"{virtual_environment_path}\" esiste gia")

	try:
		run_subprocess(["python", "-m", "venv", virtual_environment_path])

	except Exception as virtual_environment_creation_error:
		Console.Logs.Errors.fatal_error(f"Durante la creazione dell'ambiente virtuale \"{virtual_environment_path}\" si sono verificati i seguenti errori: \"{virtual_environment_creation_error}\"")

	else:
		Console.Logs.log(f"Creato ambiente virtuale presso \"{virtual_environment_path}\"")

	if activate is True:

		activation_script_path = os.path.normpath(os.path.join(virtual_environment_path, "Scripts", "activate.bat"))

		Console.Logs.log(f"Esecuzione dell script: \"{activation_script_path}\" per l'attivazione dell'ambiente virtuale presso: \"{virtual_environment_path}\"")

		try:
			run_subprocess([activation_script_path], shell = True)

		except Exception as virtual_environment_activation_error:
			Console.Logs.Errors.fatal_error(f"Durante l'attivazione dell'ambiente virtuale \"{virtual_environment_path}\" si sono verificati i seguenti errori: \"{virtual_environment_activation_error}\"")

		else:
			Console.Logs.log(f"Attivato ambiente virtuale presso \"{virtual_environment_path}\"")


def compile_file(file_path: str, executable_name: str, icon_path: str = None) -> None:
	'''
		Compila un file Python in un eseguibile usando Pyinstaller.\n
		È possibile specificare il nome dell'eseguibile.\n
		È possibile specificare l'icona dell'eseguibile.
	'''

	if not Dependencies.is_package_installed('pyinstaller'):
		Console.Logs.Errors.fatal_error("Per la compilazione di un file è necessario il modulo \"Pyinstaller\" che non risulta installato")

	file_path = os.path.normpath(file_path) #TODO: percorso file relativo alla cartella del progetto
	icon_path = os.path.normpath(icon_path)
	executable_name = executable_name.strip()

	if not os.path.exists(file_path):
		Console.Logs.Errors.fatal_error(f"Il percorso: \"{file_path}\" non esiste")

	if not os.path.isfile(file_path):
		Console.Logs.Errors.fatal_error(f"Il percorso: \"{file_path}\" non è un file")

	if not os.path.exists(icon_path):
		Console.Logs.Errors.fatal_error(f"Il percorso: \"{icon_path}\" non esiste")

	if not os.path.isfile(icon_path):
		Console.Logs.Errors.fatal_error(f"Il percorso: \"{icon_path}\" non è un file")

	if executable_name in ("", " ", None):
		Console.Logs.Errors.fatal_error(f"Il nome dell'eseguibile \"{executable_name}\" non è supportato")

	Console.Logs.log(f"Inizio compilazione del file \"{file_path}\"")
	print()

	try:

		if icon_path is not None:
			run_subprocess(["pyinstaller", "./" + file_path, "--onefile", f"--icon={icon_path}", f'--name={executable_name}'])

		else:
			run_subprocess(["pyinstaller", "./" + file_path, "--onefile", f'--name={executable_name}'])

	except CalledProcessError as called_process_error:
		Console.Logs.Errors.fatal_error(f"Durante la compilazione del file \"{file_path}\" si sono verificati i seguenti errori: \"{called_process_error}\"")

	except Exception as compilation_error:
		Console.Logs.Errors.fatal_error(f"Durante la compilazione del file \"{file_path}\" si sono verificati i seguenti errori: \"{compilation_error}\"")

	else:
		Console.Logs.log(f"File \"{file_path}\" compilato con successo")


def execute_executable(executable_path: str) -> None:
	''' Esegue l'eseguibile dato. '''

	if not os.path.exists(executable_path):
		Console.Logs.Errors.fatal_error(f"Impossibile eseguire il file: \"{executable_path}\" perché non esiste")

	if not os.path.isfile(executable_path):
		Console.Logs.Errors.fatal_error(f"Impossibile eseguire il file: \"{executable_path}\" perché non é un file")

	if not os.access(executable_path, os.X_OK):
		Console.Logs.Errors.fatal_error(f"Impossibile eseguire il file: \"{executable_path}\" perché non risulta accessibile")

	if os.path.splitext(executable_path) == '.exe':
		Console.Logs.Errors.fatal_error(f"Impossibile eseguire il file: \"{executable_path}\" perché non è un eseguibile")

	Console.Logs.log(f"Inizio esecuzione dell'eseguibile \"{executable_path}\"")

	try:
		run_subprocess(executable_path)

	except Exception as execution_error:
		Console.Logs.Errors.fatal_error(f"Durante l'esecuzione dell'eseguibile \"{executable_path}\" si sono verificati i seguenti errori: \"{execution_error}\"")

	else:
		Console.Logs.log(f"L'eseguibile \"{executable_path}\" è stato eseguito con successo")
