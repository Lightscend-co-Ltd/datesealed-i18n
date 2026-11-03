title: Ihr Veröffentlichungsdatum ist eine Selbstauskunft: ein unveränderliches Datum für Beiträge im KI-Zeitalter
description: Umschreiben dauert Sekunden, das CMS-Datum beweist nichts. So bekommt jeder Beitrag ein Datum von dritter Seite, automatisch in WordPress – mit seinen Grenzen.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Angenommen, am Morgen nach Ihrer Veröffentlichung taucht eine fast identische Fassung auf: Absätze umgestellt, Formulierungen geändert, das Gerüst dasselbe. Wie würden Sie zeigen, dass Ihre zuerst da war?

## Umschreiben ist billig geworden

Paraphrasieren, umbauen und übersetzen hat früher menschliche Arbeitszeit gekostet. Heute erledigt ein Sprachmodell das in Augenblicken. Die Zahlen zeigen, wie verbreitet maschinell geschriebene und maschinell gelesene Inhalte bereits sind.

| Quelle | Ergebnis |
|---|---|
| Imperva, 2025 Bad Bot Report | 51 % des Webverkehrs 2024 waren automatisiert; bösartige Bots machten 37 % aus, nach 32 % im Vorjahr[^imperva] |
| Cloudflare, Juli 2025 | Die Anfragen von GPTBot in seinem Netz wuchsen von Mai 2024 bis Mai 2025 um 305 %[^cf1] |
| Cloudflare, August 2025 | Rund 80 % des KI-Crawlings im vorangegangenen Jahr dienten dem Training von Modellen[^cf2] |
| NewsGuard | Nachrichtenseiten, die KI-generierte Inhalte mit wenig menschlicher Kontrolle veröffentlichen: 49 im Mai 2023, 3.749 bis Juni 2026[^newsguard] |
| Ahrefs, Mai 2025 | 74,2 % von 900.000 im April 2025 erstmals veröffentlichten Seiten enthielten KI-generierte Anteile[^ahrefs] |
| NeurIPS-2023-Paper | Ein Paraphrasierungsmodell senkte die Genauigkeit eines KI-Text-Detektors von 70,3 % auf 4,6 %[^neurips] |

Das sind Schätzungen von Anbietern und Forschenden mit jeweils eigener Methode, und keine davon ist die Wahrscheinlichkeit, dass gerade *Ihr* Beitrag kopiert wird. Sie zeigen aber, dass Umschreiben leicht und schwer zu erkennen ist.

## Ihr Veröffentlichungsdatum ist eine Selbstauskunft

Das Veröffentlichungsdatum wählen Sie selbst. WordPress erlaubt es, mit einem Datum in der Vergangenheit zu veröffentlichen und das Datum eines bereits veröffentlichten Beitrags zu ändern.[^wp] Das Datum auf der anderen Website ist genauso eine Selbstauskunft – wenn zwei Seiten „Ich war zuerst da“ sagen, ist damit nichts entschieden. Webarchive helfen, aber ob und wann sie Ihre Seite erfassen, haben Sie nicht in der Hand.

Hinzu kommt: Das Urheberrecht entsteht in Deutschland ohne Anmeldung, ein Register mit amtlichem Datum gibt es nicht.[^dpma] Den Zeitpunkt müssen Sie also selbst belegen. Dafür brauchen Sie **jemand anderen als Sie**, der das Datum **bei der Veröffentlichung** festhält, an einem Ort, den **später niemand umschreiben kann**.

## Was DateSealed tut

- Es erhält nur den **SHA-256-Hash** Ihres Beitrags, berechnet in Ihrem Browser (oder mit dem WordPress-Plugin auf Ihrem eigenen Server). Der Text wird nie übertragen.
- Es fügt einen **RFC-3161-Zeitstempel** hinzu, der sofort zurückkommt, und einen **Bitcoin-Eintrag** über OpenTimestamps, der innerhalb weniger Stunden verankert wird.
- In das Bitcoin-Ledger kann niemand nachträglich eine Zeit schreiben. Nach der Verankerung lässt sich das Datum allein mit der Nachweisdatei und dem Ledger prüfen, auch wenn es DateSealed nicht mehr gibt.

Mehr dazu in „[So zeigen Sie, dass Ihr Werk zuerst da war](/de/column/prove-you-made-it-first)“ und „[Warum ich DateSealed gebaut habe](/de/column/why-i-built-datesealed)“.

## Automatisch in WordPress

Eine Gewohnheit, an die man denken muss, übersteht keine volle Woche. Das WordPress-Plugin von DateSealed

- berechnet bei jeder Veröffentlichung und Aktualisierung auf Ihrem Server den Hash des Beitragstextes und sendet nur den Hash;
- **legt bei jeder Aktualisierung einen neuen Eintrag an**, sodass die erste Veröffentlichung nie überschrieben wird und sich eine Versionsgeschichte aufbaut;
- kann auf Wunsch ein Abzeichen mit Link zur Nachweisseite anzeigen;
- setzt WordPress 5.8 oder neuer und PHP 8.2 oder neuer voraus.

[Laden Sie es auf der API-Seite herunter](/api#wordpress), laden Sie die ZIP-Datei in WordPress unter *Plugins* hoch (*Add New → Upload Plugin*), aktivieren Sie es und öffnen Sie *Einstellungen → DateSealed*. Ein Eintrag auf wordpress.org ist in Prüfung.

## Was der Eintrag nicht sagt

- Er zeigt nicht, ob ein Mensch oder ein Modell den Text geschrieben hat.
- Er zeigt nicht, dass der Inhalt richtig oder originell ist, wer ihn geschrieben hat oder wem er gehört.
- Er **garantiert keine Rechtswirkung**. In der EU gilt die gesetzliche Vermutung für Datum, Uhrzeit und Unversehrtheit nur für qualifizierte elektronische Zeitstempel nach der eIDAS-Verordnung.[^eidas] Ein DateSealed-Eintrag ist keiner.

„Es existierte zu diesem Zeitpunkt“ ist ein guter Ausgangspunkt für eine Klärung. Entscheiden wird es sie nicht allein. Nutzen Sie den Eintrag als ein Beweisstück neben den anderen.

## Gewohnheiten, die den Eintrag wertvoll machen

1. **Behalten Sie das Original.** DateSealed speichert nur Hashes.
2. **Behalten Sie die Nachweisdateien.** Legen Sie `.tsr` und `.ots` zum Original, damit Sie ohne DateSealed prüfen können.
3. **Halten Sie beim Veröffentlichen fest.** Die Zeit des Eintrags ist der Moment, in dem Sie ihn erstellen; jeder Tag Verzögerung schwächt ihn.
4. **Überschätzen Sie ihn nicht.** Wo es darauf ankommt, nehmen Sie einen qualifizierten Zeitstempel oder einen notariellen Vermerk hinzu.

[^imperva]: Imperva, „2025 Imperva Bad Bot Report“ (15. April 2025; Daten aus dem Imperva-Netz) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare-Blog (1. Juli 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare-Blog (29. August 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, „AI Tracking Center“ <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, „What Percentage of New Content Is AI-Generated?“ (19. Mai 2025; eigener Detektor von Ahrefs, den das Unternehmen selbst als unvollkommen bezeichnet) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna u. a., „Paraphrasing evades detectors of AI-generated text“, NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, „Write Posts (Classic Editor)“ <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^dpma]: Deutsches Patent- und Markenamt, „Urheberrecht“ <https://www.dpma.de/service/schutzrechte_kurz_erklaert/urheberrecht/index.html>
[^eidas]: Verordnung (EU) Nr. 910/2014 (eIDAS), Art. 41 Abs. 2 <https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910> ; englischer Wortlaut des Artikels: <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
