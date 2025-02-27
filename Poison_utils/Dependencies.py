'''
	Funzionalità per la gestione delle dipendenze e degli import.
'''


import os

import venv
import importlib.util
import subprocess

from Poison_utils import Console, Files


OS_TYPE: str = None


if os.name not in ('posix', 'nt'):
	Console.Logs.error(f"Attenzione il sistema operativo \"{os.name}\" non è supportato")

else:
    OS_TYPE = os.name


def is_library_importable(library_name: str) -> bool:
	'''
		Ritorna vero se una libreria è importabile.\n
		Wrapper di importlib.util.find_spec().
	'''

	spec = importlib.util.find_spec(library_name)

	if spec is None:
		return False

	else:
		return True


def install_component(component: str) -> None:
	'''
		Installa componenti Python (librarie e pacchetti) con pip.\n
		Se components è una stringa, installa solo quella componente.\n
		Se components è una lista, installa tutte le componenti.
	'''

	if Virtual_environment.is_active is False:
		Console.Logs.error("Impossibile installare componenti perché l'ambiente virtuale non è istallato o attivo")
		return


	Console.Logs.log(f"Inizio installazione della componente \"{component}\"")

	if is_library_importable(component):
		Console.Logs.error(f"Impossibile installare la componente \"{component}\" perché risulta gia installata")
		return

	if OS_TYPE == 'posix':
		pip_executable_path = os.path.join(Virtual_environment.path, 'bin', 'pip')

	elif OS_TYPE == 'nt':
		pip_executable_path = os.path.join(Virtual_environment.path, 'Scripts', 'pip')

	try:
		print([pip_executable_path, "install", component])
		subprocess.run([pip_executable_path, "install", component])

	except Exception as library_installation_error:
		Console.Logs.fatal_error(f"Durante l'installazione della componente \"{component}\" si sono è verificato il seguente errore:\n\n\"{library_installation_error}\"")

	else:
		Console.Logs.log(f"Installata la componente \"{component}\"")


class Virtual_environment:
	''' Classe per la gestione degli ambienti virtuali. '''

	is_active: bool = None	# Se è None l'ambiente virtuale non è stato creato
	path: str = None	# Non se non è stato creato un ambiente virtuale

	@staticmethod
	def create_virtual_environment(environment_path: str = None, environment_directory: str = './', environment_name: str = '.venv') -> None:
		''' Crea un ambiente virtuale al percorso e con il nome specificato. '''

		if environment_path is None:
			environment_path = os.path.abspath(os.path.join(environment_directory, environment_name))

		if os.path.exists(environment_path):
			Console.Logs.error(f"Impossibile creare un ambiente virtuale al percorso: \"{environment_path}\" perché già esistente")
			return

		venv.create(environment_path)
		Files.File(".gitignore").write(f"{environment_name}\n")	#* Creazione del file .gitignore per ignorare l'ambiente virtuale.
		Virtual_environment.is_active = False
		Virtual_environment.path = environment_path
		Console.Logs.log(f"Ambiente virtuale creato con successo presso: \"{environment_path}\"")


	@staticmethod
	def activate_virtual_environment(environment_path: str = None) -> None:
		''' Attiva un ambiente virtuale. '''

		if environment_path is None:
			environment_path = Virtual_environment.path

		if not os.path.exists(environment_path):
			Console.Logs.error(f"Impossibile attivare l'ambiente virtuale al percorso \"{environment_path}\" perché non esistente")
			return

		if OS_TYPE == 'posix':
			activation_command: str = f"source {os.path.join(environment_path, 'bin', 'activate')}"
			executables_directory_path: str = "/bin/bash"

		elif OS_TYPE == 'nt':
			activation_command = f"{os.path.join(environment_path, 'Scripts', 'activate.bat')}"
			executables_directory_path: str = None

		else:
			Console.Logs.error(f"Impossibile attivare l'ambiente virtuale perché il sistema operativo \"{OS_TYPE}\" non è supportato")
			return

		try:
			subprocess.run (	#* Esecuzione del comando di attivazione dell'ambiente virtuale.
				activation_command,
				shell = True,
				check = True,
				executable = executables_directory_path
			)

		except subprocess.CalledProcessError as activation_error:
			Console.Logs.fatal_error(f"Durante l'attivazione dell'ambiente virtuale \"{environment_path}\" la chiamata del sotto-processo ha generato il seguente errore :\n\n\"{activation_error}\"")

		except Exception as activation_error:
			Console.Logs.fatal_error(f"Durante l'attivazione dell'ambiente virtuale \"{environment_path}\" si è verificato il seguente errore:\n\n\"{activation_error}\"")

		else:
			Virtual_environment.is_active = True
			Console.Logs.log(f"Ambiente virtuale presso \"{environment_path}\" attivato con successo")
