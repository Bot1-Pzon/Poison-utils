<body>
	<div>
		<h1>Poison's Utilities</h1>

<p>
			<strong>Poison's Utilities</strong> è un
			<a href="https://docs.python.org/3/tutorial/modules.html">modulo</a> sviluppato da <a href="https://github.com/Bot1-Pzon">Poison_8o8</a>  a scopo quasi esclusivamente
			didattico, è scritto in <a href="https://www.python.org/">python</a> e contiene varie funzionalità.
		</p>
	</div>

<h2>Funzionalità</h2>

<ol>
	<li>
		<!-- Colori -->
		<div>
			<h3>Gestione dei colori a terminale <code>Colors</code></h3>

<p>Funzionalità per manipolare l'output del terminale, ad esempio con la stampa colorata.</p>

<ul>
				<li>Ripristinare la formattazione <code>Colors.reset</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.bold</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.disable</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.underline</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.blink</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.reverse</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.strike_through</code>.</li>
				<li>Rendere il testo grassetto <code>Colors.invisible</code>.</li>

<li>
					<h4>Colore del testo <code>Colors.fg</code></h4>
					<ul>
						<li>Bianco <code>Colors.fg.white</code>.</li>
						<li>Nero <code>Colors.fg.black</code>.</li>
						<li>Rosso <code>Colors.fg.red</code>.</li>
						<li>Verde <code>Colors.fg.green</code>.</li>
						<li>Arancio <code>Colors.fg.orange</code>.</li>
						<li>Blue <code>Colors.fg.blue</code>.</li>
						<li>Viola <code>Colors.fg.purple</code>.</li>
						<li>Ciano <code>Colors.fg.cyan</code>.</li>
						<li>Verde chiaro <code>Colors.fg.light_grey</code>.</li>
						<li>Verde scuro <code>Colors.fg.dark_grey</code>.</li>
						<li>Rosso chiaro <code>Colors.fg.light_red</code>.</li>
						<li>Verde chiaro <code>Colors.fg.light_green</code>.</li>
						<li>Giallo <code>Colors.fg.yellow</code>.</li>
						<li>Blu chiaro <code>Colors.fg.light_blue</code>.</li>
						<li>Rosa <code>Colors.fg.pink</code>.</li>
						<li>Ciano chiaro <code>Colors.fg.light_cyan</code>.</li>
					</ul>
				</li>
				<li>
					<h4>Colore dello sfondo <code>Colors.bg</code></h4>
					<ul>
						<li>Nero <code>Colors.bg.black</code>.</li>
						<li>Rosso <code>Colors.bg.red</code>.</li>
						<li>Verde <code>Colors.bg.green</code>.</li>
						<li>Arancio <code>Colors.bg.orange</code>.</li>
						<li>Blue <code>Colors.bg.blue</code>.</li>
						<li>Viola <code>Colors.bg.purple</code>.</li>
						<li>Bianco <code>Colors.bg.white</code>.</li>
						<li>Ciano <code>Colors.bg.cyan</code>.</li>
						<li>Verde scuro <code>Colors.bg.dark_grey</code>.</li>
					</ul>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- Console -->
		<div>
			<h3>Interazione con la console <code>Console</code></h3>
			<p>Funzionalità per facilitare l'interazione con il terminale.</p>

<ul>
				<li>
					<h4>Gestione degli errori non fatali <code>Console.error()</code></h4>
				</li>
				<li>
					<h4>Gestione degli errori fatali <code>Console.fatal_error()</code></h4>
				</li>
				<li>
					<h4>Creazione della cartella per i log <code>Console.create_logs_folder()</code></h4>
				</li>
				<li>
					<h4>Configurazione della console <code>Console.config()</code></h4>
				</li>
				<li>
					<h4><code>Console.log()</code></h4>
				</li>
				<li>
					<h4><code>Console.stop()</code></h4>
				</li>
				<li>
					<h4><code>Console.clear()</code></h4>
				</li>
				<li>
					<h4><code>Console.del_lines()</code></h4>
				</li>
				<li>
					<h4><code>Console.function_timer()</code></h4>
				</li>
				<li>
					<h4><code>Console.create_virtual_environment()</code></h4>
				</li>
				<li>
					<h4><code>Console.file_path_input()</code></h4>
				</li>
				<li>
					<h4><code>Console.Cursor</code></h4>
					<ul>
						<li>
							<h5><code>Console.Cursor.move_to()</code></h5>
						</li>
						<li>
							<h5><code>Console.Cursor.reset()</code></h5>
						</li>
					</ul>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- File -->
		<div>
			<h3>Gestione  comprensibile dei file <code>File</code></h3>
			<p>Funzionalità per la gestione e interazione con i file.</p>

<ul>
				<li>
					<h4>Inizializzazione di un File <code>File.__init__()</code></h4>
				</li>
				<li>
					<h4>Scrittura a file <code>File.write()</code></h4>
				</li>
				<li>
					<h4>Eliminazione di un file oggetto <code>File.delete()</code></h4>
				</li>
				<li>
					<h4>Rappresentazione in stringa di un file <code>File.__str__()</code></h4>
				</li>
				<li>
					<h4>Esistenza di un percorso file <code>File.path_exist()</code></h4>
				</li>
				<li>
					<h4>Creazione di un percorso file <code>File.create_complete_path()</code></h4>
				</li>
				<li>
					<h4>Eliminazione di un file <code>File.delete_file_at_path()</code></h4>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- Web_kit -->
		<div>
			<h3>Funzionalità per l'implementazione di server web <code>Web_kit</code></h3>
			<p>Funzionalità per lo sviluppo di server web: caricamento di un documento.</p>
			<ul>
				<li>
					<h4>Configurazione <code>Web_kit.config()</code></h4>
				</li>
				<li>
					<h4>Render delle pagine <code>Web_kit.page_render()</code></h4>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- Liste -->
		<div>
			<h3>Liste <code>List</code></h3>
			<p>Funzionalità per la gestione di liste.</p>
			<ul>
				<li>
					<h4>Creazione di una lista casuale <code>List.create_random_list()</code></h4>
				</li>
				<li>
					<h4>Riordinamento della lista <code>List.bubble_sort()</code></h4>
				</li>
				<li>
					<h4>Riordinamento della lista 2 <code>List.jenky_sort()</code></h4>
				</li>
				<li>
					<h4>Contatore dui duplicati nelle liste <code>List.duplicates_counter()</code></h4>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- Matematica -->
		<div>
			<h3>Funzioni matematiche <code>Math</code></h3>
			<p>Funzionalità per l'implementazione di varie funzioni matematiche.</p>
			<ul>
				<li>
					<h4>Funzione per il calcolo del fattoriale <code>Math.factorial()</code></h4>
				</li>
				<li>
					<h4>Funzione per il calcolo della serie di Fibonacci <code>Math.fibonacci()</code></h4>
				</li>
			</ul>
		</div>
	</li>
	<li>
		<!-- Fisica -->
		<div>
			<h3>Calcoli con le grandezze fisiche <code>Physic</code></h3>
			<p>Classe per il calcolo con grandezze fisiche tenendo conto delle incertezze.</p>
			<ul>
				<li>
					<h4>Inizializzazione <code>Physic.__init__()</code></h4>
				</li>
				<li>
					<h4>Somma <code>Physic.__add__()</code></h4>
				</li>
				<li>
					<h4>Sottrazione <code>Physic.__sub__()</code></h4>
				</li>
				<li>
					<h4>Moltiplicazione <code>Physic.__mul__()</code></h4>
				</li>
				<li>
					<h4>Divisione <code>Physic.__truediv__()</code></h4>
				</li>
				<li>
					<h4>Rappresentazione in stringa <code>Physic.__str__()</code></h4>
				</li>
			</ul>
		</div>
	</li>
</ol>
</body>
