title: So zeigen Sie, dass Ihr Werk zuerst da war: ein Datum von dritter Seite für Fotos und Entwürfe
description: Jedes eigene Datum lässt sich ändern. So halten Sie kostenlos und ohne Upload fest, dass ein Foto oder Entwurf existierte – und was das beweist und was nicht.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Wenn jemand Ihr Werk kopiert: Können Sie zeigen, dass Ihres zuerst da war? Diese Anleitung erklärt, wie Sie sich auf diesen Moment vorbereiten – kostenlos und ohne Ihr Werk jemandem zu zeigen.

## In Deutschland entsteht das Urheberrecht ohne Anmeldung

Das Urheberrecht entsteht in Deutschland mit der Schöpfung des Werks. Eine Eintragung in ein Register gibt es nicht, und es fallen keine Gebühren an.[^dpma] Auch in der Schweiz entsteht der Schutz automatisch, ein Register gibt es dort ebenfalls nicht.[^ige]

Das ist bequem, hat aber eine Kehrseite: Im Streitfall gibt es kein amtliches Datum, auf das Sie verweisen können. Das Gesetz vermutet zwar, dass derjenige Urheber ist, der auf den Exemplaren eines erschienenen Werks in üblicher Weise als solcher bezeichnet ist (§ 10 UrhG).[^urhg10] Wann Ihr Werk entstanden ist, müssen Sie aber mit eigenen Mitteln belegen.

## Jedes Datum, das Sie selbst haben, lässt sich ändern

Das Problem mit Datumsbelegen ist einfach: Was Sie selbst ändern können, kann die Gegenseite Ihnen als geändert vorhalten.

| Ihr Datum | Warum es schwach ist |
|---|---|
| Veröffentlichungsdatum im CMS | Es lässt sich in die Vergangenheit setzen. WordPress beschreibt, wie.[^wp] |
| Foto-Metadaten (Exif) | Kostenlose Werkzeuge wie ExifTool ändern sie, auch für viele Dateien auf einmal.[^exif] |
| Dateidatum | Unter Windows erhält eine kopierte Datei ein neues Erstellungsdatum (das Änderungsdatum bleibt).[^kb] |
| Screenshots | Sie lassen sich bearbeiten wie jedes Bild. |

Besser als nichts ist jedes davon. Aber keines beantwortet die Frage „Hätten Sie das nicht nachträglich erstellen können?“. Dafür brauchen Sie ein Datum, das **jemand anderes als Sie** festhält, und zwar so, dass **es später niemand umschreiben kann**.

## Festhalten mit DateSealed

1. Öffnen Sie die [Startseite](/de/) und fügen Sie Text ein oder wählen Sie eine Datei. Sie können auch eine URL oder einen vorhandenen SHA-256-Wert eingeben.
2. Prüfen Sie den angezeigten SHA-256 und klicken Sie auf die Schaltfläche, um ihn festzuhalten. Der Hash wird in Ihrem Browser berechnet; Datei oder Text werden nicht übertragen.
3. Die Nachweisseite öffnet sich. Laden Sie die `.tsr` (signierter Zeitstempel) und die `.ots` (Bitcoin-Nachweis) herunter und bewahren Sie beide **zusammen mit der Originaldatei** auf.

Jeder Eintrag erhält zwei Datumsangaben: einen RFC-3161-Zeitstempel, der sofort zurückkommt, und einen OpenTimestamps-Eintrag, der innerhalb weniger Stunden in einem Bitcoin-Block verankert wird. Danach lässt sich das Datum allein am Bitcoin-Ledger prüfen, auch wenn DateSealed eingestellt wird. Die Nachweisseite nennt die Befehle, mit denen Sie das auf Ihrem eigenen Rechner tun.

Das Limit liegt bei 10 Einträgen pro Stunde und 50 pro Tag je IP-Adresse.

## Fotos veröffentlichen? Nutzen Sie den Stempel

[Fotos stempeln](/de/stamp) hält den Hash Ihres Originals fest und erzeugt dann in Ihrem Browser eine Kopie mit einem kleinen Badge, der das Datum und die Adresse der Nachweisseite zeigt. Das Foto selbst wird nicht hochgeladen.

Der Eintrag bezieht sich auf **das Original**. Die gestempelte Kopie ist eine andere Datei, und der Badge lässt sich wegschneiden; für sich allein beweist er nichts. Veröffentlichen Sie die gestempelte Kopie und bewahren Sie das Original sicher auf.

## Was ein Eintrag zeigt – und was nicht

Er zeigt, dass **Daten mit diesem Hash zum festgehaltenen Zeitpunkt existierten**. Das ist alles.

- Er zeigt nicht, dass der Inhalt richtig oder originell ist.
- Er zeigt nicht, dass Sie das Werk geschaffen haben oder dass es Ihnen gehört. Wer es geschaffen hat, steht nicht im Eintrag.
- Er **garantiert keine Rechtswirkung**. Nach der eIDAS-Verordnung gilt für einen qualifizierten elektronischen Zeitstempel die Vermutung, dass Datum und Uhrzeit richtig sind und die verknüpften Daten unverändert.[^eidas] Qualifizierte Anbieter in Deutschland beaufsichtigt die Bundesnetzagentur.[^vdg] Ein DateSealed-Eintrag ist kein qualifizierter Zeitstempel.

## Für das eine Werk, das Sie wirklich schützen müssen

Nutzen Sie zusätzlich förmliche Wege:

| Weg | Wofür er sich eignet |
|---|---|
| Notarin oder Notar | Bescheinigt, wann ihr oder ihm eine private Urkunde vorgelegt wurde (§ 43 BeurkG).[^beurkg] |
| Qualifizierter elektronischer Zeitstempel | Wenn Sie die gesetzliche Vermutung nach eIDAS brauchen |
| DateSealed | Kostenlos: zuerst einmal ein Datum für den laufenden Strom an Fotos, Artikeln und Entwürfen |

DateSealed ist die günstige, schnelle erste Schicht – ein weiteres Beweisstück, das Sie neben die anderen legen.

## Zwei Dinge, die Sie sich merken sollten

- **Behalten Sie das Original.** DateSealed speichert nur den Hash. Ohne die Originaldatei lässt sich der Eintrag mit nichts verbinden.
- **Halten Sie nach jeder Änderung erneut fest.** Ändert sich ein Zeichen, ändert sich der Hash. Unter WordPress übernimmt [das Plugin](/api#wordpress) das bei jeder Veröffentlichung und Aktualisierung.

[^dpma]: Deutsches Patent- und Markenamt, „Urheberrecht“ <https://www.dpma.de/service/schutzrechte_kurz_erklaert/urheberrecht/index.html>
[^ige]: Eidgenössisches Institut für Geistiges Eigentum, „Urheberrecht“ <https://www.ige.ch/de/etwas-schuetzen/urheberrecht>
[^urhg10]: § 10 Urheberrechtsgesetz <https://www.gesetze-im-internet.de/urhg/__10.html>
[^wp]: WordPress.org, „Write Posts (Classic Editor)“ <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Microsoft Knowledge Base, Artikel KB299648 (wie Datumsangaben beim Kopieren und Verschieben von Dateien behandelt werden)
[^eidas]: Verordnung (EU) Nr. 910/2014 (eIDAS), Art. 41 Abs. 2 <https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910> ; englischer Wortlaut des Artikels: <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
[^vdg]: § 2 Vertrauensdienstegesetz <https://www.gesetze-im-internet.de/vdg/__2.html>
[^beurkg]: § 43 Beurkundungsgesetz <https://www.gesetze-im-internet.de/beurkg/__43.html>
