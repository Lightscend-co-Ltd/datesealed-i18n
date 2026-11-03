title: Come dimostrare di averlo fatto prima: una data di terzi per foto e bozze
description: Ogni data che conservi da solo si può modificare. Come registrare gratis, senza caricare nulla, che una foto o una bozza esistevano in un dato giorno e cosa prova.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Se qualcuno copia il tuo lavoro, riesci a dimostrare che il tuo è venuto prima? Questa guida spiega come prepararti a quel momento, gratis e senza mostrare l'opera a nessuno.

## Ogni data che hai si può modificare

Il problema delle date come prova è semplice: tutto ciò che puoi cambiare tu, la controparte può sostenere che l'hai cambiato.

| La data che hai | Perché è debole |
|---|---|
| Data di pubblicazione del CMS | Puoi impostare una data passata. WordPress spiega come.[^wp] |
| Metadati della foto (Exif) | Strumenti gratuiti come ExifTool li modificano, e possono spostare le date in blocco.[^exif] |
| Date del file | In Windows un file copiato riceve una nuova data di creazione (quella di modifica resta).[^kb] |
| Screenshot | Si ritoccano come qualsiasi immagine. |

Ognuna è meglio di niente, ma nessuna risponde alla domanda «non potresti averlo preparato dopo?». Ti serve una data annotata da **qualcuno che non sia tu**, in una forma che **nessuno possa riscrivere in seguito**.

## Registrare con DateSealed

1. Apri la [pagina iniziale](/it/) e incolla un testo o scegli un file. Puoi anche inserire un URL o uno SHA-256 che hai già.
2. Controlla lo SHA-256 mostrato e premi «Registra ora». L'hash viene calcolato nel browser, quindi il file o il testo non vengono mai inviati.
3. Si apre la pagina della registrazione. Scarica il `.tsr` (marca temporale firmata) e l'`.ots` (prova su Bitcoin) e conservali **insieme al file originale**.

Ogni registrazione riceve due date: una marca temporale RFC 3161 restituita subito e una registrazione OpenTimestamps ancorata in un blocco di Bitcoin entro poche ore. Una volta ancorata, la data si può verificare con il solo registro di Bitcoin, anche se DateSealed chiudesse. La pagina della registrazione riporta i comandi per verificarla sul tuo computer.

Il limite è di 10 registrazioni all'ora e 50 al giorno per indirizzo IP.

## Pubblichi foto? Usa la timbratura

[Timbra foto](/it/stamp) registra l'hash dell'originale e poi, nel tuo browser, crea una copia con un piccolo badge che mostra la data della registrazione e l'indirizzo della sua pagina. La foto non viene caricata.

La registrazione riguarda **l'originale**. La copia timbrata è un altro file e il badge si può ritagliare; da solo non prova nulla. Pubblica la copia timbrata e conserva con cura l'originale.

## Cosa mostra una registrazione, e cosa no

Mostra che **dati corrispondenti a questo hash esistevano al momento registrato**. Tutto qui.

- Non mostra che il contenuto sia corretto o originale.
- Non mostra che l'hai creato tu o che ne sei titolare. La registrazione non dice chi è l'autore.
- **Non garantisce alcun effetto legale.** In Italia, come nel resto dell'UE, la marcatura temporale è disciplinata dagli articoli 41 e 42 del regolamento eIDAS; la qualifica ai prestatori la concede AgID, e la validazione temporale dà luogo a una presunzione legale relativa sulla data e sull'ora.[^agid] Il regolamento attribuisce la presunzione di accuratezza della data e dell'ora e di integrità dei dati alla validazione temporale elettronica qualificata.[^eidas] Una registrazione DateSealed usa lo stesso formato tecnico RFC 3161, ma non è una marca temporale qualificata.

## Per la cosa che vuoi davvero proteggere

In Italia il diritto d'autore nasce con l'opera: per la legge sul diritto d'autore il titolo originario di acquisto è la creazione dell'opera (art. 6 della legge 633/1941).[^l633] Non serve alcuna registrazione per avere i diritti, ma conviene avere una data che altri possano verificare.

| Strumento | Costo | A cosa serve |
|---|---|---|
| Deposito Opere Inedite della SIAE | 72 € per persone fisiche iscritte alla SIAE, 144 € per non iscritte, 288 € per persone giuridiche, bollo da 2 € incluso (pagina SIAE consultata a novembre 2026)[^siae] | Per opere non ancora pubblicate. Dura 5 anni ed è rinnovabile finché l'opera resta inedita |
| Marca temporale qualificata | Secondo il prestatore | Documenti che richiedono un valore legale riconosciuto |
| DateSealed | Gratuito | Dare subito una data al flusso continuo di foto, articoli e bozze |

Secondo la SIAE, il deposito fornisce «una prova certa dell'esistenza dell'opera», non comporta tutela economica né una valutazione sulla proteggibilità, ed è aperto anche a chi non è iscritto; la domanda si spedisce per posta alla sede di Roma.[^siae] DateSealed è un primo livello rapido e gratuito: una prova in più da affiancare alle altre.

## Due cose da ricordare

- **Conserva l'originale.** DateSealed ha solo l'hash. Senza il file originale, la registrazione non si collega a nulla.
- **Registra di nuovo dopo ogni modifica.** Basta cambiare un carattere perché l'hash cambi. Su WordPress, [il plugin](/api#wordpress) registra al posto tuo ogni pubblicazione e ogni aggiornamento.

[^wp]: WordPress.org, «Write Posts (Classic Editor)» <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Articolo KB299648 della Microsoft Knowledge Base (come vengono gestite le date quando si copiano o spostano i file)
[^agid]: AgID, «Le marche temporali verso eIDAS» <https://www.agid.gov.it/en/node/1675>
[^eidas]: Regolamento (UE) n. 910/2014 (eIDAS), articolo 41, paragrafo 2 (EUR-Lex, versione italiana) <https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32014R0910>
[^l633]: Legge 22 aprile 1941, n. 633, art. 6 (Normattiva) <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1941-04-22;633~art6>
[^siae]: SIAE, «Deposito Opere Inedite» <https://www.siae.it/it/cosa-facciamo/altri-servizi/deposito-opere-inedite/>
