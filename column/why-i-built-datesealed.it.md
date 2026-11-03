title: Perché ho creato DateSealed: una nota dello sviluppatore
description: È nato dal voler proteggere le foto degli immobili dalle copie. Cosa ho trovato e le regole che mi sono dato per un registro gratuito che neanche io posso riscrivere.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed è uno strumento gratuito che registra quando esisteva un testo, una foto o una pagina web. Sono Yuki Nakazawa e l'ho sviluppato io. In questa nota racconto perché, e quali scelte ho fatto lungo la strada.

## Tutto è cominciato con le foto degli immobili

Gestisco un'agenzia immobiliare in Giappone: fotografiamo gli immobili e pubblichiamo gli annunci. Volevo essere pronto per il giorno in cui qualcuno avesse ritoccato una di quelle foto o l'avesse pubblicata su un altro sito, e poter dimostrare che l'originale era nostro ed esisteva prima.

Avevo i file originali, e i miei post avevano una data. Ma potevo modificarle tutte io stesso, e chiunque avesse una copia poteva rivendicare le stesse date. Mi serviva una data annotata da **qualcuno che non fossi io**, in una forma che **nessuno potesse cambiare dopo**.

## Cosa ho trovato all'inizio

Ho guardato cosa c'era in Giappone a novembre 2026:

- **Data certa presso un notaio.** 700 yen a documento. Esiste una versione elettronica, ma accetta solo file di testo, PDF e XML fino a 10 MB, e la procedura si svolge nei giorni feriali.
- **Registrazione presso l'Agenzia per gli affari culturali.** 3.000 yen per opera, su carta e una alla volta. Fa presumere che l'opera sia stata pubblicata alla data registrata.
- **Marche temporali di fornitori accreditati dal Ministero degli affari interni e delle comunicazioni.** Sono quelle con un riconoscimento ufficiale in Giappone, con prezzi pensati soprattutto per le aziende.
- **Servizi di registrazione su blockchain.** Quelli che ho trovato erano per aziende, oppure a pagamento.
- **Firme nella fotocamera (C2PA).** Alcune fotocamere firmano la foto al momento dello scatto. Questo dice da dove viene un file, che è una domanda diversa da quando esisteva.

Sono tutte soluzioni utili e, per la cosa che davvero devi proteggere, conviene usarle. Ma pagare e fare una pratica per ogni nuova foto o articolo non è realistico. Io volevo qualcosa di **gratuito, senza registrazione, senza caricare nulla, conservato dove nemmeno il gestore possa riscriverlo e automatico su WordPress a ogni pubblicazione**. Non l'ho trovato, quindi l'ho costruito.

## Le regole che mi sono dato

### Ricevere solo un hash

DateSealed riceve soltanto l'hash SHA-256 del tuo file o testo, un'impronta di 64 caratteri. L'hash viene calcolato nel tuo browser, quindi foto e bozze non lasciano mai il tuo computer. Ciò che si vuole registrare è proprio il lavoro non ancora pubblicato, e doverlo consegnare per farlo registrare non avrebbe senso.

### Non dovresti essere costretto a fidarti di me

Ogni registrazione riceve due date. Una è una marca temporale RFC 3161 firmata dall'autorità di marcatura temporale di DateSealed, restituita subito. L'altra viene ancorata in un blocco di Bitcoin tramite OpenTimestamps, di solito entro poche ore.

La prima vale quanto la mia parola. La seconda non dipende da me. Una volta ancorata, puoi verificare la data con il solo file di prova (`.ots`) e il registro di Bitcoin, anche se DateSealed sparisse. Ogni pagina di registrazione riporta i comandi per verificarla sul tuo computer.

La chiave radice dell'autorità di marcatura temporale è stata generata sul mio computer ed è conservata cifrata con una passphrase. Sul server c'è solo la chiave di firma.

### Mai cancellare, mai riscrivere

Neppure le schermate di amministrazione permettono di cancellare una registrazione o di cambiarne l'hash o l'ora. Un registro vale qualcosa solo se chi lo tiene non può toccarlo. Quando aggiorni un post, la registrazione precedente resta e se ne aggiunge una nuova. Il plugin per WordPress segue la stessa regola.

### Dire subito cosa non può fare

Una registrazione mostra che, in quel momento, esistevano dati corrispondenti all'hash. Niente di più. Non mostra che li hai creati tu, che ne sei titolare né che siano corretti, e **non garantisce alcun effetto legale**. Lo ripeto in molti punti del sito, perché sono le aspettative sbagliate a fare danni.

### Essere chiari su cosa viene raccolto

Per prevenire abusi, applicare i limiti, indagare sui malfunzionamenti e capire l'utilizzo, ogni uso viene registrato con l'indirizzo IP e pochi altri dati. Non li uso per la pubblicità e non li vendo. Indirizzi IP e nomi host restano su questo server per 30 giorni, poi passano a un archivio separato gestito da me per un massimo di 13 mesi; dopo, la parte finale dell'indirizzo viene eliminata e restano solo statistiche. I dettagli sono nei [termini](/it/terms).

## Per chiunque

È gratuito e non serve un account. L'interfaccia è disponibile in 20 lingue. Ci sono anche la timbratura delle foto, un modo per registrare un URL già pubblicato, un'API e un plugin per WordPress. Puoi [scaricare il plugin dalla pagina dell'API](/api#wordpress); la pubblicazione su wordpress.org è in fase di revisione.

Per i passaggi concreti, e per le vie formali disponibili in Italia, leggi [Come dimostrare di averlo fatto prima](/it/column/prove-you-made-it-first).

## Dimmi cosa non funziona

Mi piacerebbe sapere dove DateSealed ti ostacola e cosa vorresti che facesse, soprattutto se sei un fotografo o un blogger e ti è capitata una disputa su "chi è arrivato prima". I contatti sono in fondo alla pagina.
