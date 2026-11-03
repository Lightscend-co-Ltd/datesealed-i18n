title: Waarom ik DateSealed heb gebouwd: een notitie van de ontwikkelaar
description: Het begon met vastgoedfoto's. Wat ik bij bestaande opties vond, en de regels voor een gratis bewijs dat zelfs ik niet kan herschrijven.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed is een gratis hulpmiddel dat vastlegt wanneer een tekst, een foto of een webpagina bestond. Ik ben Yuki Nakazawa en ik heb het gebouwd. Deze notitie gaat over het waarom, en over de keuzes die ik onderweg heb gemaakt.

## Het begon met vastgoedfoto's

Ik heb een vastgoedbedrijf in Japan. We fotograferen onze panden en publiceren die foto's. Ik wilde voorbereid zijn op de dag dat iemand een van die foto's zou bewerken of op een andere site zou zetten, zodat ik kon laten zien dat het origineel van ons was en er eerder was.

Ik had de originele bestanden, en mijn berichten hadden een publicatiedatum. Maar dat kon ik allemaal zelf aanpassen, en wie een kopie heeft, kan dezelfde datums claimen. Wat ik nodig had, was een datum die **iemand anders dan ikzelf** vastlegt, in een vorm die **achteraf door niemand te veranderen is**.

## Wat ik eerst vond

Ik heb gekeken wat er in Japan beschikbaar was, stand november 2026:

- **Een vaste datum van een notaris.** 700 yen per document. Er is een elektronische variant, maar die accepteert alleen tekst-, pdf- en xml-bestanden tot 10 MB, en werkt alleen op werkdagen.
- **Registratie bij het Japanse Agentschap voor Culturele Zaken.** 3.000 yen per werk, op papier, één werk tegelijk. Het levert een vermoeden op dat het werk op de geregistreerde datum is gepubliceerd.
- **Tijdstempels van aanbieders die het Japanse ministerie van Binnenlandse Zaken en Communicatie heeft erkend.** Die hebben in Japan een officiële status. De prijzen zijn vooral op bedrijven gericht.
- **Bewijsdiensten op basis van blockchain.** Die ik vond, waren voor bedrijven bedoeld of betaald.
- **Handtekeningen in de camera (C2PA).** Sommige camera's ondertekenen foto's bij het maken. Dat zegt iets over waar een bestand vandaan komt, en dat is een andere vraag dan wanneer het bestond.

Dat is allemaal nuttig, en voor dat ene werk dat je echt moet beschermen, kun je het het beste ook gebruiken. Maar voor elke nieuwe foto of elk artikel betalen en een aanvraag indienen is niet realistisch. Ik wilde iets dat **gratis is, zonder account werkt, niets uploadt, wordt bewaard op een plek die zelfs de beheerder niet kan herschrijven, en in WordPress bij elke publicatie vanzelf gebeurt**. Ik vond het niet, dus heb ik het gebouwd.

## De regels die ik mezelf stelde

### Niets aannemen behalve een hash

DateSealed ontvangt alleen de SHA-256-hash van je bestand of tekst, een vingerafdruk van 64 tekens. De hash wordt in je browser berekend, dus je foto's en concepten verlaten je computer niet. Juist ongepubliceerd werk wil je vastleggen; als je het daarvoor uit handen moet geven, schiet het zijn doel voorbij.

### Je zou mij niet hoeven te vertrouwen

Elke vastlegging krijgt twee datums. De eerste is een RFC 3161-tijdstempel, ondertekend door de eigen tijdstempeldienst van DateSealed en direct teruggegeven. De tweede wordt via OpenTimestamps verankerd in een Bitcoin-blok, meestal binnen een paar uur.

De eerste is zo betrouwbaar als ik ben. De tweede kan ik niet veranderen. Is hij eenmaal verankerd, dan kun je de datum controleren met alleen het bewijsbestand (`.ots`) en het Bitcoin-grootboek, ook als DateSealed verdwijnt. Elke vastleggingspagina vermeldt de opdrachten om dat op je eigen computer te controleren.

De hoofdsleutel van de tijdstempeldienst is op mijn eigen computer aangemaakt en wordt versleuteld met een wachtwoordzin bewaard. De server heeft alleen de ondertekeningssleutel.

### Nooit wissen, nooit herschrijven

Zelfs het beheerscherm heeft geen mogelijkheid om een vastlegging te verwijderen of de hash of tijd te wijzigen. Een register is alleen iets waard als de beheerder er niet aan kan komen. Als je een bericht bijwerkt, blijft de oude vastlegging staan en komt er een nieuwe bij. De WordPress-plugin volgt dezelfde regel.

### Vooraf zeggen wat het niet kan

Een vastlegging laat zien dat gegevens met deze hash op dat moment bestonden. Meer niet. Ze laat niet zien dat jij het hebt gemaakt, dat het van jou is of dat het klopt, en ze **garandeert geen rechtsgevolg**. Dat zeg ik op veel plaatsen op de site, omdat verkeerde verwachtingen de meeste schade doen.

### Duidelijk zijn over wat wordt vastgelegd

Om misbruik te voorkomen, limieten te handhaven, fouten op te sporen en het gebruik te begrijpen, wordt elk gebruik gelogd met het IP-adres en een paar andere gegevens. Die worden niet voor reclame gebruikt en niet verkocht. IP-adressen en hostnamen blijven 30 dagen op deze server en gaan daarna naar aparte opslag die ik beheer, voor maximaal 13 maanden; daarna wordt het einde van het adres verwijderd en blijven alleen statistieken over. De details staan in de [gebruiksvoorwaarden](/nl/terms).

## Voor iedereen

Het is gratis en je hebt geen account nodig. De interface is beschikbaar in 20 talen. Er is ook een stempel voor foto's, een manier om een gepubliceerde URL vast te leggen, een API en een WordPress-plugin. Je kunt [de plugin downloaden op de API-pagina](/api#wordpress); een vermelding op wordpress.org wordt beoordeeld.

Hoe je stap voor stap een datum aan foto's en concepten geeft, en wat er in Nederland en België voor bestaat, lees je in "[Zo laat je zien dat jij het eerst had](/nl/column/prove-you-made-it-first)".

## Laat me weten wat er misgaat

Ik hoor graag waar DateSealed je in de weg zit en wat het als volgende zou moeten kunnen, vooral van fotografen en bloggers die al eens in een discussie over "wie was eerst" verwikkeld zijn geraakt. De contactgegevens staan onderaan de pagina.
