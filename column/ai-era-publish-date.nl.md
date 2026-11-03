title: Je publicatiedatum is een eigen verklaring: een datum die niemand kan herschrijven in het AI-tijdperk
description: Herschrijven kost nu seconden en je CMS-datum bewijst niets. Zo geef je elk bericht een datum van een derde, automatisch in WordPress, en dit zijn de grenzen.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Stel: de ochtend nadat je iets publiceert, verschijnt er een bijna-kopie. Alinea's omgegooid, zinnen anders geformuleerd, het skelet hetzelfde. Hoe laat je zien dat het jouwe er eerst was?

## Herschrijven is goedkoop geworden

Parafraseren, herstructureren en vertalen kostte vroeger mensenwerk. Nu doet een taalmodel het in een oogwenk. De cijfers laten zien hoe gewoon door machines geschreven en gelezen inhoud al is.

| Bron | Bevinding |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% van het webverkeer in 2024 was geautomatiseerd; kwaadaardige bots waren goed voor 37%, tegen 32% een jaar eerder[^imperva] |
| Cloudflare, juli 2025 | Het aantal verzoeken van GPTBot op zijn netwerk groeide van mei 2024 tot mei 2025 met 305%[^cf1] |
| Cloudflare, augustus 2025 | Ongeveer 80% van het AI-crawlen in het jaar daarvoor diende voor het trainen van modellen[^cf2] |
| NewsGuard | Nieuwssites die AI-gegenereerde inhoud publiceren met weinig menselijk toezicht: 49 in mei 2023, 3.749 in juni 2026[^newsguard] |
| Ahrefs, mei 2025 | 74,2% van 900.000 pagina's die in april 2025 voor het eerst verschenen, bevatte AI-gegenereerde inhoud[^ahrefs] |
| NeurIPS 2023-paper | Een parafraseermodel liet de nauwkeurigheid van een AI-tekstdetector dalen van 70,3% naar 4,6%[^neurips] |

Dit zijn schattingen van bedrijven en onderzoekers, elk met een eigen methode, en geen ervan is de kans dat juist *jouw* bericht wordt gekopieerd. Ze laten wel zien dat herschrijven makkelijk is en moeilijk te herkennen.

## Je publicatiedatum is een eigen verklaring

Je publicatiedatum kies je zelf. WordPress laat je publiceren met een datum in het verleden en de datum van een gepubliceerd bericht wijzigen.[^wp] De datum op de andere site is net zo goed een eigen verklaring; als twee mensen zeggen "ik was eerst", is daarmee niets beslist. Webarchieven helpen, maar of en wanneer ze je pagina vastleggen, bepaal jij niet.

In Nederland ontstaat het auteursrecht bovendien automatisch, zonder registratie.[^op] Er is dus geen officiële datum: je moet zelf kunnen aantonen wanneer je tekst bestond. Daarvoor heb je **iemand anders dan jijzelf** nodig die de datum **op het moment van publiceren** vastlegt, op een plek die **later door niemand te herschrijven is**.

## Wat DateSealed doet

- Het ontvangt alleen de **SHA-256-hash** van je bericht, berekend in je browser (of met de WordPress-plugin op je eigen server). De tekst wordt nooit verstuurd.
- Het voegt een **RFC 3161-tijdstempel** toe die direct terugkomt, en een **Bitcoin-vastlegging** via OpenTimestamps die binnen een paar uur wordt verankerd.
- Niemand kan achteraf een tijd in het Bitcoin-grootboek schrijven. Na verankering is de datum te controleren met alleen het bewijsbestand en het grootboek, ook als DateSealed verdwijnt.

Meer hierover in "[Zo laat je zien dat jij het eerst had](/nl/column/prove-you-made-it-first)" en "[Waarom ik DateSealed heb gebouwd](/nl/column/why-i-built-datesealed)".

## Automatisch in WordPress

Een gewoonte waar je aan moet denken, overleeft geen drukke week. De WordPress-plugin van DateSealed:

- berekent bij elke publicatie en update op je server de hash van de berichttekst en verstuurt alleen die hash;
- **voegt bij elke update een nieuwe vastlegging toe**, zodat de eerste publicatie nooit wordt overschreven en de versiegeschiedenis zich opbouwt;
- kan een label tonen dat naar de vastleggingspagina linkt (optioneel);
- vereist WordPress 5.8 of hoger en PHP 8.2 of hoger.

[Download hem op de API-pagina](/api#wordpress), ga in WordPress naar *Plugins → Nieuwe plugin → Plugin uploaden* (*Plugins → Add New → Upload Plugin*), upload het zip-bestand, activeer de plugin en open *Instellingen → DateSealed* (*Settings → DateSealed*). De vermelding op wordpress.org is nog in behandeling.

## Wat de vastlegging niet zegt

- Ze zegt niet of een mens of een model de tekst heeft geschreven.
- Ze zegt niet dat de inhoud juist of origineel is, wie hem heeft geschreven of van wie hij is.
- Ze **garandeert geen rechtsgevolg**. In de EU geldt het wettelijke vermoeden van juiste datum en tijd alleen voor gekwalificeerde elektronische tijdstempels volgens de eIDAS-verordening.[^eidas] Een vastlegging van DateSealed is dat niet.

"Het bestond op dit moment" is een goed beginpunt voor een gesprek. Op zichzelf beslecht het niets. Gebruik de vastlegging als één bewijsstuk naast de rest.

## Gewoonten die de vastlegging waardevol maken

1. **Bewaar het origineel.** DateSealed bewaart alleen hashes.
2. **Bewaar de bewijsbestanden.** Zet de `.tsr` en de `.ots` bij het origineel, zodat je zonder DateSealed kunt controleren.
3. **Leg vast bij het publiceren.** Het tijdstip van de vastlegging is het moment waarop je die maakt; elke dag uitstel maakt de vastlegging zwakker.
4. **Overschat de vastlegging niet.** Gaat het ergens echt om, voeg dan een i-DEPOT[^op] of een gekwalificeerde tijdstempel toe.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (15 april 2025; gegevens uit het Imperva-netwerk) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare-blog (1 juli 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare-blog (29 augustus 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (19 mei 2025; eigen detector van Ahrefs, die volgens Ahrefs niet foutloos is) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna e.a., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^op]: Ondernemersplein (overheidsinformatie voor ondernemers, tekst van het BOIP), "Uw idee vastleggen" <https://ondernemersplein.overheid.nl/uw-idee-vastleggen/>
[^eidas]: Verordening (EU) nr. 910/2014 (eIDAS), artikel 41, lid 2 <https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32014R0910> ; Engelse tekst van het artikel: <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
