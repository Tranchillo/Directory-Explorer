# Directory Explorer

Uno strumento Python per generare una rappresentazione testuale della struttura delle directory, progettato specificamente per facilitare la comunicazione con LLMs (ChatGPT, Claude) durante lo sviluppo di progetti.

## Caso d'Uso Principale
Questo strumento è stato sviluppato specificamente per facilitare l'interazione con i Large Language Models (LLM) come Claude, ChatGPT o altri assistenti AI. Quando si lavora su progetti complessi, come lo sviluppo di siti web o applicazioni, spesso è necessario comunicare agli LLM la struttura esatta delle directory del proprio progetto.

Lo script genera automaticamente una rappresentazione testuale chiara e gerarchica dell'organizzazione delle cartelle e dei file, che può essere facilmente copiata e incollata nelle conversazioni con gli LLM. Questo permette agli assistenti AI di:
- Comprendere meglio l'architettura del progetto
- Fornire suggerimenti più pertinenti e contestualizzati
- Identificare potenziali problemi organizzativi
- Proporre ottimizzazioni nella struttura dei file

È particolarmente utile durante:
- La fase di sviluppo di siti web
- La riorganizzazione di progetti esistenti
- La richiesta di consulenza sulla struttura dei file
- La documentazione della struttura del progetto

## Funzionalità
- Esplorazione ricorsiva delle directory
- Ordinamento alfabetico di file e cartelle
- Formattazione gerarchica con indentazione
- Gestione degli errori per cartelle inaccessibili
- Supporto Unicode (UTF-8)
- Esclusione automatica delle directory dell'ambiente virtuale ('venv') per:
  - Ridurre l'utilizzo non necessario di token durante la condivisione con gli LLM
  - Mantenere l'output focalizzato sui file rilevanti del progetto
  - Migliorare la leggibilità escludendo file di build e dipendenze
  - Ottimizzare la visualizzazione della struttura per scopi di sviluppo

## Prerequisiti
- Python 3.x
- Nessuna dipendenza esterna richiesta (usa solo moduli della libreria standard Python)

## Installazione e Utilizzo
1. Scarica il file `directory-explorer.py`
2. Posiziona il file nella directory che desideri esplorare
3. Apri un terminale o prompt dei comandi
4. Naviga fino alla directory:
   ```bash
   cd percorso/alla/tua/directory
   ```
5. Esegui lo script:
   ```bash
   python directory-explorer.py
   ```

Lo script genererà un file `struttura_directory.txt` nella stessa directory, contenente la struttura completa.

## Esempio di Output
```
Struttura completa della directory: C:/esempio
|-- documenti/
    |-- progetto1/
        |-- file1.txt
        |-- file2.pdf
    |-- note.txt
|-- immagini/
    |-- foto1.jpg
    |-- foto2.png
|-- readme.md
```

## Note e Limitazioni
### Note
- Le directory sono indicate con una "/" alla fine
- In caso di errori nell'accesso a specifiche directory, verrà mostrato un messaggio di errore nel report
- Il file di output viene sempre salvato in formato UTF-8
- La directory 'venv' viene automaticamente saltata e contrassegnata come [Saltato] nell'output
- I contenuti dell'ambiente virtuale sono esclusi per ottimizzare l'output per le comunicazioni con gli LLM

### Limitazioni
- Non mostra le dimensioni dei file
- Non mostra le date di modifica
- Non ignora file o cartelle nascosti

### Messaggi di Errore Comuni
- "Permission denied": Lo script non ha i diritti di accesso a una directory
- "File not found": Il percorso specificato non esiste
- "Path too long": Il percorso supera il limite massimo di lunghezza del sistema

## Miglioramenti Futuri
- Visualizzazione delle dimensioni dei file
- Data dell'ultima modifica
- Opzione per ignorare cartelle/file specifici
- Esportazione in diversi formati (JSON, XML)
- Argomenti da riga di comando per la personalizzazione

## Contribuire
Sentiti libero di:
1. Fork del repository
2. Creare un branch per le tue modifiche
3. Inviare una pull request

## Licenza
Questo progetto è distribuito con licenza MIT. Sentiti libero di utilizzarlo e modificarlo come preferisci.
