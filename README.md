<body>
<main class="markdown-body">
<header>
<h1>Poison's Utilities</h1>

<p>
<strong>Poison's Utilities</strong>
<a href="https://docs.python.org/3/tutorial/modules.html">modulo</a> sviluppato da
<a href="https://github.com/Bot1-Pzon">Poison_8o8</a> a scopo quasi esclusivamente didattico, è scritto in
<a href="https://www.python.org/">python</a> e contiene varie funzionalità.
</p>
</header>

<h2>Funzionalità</h2>

<ol>
<!-- Console -->
<li>
<h3>Interazione con la console <code>Console</code></h3>
<p>Funzionalità per facilitare l'interazione con il terminale.</p>

<ul>
<li>
<h4>Configurazione della console <code>Console.config()</code></h4>
<p>
Metodo di configurazione della funzionalità Console.<br /><br />

È possibile attivare il debug: "<code>Console.config(debug=True)</code>".<br />
È possibile attivare i logs: "<code>Console.config(logs=True)</code>".<br />
È possibile specificare il percorso presso il quale si desidera venga creata la cartella
contenente i file edi log: "<code>Console.config(logs_file_path = "...")</code>". <br />
È possibile specificare il metodo di pulizia dello schermo compatibile con la console:<br />
"<code>Console.config(screen_cleaning_method="...")</code>", (sono disponibili
<code>"auto"</code>, <code>"cls"</code> e <code>"clear"</code>). <br />
È possibile attivare l'output colorato: "<code>Console.config(colored_output=True)</code>".
</p>
</li>
<li>
<h4>Pulizia del terminale <code>Console.clear()</code></h4>
<p>
Pulisce il terminale.<br />
Wrapper di <code>os.system('clear')</code> o <code>os.system('cls')</code> a seconda del sistema
operativo.
</p>
</li>
<li>
<h4>Interruzione del programma <code>Console.stop()</code></h4>
<p>
Arresta il programma.<br />
Wrapper di <code>sys.exit()</code>.
</p>
</li>

<!-- Colori -->
<li>
<h4>Gestione dei colori a terminale <code>Console.Colors</code></h4>
<p>Funzionalità per manipolare l'output del terminale, ad esempio con la stampa colorata.</p>
<ul>
<li>Ripristinare la formattazione <code>Console.Colors.reset</code>.</li>
<li>Rendere il testo grassetto <code>Console.Colors.bold</code>.</li>
<li>Disabilitare il testo <code>Console.Colors.disable</code>.</li>
<li>Rendere il testo sottolineato <code>Console.Colors.underline</code>.</li>
<li>Rendere il testo intermittente <code>Console.Colors.blink</code>.</li>
<li>? <code>Console.Colors.reverse</code>.</li>
<li>? <code>Console.Colors.strike_through</code>.</li>
<li>Rendere il testo invisibile <code>Console.Colors.invisible</code>.</li>
<li>
<h5>Colore del testo <code>Console.Console.Colors.fg</code></h5>
<ul>
<li>Bianco <code>Console.Colors.fg.white</code>.</li>
<li>Nero <code>Console.Colors.fg.black</code>.</li>
<li>Rosso <code>Console.Colors.fg.red</code>.</li>
<li>Verde <code>Console.Colors.fg.green</code>.</li>
<li>Arancio <code>Console.Colors.fg.orange</code>.</li>
<li>Blue <code>Console.Colors.fg.blue</code>.</li>
<li>Viola <code>Console.Colors.fg.purple</code>.</li>
<li>Ciano <code>Console.Colors.fg.cyan</code>.</li>
<li>Verde chiaro <code>Console.Colors.fg.light_grey</code>.</li>
<li>Verde scuro <code>Console.Colors.fg.dark_grey</code>.</li>
<li>Rosso chiaro <code>Console.Colors.fg.light_red</code>.</li>
<li>Verde chiaro <code>Console.Colors.fg.light_green</code>.</li>
<li>Giallo <code>Console.Colors.fg.yellow</code>.</li>
<li>Blu chiaro <code>Console.Colors.fg.light_blue</code>.</li>
<li>Rosa <code>Console.Colors.fg.pink</code>.</li>
<li>Ciano chiaro <code>Console.Colors.fg.light_cyan</code>.</li>
</ul>
</li>
<li>
<h5>Colore dello sfondo <code>Console.Console.Colors.bg</code></h5>
<ul>
<li>Nero <code>Console.Colors.bg.black</code>.</li>
<li>Rosso <code>Console.Colors.bg.red</code>.</li>
<li>Verde <code>Console.Colors.bg.green</code>.</li>
<li>Arancio <code>Console.Colors.bg.orange</code>.</li>
<li>Blue <code>Console.Colors.bg.blue</code>.</li>
<li>Viola <code>Console.Colors.bg.purple</code>.</li>
<li>Bianco <code>Console.Colors.bg.white</code>.</li>
<li>Ciano <code>Console.Colors.bg.cyan</code>.</li>
<li>Verde scuro <code>Console.Colors.bg.dark_grey</code>.</li>
</ul>
</li>
</ul>
</li>

<!-- Logging -->
<li>
<h4>Sistema di Logging <code>Console.Logs</code></h4>
<p>Funzionalità per il logging di informazioni, sia a terminale che a file.</p>
<ul>
<li>
<h5>Creazione della cartella per i log <code>Console.Logs.create_logs_folder()</code></h5>
<p>Crea la cartella e i file di log.</p>
</li>
<li>
<h5>Scrittura nel file di log <code>Console.Log.rite_to_log_files()</code></h5>
<p>Scrive ai vari file di log.</p>
</li>
<li>
<h5>Strumento di logging <code>Console.Logs.log()</code></h5>
<p>
Stampa di informazioni utili a terminale a fini di debug, abilitatile con
<code>Console.config(debug = True)</code>.<br />
Il parametro <code>show_to_console</code> sovrascriverà la configurazione solo per
l'istanza dove la sua funzione è stata chiamata.
</p>
</li>
<li>
<h5>Timer delle funzioni <code>Console.Logs.function_timer()</code></h5>
<p>Misura e logga il tempo di esecuzione di una funzione.</p>
</li>
<li>
<h5>Gestione degli errori <code>Console.Logs.Errors</code></h5>
<p>Sottoclasse per la gestione degli errori.</p>
<ul>
<li>
<h6>Errore non fatali <code>Console.Logs.Errors.error()</code></h6>
<p>
Logga un errore non fatale.<br />
Per presentare errori fatali usare:
<code>Console.Logs.Errors.fatal_error()</code>.
</p>
</li>
<li>
<h6>Errore fatali <code>Console.Logs.Errors.fatal_error()</code></h6>
<p>
Logga un errore fatale e interrompe il programma.<br />
Per presentare errori non fatali usare:
<code>Console.Logs.Errors.error()</code>.<br />
Wrapper di: <code>raise Exception(error_message)</code>.
</p>
</li>
</ul>
</li>

<!-- Cursore -->
<li>
<h5>Interazione col cursore <code>Console.Cursor</code></h5>
<p>Sottoclasse per l'interazione con il cursore.</p>
<ul>
<li>
<h6>Spostamento del cursore <code>Console.Cursor.move_to()</code></h6>
<p>Sposta il cursore del terminale alle coordinate date.</p>
</li>
<li>
<h6>Riposizionamento del cursore <code>Console.Cursor.reset()</code></h6>
<p>Riposiziona il cursore nella posizione iniziale.</p>
</li>
<li>
<h6>Eliminazione di linee <code>Console.Cursor.del_lines()</code></h6>
<p>Cancella il numero dato di linee dal terminale.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>

<!-- File -->
<li>
<h3>Gestione comprensibile dei file <code>File</code></h3>
<p>Funzionalità per la gestione e interazione con i file.</p>

<ul>
<li>
<h4>Inizializzazione di un File <code>File.__init__()</code></h4>
</li>
<li>
<h4>Scrittura a file <code>File.write()</code></h4>
<p>Scrittura a file.</p>
</li>
<li>
<h4>Eliminazione di un file <code>File.delete()</code></h4>
<p>Elimina il file e la sua istanza associata.</p>
</li>
<li>
<h4>Rappresentazione in stringa <code>File.__str__()</code></h4>
</li>
<li>
<h4>Esistenza di un percorso file <code>File.path_exist()</code></h4>
<p>
Ritorna True se il percorso esiste.<br />
Wrapper di <code>os.path.exists()</code>.
</p>
</li>
<li>
<h4>Creazione di un percorso file <code>File.create_complete_path()</code></h4>
<p>
Crea il percorso completo di cartelle e file.<br />
Se si desidera creare solo cartelle non specificare "<code>file_name</code>".
</p>
</li>
<li>
<h4>Eliminazione di un file <code>File.delete_file_at_path()</code></h4>
<p>
Elimina il file al percorso dato.<br />
wrapper di <code>os.remove()</code>.
</p>
</li>
<li>
<h4>Spostamento di un file <code>File.move_file()</code></h4>
<p>Sposta il file dal percorso specificato a quello dato.</p>
</li>
</ul>
</li>

<!-- Robe Web -->
<li>
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
</li>

<!-- Liste -->
<li>
<h3>Interazione con le Liste <code>List</code></h3>
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
</li>

<!-- Matematica -->
<li>
<h3>Funzioni matematiche <code>Math</code></h3>
<p>Funzionalità per l'implementazione di varie funzioni matematiche.</p>
<ul>
<li>
<h4>Funzione per il calcolo del fattoriale <code>Math.factorial()</code></h4>
<p>Ritorna il fattoriale del numero dato.</p>
</li>
<li>
<h4>Funzione per il calcolo della serie di Fibonacci <code>Math.fibonacci()</code></h4>
<p>Ritorna l'n-esimo numero nella sequenza di Fibonacci.</p>
</li>
<li>
<h4>Se un numero è primo <code>Math.is_prime()</code></h4>
<p>Ritorna vero se un numero è primo.</p>
</li>
</ul>
</li>

<!-- Fisica -->
<li>
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
</li>

<!-- Dipendenze -->
<li>
<h3>Calcoli con le grandezze fisiche <code>Dependencies</code></h3>
<p>Classe per la gestione delle dipendenze.</p>
<ul>
<li>
<h4>Verifica dell'importazione di una libreria <code>Dependencies.is_library_imported()</code></h4>
<p>Ritorna vero se una libreria è installata.</p>
</li>
<li>
<h4>
Verifica dell'installazione di una pacchetto <code>Dependencies.is_package_installed()</code>
</h4>
<p>Ritorna vero se un pacchetto Python risulta installato.</p>
</li>
</ul>
</li>
<li>
<h3>Creazione di un ambiente virtuale<code>create_virtual_environment()</code></h3>
<p>
Crea un ambiente virtuale Python e presso il percorso specificato.<br />
È possibile specificare in nome dell'ambiente virtuale.
</p>
</li>
<li>
<h3>Compilazione di un file <code>compile_file()</code></h3>
<p>
Compila un file Python in un eseguibile usando Pyinstaller.<br />
È possibile specificare il nome dell'eseguibile.<br />
È possibile specificare l'icona dell'eseguibile.
</p>
</li>
<li>
<h3>Esecuzione di un eseguibile <code>execute_executable()</code></h3>
<p>Esegue l'eseguibile dato.</p>
</li>
</ol>
</main>
</body>
