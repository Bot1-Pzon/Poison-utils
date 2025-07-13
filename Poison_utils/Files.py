'''
	Funzionalità per la gestione e interazione con i file.
'''


import os

import shutil

from Poison_utils import Console


class File:
	'''
		Classe per la gestione dei file.

		Sull'istanza di questa classe è possibile:
		- Leggere il contenuto del file.
		- Scrivere al file.
		- Eliminare il file (L'istanza verrà eliminata).
	'''

	path: str
	name: str
	extension: str
	directory_name: str

	def __init__(self, path: str) -> None:


		if not os.path.exists(path):	# Se il percorso file non esiste:
			try:
				file = open(path, "x")	#* Crea il file.
				file.close()

			except Exception as file_handling_error:
				Console.Logs.fatal_error(f"Durante la creazione del file: \"{path}\" si è verificato il seguente errore:\n\n\"{file_handling_error}\"")

			else:
				Console.Logs.log(f'File: "{path}" creato')

		if not os.path.isfile(path):	# Se il percorso non punta ad un file:
			Console.Logs.error(f"Il percorso file: \"{path}\" non punta ad un file")
			return

		self.path = os.path.normpath(os.path.realpath(path))

		self.name = os.path.basename(self.path)

		self.extension = os.path.splitext(self.path)[1]

		self.directory_name = os.path.basename(os.path.dirname(self.path))

		try:
			with open(self.path, "r") as file:
				self.content = file.read()

		except Exception as file_reading_error:
			Console.Logs.fatal_error(f"Durante la lettura del file \"{self.path}\" si è verificato il seguente errore:\n\n\"{file_reading_error}\"")


	def write(self, content: str, binary: bool = False) -> None:

		self.content = content

		if binary is True:
			writing_method = "wb"
			encoding = None
			content = content.encode()

		else:
			writing_method = "w"
			encoding = 'utf-8'

		with open(self.path, writing_method, encoding = encoding) as file:
			file.write(content)	#* Scrittura a file.

		if len(content) > 25:
			Console.Logs.log(f"Scrittura al file \"{self.path}\" completata")

		else:
			content = content.encode()
			Console.Logs.log(f"Scrittura di \"{content}\" al file \"{self.path}\" completata")


	def delete(self) -> None:
		''' Elimina il file e la sua istanza associata. '''

		os.remove(self.path)	#* Eliminare il file.
		Console.Logs.log(f'File "{self.path}" eliminato')
		del self	#* Eliminare l'istanza.


	def __str__(self) -> str:
		''' rappresenta in stringa di un file, comprende il suo nome e percorso. '''
		return f"[{self.name} -> '{self.path}']"


def path_exist(path: str) -> bool:
	'''
		Ritorna True se il percorso esiste.\n
		Wrapper di "os.path.exists()".
	'''
	return os.path.exists(path)


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
		Console.Logs.fatal_error(f"Il percorso \"{path}\" esiste gia")	#* Lancia un errore.

	if not os.path.exists(os.path.dirname(path)):	# Se la cartella contenitrice non esiste:
		os.makedirs(os.path.dirname(path))	#* Creazione cartella contenitrice.
		Console.Logs.log(f"Cartella \"{os.path.dirname(path)}\" creata")

	if file_name is None:
		os.makedirs(path)
		Console.Logs.log(f'Cartella "{path}" creata')

	else:
		try:
			file = open(path, "x")	#* Creazione del file.
			file.close()

		except Exception as file_handling_error:
			Console.Logs.fatal_error(f"Durante la creazione del file: \"{path}\" si è verificato il seguente errore:\n\n\"{file_handling_error}\"")

		else:
			Console.Logs.log(f'File "{path}" creato')
			return File(path)


def delete_file_at_path(path: str, log_it: bool = True) -> None:
	'''
		Elimina il file o la cartella al percorso dato.

		Wrapper di "os.remove()".
	'''

	if not os.path.exists(path):	# Se il percorso non esiste:
		Console.Logs.error(f"Impossibile eliminare il \"{path}\" perché non esiste")
		return

	elif os.path.isfile(path):
		is_file = True

	elif os.path.isdir(path):
		is_file = False

	else:
		Console.Logs.fatal_error(f"Il percorso \"{path}\" non è stato riconosciuto ne come file ne come cartella")

	if is_file is True:

		try:
			os.remove(path)	#* Eliminazione del file.

		except Exception as file_handling_error:
			Console.Logs.fatal_error(f"Durante l'eliminazione del file \"{path}\" si è verificato il seguente errore:\n\n\"{file_handling_error}\"")

		else:
			if log_it is True:
				Console.Logs.log(f"File \"{path}\" eliminato")

	else:
		try:
			shutil.rmtree(path)	#* Eliminazione della cartella.

		except Exception as directory_elimination_error:
			Console.Logs.fatal_error(f"Durante l'eliminazione della cartella \"{path}\" si è verificato il seguente errore:\n\n\"{directory_elimination_error}\"")

		else:
			if log_it is True:
				Console.Logs.log(f"Cartella \"{path}\" eliminata")


def move_file(from_path: str, to_path: str) -> None:
	'''
		Sposta il file dal percorso specificato a quello dato.
		Wrapper di "shutil.move()".
	'''

	if not os.path.exists(from_path):	# Se il percorso da muovere non esiste:
		Console.Logs.fatal_error(f"Il percorso \"{from_path}\" non esiste")

	if not os.path.isfile(from_path):	# Se il percorso da muovere non rappresenta un file:
		Console.Logs.fatal_error(f"Il percorso \"{from_path}\" non rappresenta un file")

	if os.path.exists(to_path):	# Se il percorso di destinazione esiste:
		Console.Logs.error(f"Impossibile spostare (\"{from_path}\" -> \"{to_path}\") in quanto gia presente alla destinazione")

	try:
		shutil.move(from_path, to_path)

	except Exception as file_handling_error:
		Console.Logs.fatal_error(f"Durante il movimento del file (\"{from_path}\" -> \"{to_path}\") si è verificato il seguente errore:\n\n\"{file_handling_error}\"")

	else:
		Console.Logs.log(f"Avvenuto spostamento file: (\"{from_path}\" -> \"{to_path}\")")


def copy_file(from_path: str, to_path: str) -> None:
	'''
		Copia il file del percorso specificato a quello dato.
		Wrapper di "shutil.copy()".
	'''

	if not os.path.exists(from_path):	# Se il percorso da copiare non esiste:
		Console.Logs.fatal_error(f"Il percorso \"{from_path}\" non esiste")

	if os.path.exists(to_path):	# Se il percorso di destinazione esiste:
		Console.Logs.error(f"Impossibile copiare (\"{from_path}\" -> \"{to_path}\") in quanto gia presente alla destinazione")

	try:
		shutil.copy(from_path, to_path)

	except Exception as file_copying_error:
		Console.Logs.fatal_error(f"Durante la copiatura del file (\"{from_path}\" -> \"{to_path}\") si è verificato il seguente errore:\n\n\"{file_copying_error}\"")

	else:
		Console.Logs.log(f"Avvenuta copiatura file: (\"{from_path}\" -> \"{to_path}\")")


def get_file_extension(file_path: str) -> str:
	'''
		Ritorna l'estensione del file al percorso specificato.
		Se il percorso non punta ad un file ritorna una stringa vuota.
	'''

	if not os.path.isfile(file_path):	# Se il percorso non punta ad un file:
		return ""

	return os.path.splitext(file_path)[1]	#* Ritorna l'estensione del file.
