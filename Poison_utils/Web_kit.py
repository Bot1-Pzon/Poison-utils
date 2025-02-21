'''
	Funzionalità per lo sviluppo di server web.
'''


import os

from Poison_utils import Console


STATIC_RESOURCES_PATH = None

@staticmethod
def config(*, statics_path: str = 'statics') -> None:
	'''
		Metodo di configurazione della funzionalità Web_kit.\n
		- È possibile specificare il percorso delle risorse statiche.
	'''

	if os.path.exists(statics_path):
		STATIC_RESOURCES_PATH = statics_path

	else:
		Console.Logs.fatal_error(f"Il percorso \"{statics_path}\" non esiste")


@staticmethod
def render_page(page_file_name: str) -> str:
	'''
		Funzionalità che permette il rendering di documenti ".html" specificando il nome del file.
		- page_file_name: Nome del file della pagina che si intende caricare.
	'''

	page_file_path = os.path.normpath(os.path.join(STATIC_RESOURCES_PATH, page_file_name.strip()))


	if not os.path.exists(page_file_path):	# Se il percorso file della pagina non esiste:
		Console.Logs.error(f"Errore: \"{page_file_path}\" non esiste")
		return f'Errore: "{page_file_path}" non esiste.'

	elif not os.path.isfile(page_file_path):	# Se il percorso file della pagina non è un file:
		Console.Logs.error(f"Errore: \"{page_file_path}\" non è un file")
		return f'Errore: "{page_file_path}" non è un file.'

	elif not os.path.splitext()(2) == '.html':	# Se il file non è un documento ".html":
		Console.Logs.error(f"Errore: \"{page_file_path}\" non è un documento \".html\"")
		return f'Errore: "{page_file_path}" non è un documento ".html".'

	else:
		with open(page_file_path, "r") as page_file:
			page_content = page_file.read()	#* Rendering della pagina.

		Console.Logs.log(f"Pagina \"{page_file_name}\" caricata da: \"{page_file_path}\" con successo.")
		return page_content
