title: La data di pubblicazione è un'autodichiarazione: una data che nessuno può riscrivere nell'era dell'IA
description: Riscrivere un articolo richiede pochi istanti e la data del CMS non prova nulla. Come avere una data di terzi per ogni post, anche su WordPress, e i limiti.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Immagina che, la mattina dopo la pubblicazione, compaia una quasi copia: paragrafi in un altro ordine, frasi riformulate, lo stesso scheletro. Come dimostreresti che il tuo è venuto prima?

## Riscrivere costa poco

Parafrasare, ristrutturare e tradurre richiedevano tempo umano. Oggi un modello linguistico lo fa in un attimo. I numeri mostrano quanto siano già diffusi i contenuti scritti e letti dalle macchine.

| Fonte | Dato |
|---|---|
| Imperva, 2025 Bad Bot Report | Il 51% del traffico web nel 2024 era automatizzato; i bot malevoli erano il 37%, contro il 32%[^imperva] |
| Cloudflare, luglio 2025 | Le richieste di GPTBot sulla sua rete sono cresciute del 305% da maggio 2024 a maggio 2025[^cf1] |
| Cloudflare, agosto 2025 | Circa l'80% della scansione da parte dell'IA nell'anno precedente serviva ad addestrare modelli[^cf2] |
| NewsGuard | Siti di notizie che pubblicano contenuti generati dall'IA con poca supervisione umana: 49 a maggio 2023, 3.749 a giugno 2026[^newsguard] |
| Ahrefs, maggio 2025 | Il 74,2% di 900.000 pagine pubblicate per la prima volta ad aprile 2025 conteneva contenuti generati dall'IA[^ahrefs] |
| Articolo NeurIPS 2023 | Un modello di parafrasi ha ridotto l'accuratezza di un rilevatore di testi IA dal 70,3% al 4,6%[^neurips] |

Sono stime di aziende o ricercatori, ognuna con il suo metodo, e nessuna indica la probabilità che venga copiato il *tuo* post. Mostrano però che riscrivere è facile e difficile da individuare.

## La data di pubblicazione è un'autodichiarazione

La data di pubblicazione la scegli tu. WordPress permette di pubblicare con una data passata e di cambiare la data di un post già online.[^wp] Anche la data dell'altro sito è autodichiarata, quindi due persone che dicono «sono arrivato prima io» non risolvono nulla. Gli archivi del web aiutano, ma non decidi tu se e quando salvano la tua pagina.

Ti serve che **qualcuno che non sia tu** annoti la data **nel momento in cui pubblichi**, in un posto che **nessuno possa riscrivere dopo**.

## Cosa fa DateSealed

- Riceve solo l'**hash SHA-256** del post, calcolato nel tuo browser (o sul tuo server, con il plugin per WordPress). Il testo non viene mai inviato.
- Gli associa una **marca temporale RFC 3161**, restituita subito, e una **registrazione su Bitcoin** tramite OpenTimestamps, ancorata entro poche ore.
- Nessuno può scrivere un orario nel registro di Bitcoin a posteriori. Una volta ancorata, la data si verifica con il solo file di prova e il registro, anche se DateSealed sparisse.

Più dettagli in «[Come dimostrare di averlo fatto prima](/it/column/prove-you-made-it-first)» e «[Perché ho creato DateSealed](/it/column/why-i-built-datesealed)».

## Automatico su WordPress

Un'abitudine che devi ricordarti non sopravvive a una settimana piena. Il plugin DateSealed per WordPress:

- calcola sul tuo server l'hash del testo a ogni pubblicazione e aggiornamento, e invia solo l'hash;
- **aggiunge una nuova registrazione** a ogni aggiornamento, così la prima pubblicazione non viene mai sovrascritta e lo storico delle revisioni si accumula;
- può mostrare un badge con il link alla pagina della registrazione (facoltativo);
- richiede WordPress 5.8 o successivo e PHP 8.2 o successivo.

[Scaricalo dalla pagina dell'API](/api#wordpress), poi in WordPress vai su *Plugins → Add New → Upload Plugin*, attivalo e apri *Settings → DateSealed* (in un WordPress in italiano questi menu compaiono tradotti). La pubblicazione su wordpress.org è in fase di revisione.

## Cosa la registrazione non dice

- Non mostra se il testo l'ha scritto una persona o un modello.
- Non mostra che il contenuto sia corretto o originale, chi l'ha scritto né chi ne è titolare.
- **Non garantisce alcun effetto legale.** In Italia e nell'UE la presunzione legale spetta alla validazione temporale elettronica qualificata del regolamento eIDAS, rilasciata da prestatori qualificati da AgID.[^agid][^eidas] DateSealed non lo è.

«Esisteva in questo momento» è un buon punto di partenza per una discussione, ma da solo non la chiude. Usa la registrazione come una prova accanto alle altre.

## Abitudini che danno valore alla registrazione

1. **Conserva l'originale.** DateSealed tiene solo gli hash.
2. **Conserva i file di prova.** Tieni `.tsr` e `.ots` insieme all'originale, così puoi verificare senza DateSealed.
3. **Registra al momento della pubblicazione.** L'ora della registrazione è quella in cui l'hai fatta; ogni giorno di ritardo la indebolisce.
4. **Non sopravvalutarla.** Per un post importante, aggiungi una marca temporale qualificata; per un'opera non ancora pubblicata, anche il Deposito Opere Inedite della SIAE.

[^imperva]: Imperva, «2025 Imperva Bad Bot Report» (15 aprile 2025; dati della rete Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog di Cloudflare (1° luglio 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog di Cloudflare (29 agosto 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, «AI Tracking Center» <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, «What Percentage of New Content Is AI-Generated?» (19 maggio 2025; con il rilevatore dell'azienda, che essa stessa definisce imperfetto) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., «Paraphrasing evades detectors of AI-generated text», NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, «Write Posts (Classic Editor)» <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^agid]: AgID, «Le marche temporali verso eIDAS» <https://www.agid.gov.it/en/node/1675>
[^eidas]: Regolamento (UE) n. 910/2014 (eIDAS), articolo 41, paragrafo 2 (EUR-Lex, versione italiana) <https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32014R0910>
