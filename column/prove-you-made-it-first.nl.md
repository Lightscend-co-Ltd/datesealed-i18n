title: Zo laat je zien dat jij het eerst had: een datum van een derde voor je foto's en concepten
description: Elke eigen datum is aan te passen. Zo leg je gratis en zonder upload vast dat een foto of concept bestond, wat dat bewijst en wat het i-DEPOT toevoegt.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Als iemand je werk kopieert, kun je dan laten zien dat het jouwe er eerder was? Deze handleiding legt uit hoe je je op dat moment voorbereidt, gratis en zonder je werk aan iemand te laten zien.

## Auteursrecht ontstaat vanzelf, het bewijs niet

In Nederland ontstaat het auteursrecht automatisch zodra je een origineel werk maakt; registreren is niet nodig.[^op] Dat is handig, maar er is dus ook geen register met een officiële datum. Aantonen dat jij de maker bent en dat jouw werk er op een bepaalde dag al was, kan in een geschil lastig zijn.

## Elke datum die je zelf hebt, is aan te passen

Het probleem met datumbewijs is eenvoudig: wat je zelf kunt veranderen, daarvan kan de tegenpartij zeggen dat je het hebt veranderd.

| De datum die je hebt | Waarom die zwak is |
|---|---|
| Publicatiedatum in je CMS | Je kunt een datum in het verleden instellen. WordPress legt uit hoe.[^wp] |
| Fotometadata (Exif) | Gratis programma's als ExifTool passen ze aan, ook voor veel bestanden tegelijk.[^exif] |
| Bestandsdatums | In Windows krijgt een gekopieerd bestand een nieuwe aanmaakdatum (de wijzigingsdatum blijft).[^kb] |
| Schermafbeeldingen | Die zijn te bewerken zoals elk ander beeld. |

Elk daarvan is beter dan niets, maar geen ervan beantwoordt de vraag "had je dit niet achteraf kunnen maken?". Daarvoor heb je een datum nodig die **iemand anders dan jijzelf** vastlegt, in een vorm die **later door niemand te herschrijven is**.

## Vastleggen met DateSealed

1. Open de [startpagina](/nl/) en plak een tekst of kies een bestand. Je kunt ook een URL invoeren, of een SHA-256 die je al hebt.
2. Controleer de getoonde SHA-256 en klik op de knop om hem vast te leggen. De hash wordt in je browser berekend; het bestand of de tekst zelf wordt nooit verstuurd.
3. De vastleggingspagina opent. Download de `.tsr` (ondertekende tijdstempel) en de `.ots` (Bitcoin-bewijs) en bewaar ze **samen met het originele bestand**.

Elke vastlegging krijgt twee datums: een RFC 3161-tijdstempel die direct terugkomt, en een OpenTimestamps-vastlegging die binnen een paar uur in een Bitcoin-blok wordt verankerd. Daarna is de datum te controleren met alleen het Bitcoin-grootboek, ook als DateSealed ophoudt te bestaan. De vastleggingspagina vermeldt de opdrachten om dat op je eigen computer te doen.

De limiet is 10 vastleggingen per uur en 50 per dag per IP-adres.

## Foto's publiceren? Gebruik de stempel

[Foto stempelen](/nl/stamp) legt de hash van je origineel vast en maakt daarna in je browser een kopie met een klein label met de datum van de vastlegging en het adres van de vastleggingspagina. De foto zelf wordt niet geüpload.

De vastlegging hoort bij **het origineel**. De gestempelde kopie is een ander bestand, en het label kun je wegsnijden; op zichzelf bewijst het niets. Publiceer de gestempelde kopie en bewaar het origineel goed.

## Wat een vastlegging laat zien, en wat niet

Ze laat zien dat **gegevens met deze hash op het vastgelegde tijdstip bestonden**. Dat is alles.

- Ze laat niet zien dat de inhoud juist of origineel is.
- Ze laat niet zien dat jij het hebt gemaakt of dat het van jou is. Wie het werk heeft gemaakt, staat niet in de vastlegging.
- Ze **garandeert geen rechtsgevolg**. Volgens de Europese eIDAS-verordening geldt voor een **gekwalificeerde** elektronische tijdstempel het vermoeden dat datum en tijd juist zijn en dat de gekoppelde gegevens niet zijn gewijzigd.[^eidas] Een vastlegging van DateSealed is geen gekwalificeerde tijdstempel.

## Voor dat ene werk dat je echt moet beschermen

Gebruik daarnaast formele middelen:

| Middel | Wat het oplevert |
|---|---|
| i-DEPOT van het Benelux-Bureau voor de Intellectuele Eigendom (BOIP) | Bewijs dat je idee op een bepaalde datum bestond; het geeft zelf geen intellectueel eigendomsrecht. Digitaal € 37 voor 5 jaar of € 53 voor 10 jaar, verlengen met 5 jaar € 26 (geraadpleegd op 3 november 2026).[^op] |
| Gekwalificeerde elektronische tijdstempel | Het wettelijke vermoeden uit eIDAS, als je dat nodig hebt |
| DateSealed | Gratis: eerst een datum voor de doorlopende stroom foto's, artikelen en concepten |

Het i-DEPOT is een Benelux-dienst, dus ook bruikbaar voor makers in België.

DateSealed is de goedkope, snelle eerste laag: nog een bewijsstuk om naast de rest te leggen.

## Twee dingen om te onthouden

- **Bewaar het origineel.** DateSealed bewaart alleen de hash. Zonder het originele bestand is de vastlegging nergens aan te koppelen.
- **Leg na elke wijziging opnieuw vast.** Verander één teken en de hash verandert. In WordPress doet [de plugin](/api#wordpress) dat voor je bij elke publicatie en update.

[^op]: Ondernemersplein (overheidsinformatie voor ondernemers, tekst van het BOIP), "Uw idee vastleggen" <https://ondernemersplein.overheid.nl/uw-idee-vastleggen/>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Microsoft Knowledge Base, artikel KB299648 (hoe datums worden behandeld bij het kopiëren of verplaatsen van bestanden)
[^eidas]: Verordening (EU) nr. 910/2014 (eIDAS), artikel 41, lid 2 <https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32014R0910> ; Engelse tekst van het artikel: <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
