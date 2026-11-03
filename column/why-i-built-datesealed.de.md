title: Warum ich DateSealed gebaut habe – eine Notiz des Entwicklers
description: Am Anfang standen Immobilienfotos. Was ich an Angeboten vorfand und nach welchen Regeln ich einen kostenlosen Nachweis baute, den selbst ich nicht ändern kann.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed ist ein kostenloses Werkzeug, das festhält, wann ein Text, ein Foto oder eine Webseite existiert hat. Ich bin Yuki Nakazawa und habe es entwickelt. In dieser Notiz geht es darum, warum – und um die Entscheidungen, die ich dabei getroffen habe.

## Am Anfang standen Immobilienfotos

Ich führe in Japan ein Immobilienunternehmen. Wir fotografieren unsere Objekte und veröffentlichen die Bilder. Ich wollte für den Tag vorbereitet sein, an dem jemand eines dieser Fotos verändert oder auf einer anderen Website zeigt – und dann belegen können, dass das Original von uns stammt und zuerst da war.

Die Originaldateien hatte ich, und meine Beiträge hatten ein Veröffentlichungsdatum. Aber all das konnte ich selbst ändern, und wer eine Kopie besitzt, kann dieselben Daten für sich beanspruchen. Was ich brauchte, war ein Datum, das **jemand anderes als ich** festhält, und zwar so, dass **niemand es nachträglich ändern kann**.

## Was ich zuerst gefunden habe

Ich habe mir angesehen, was es in Japan Stand November 2026 gab:

- **Das amtliche Datum eines Notars.** 700 Yen pro Dokument. Es gibt eine elektronische Variante, die aber nur Text-, PDF- und XML-Dateien bis 10 MB annimmt und nur werktags bearbeitet wird.
- **Die Registrierung bei der japanischen Kulturbehörde.** 3.000 Yen pro Werk, auf Papier, ein Werk nach dem anderen. Sie begründet die Vermutung, dass das Werk am eingetragenen Tag veröffentlicht wurde.
- **Zeitstempel von Anbietern, die das japanische Ministerium für Inneres und Kommunikation akkreditiert hat.** Sie haben in Japan einen offiziellen Status. Die Preise richten sich überwiegend an Unternehmen.
- **Blockchain-basierte Nachweisdienste.** Die ich fand, waren für Firmen gedacht oder kostenpflichtig.
- **Signaturen in der Kamera (C2PA).** Manche Kameras signieren Fotos bei der Aufnahme. Das sagt etwas darüber, woher eine Datei stammt – eine andere Frage als die, wann sie existierte.

All das ist nützlich, und für das eine Werk, das man wirklich schützen muss, sollte man es auch nutzen. Aber für jedes neue Foto und jeden Artikel zu zahlen und Anträge zu stellen, ist nicht realistisch. Ich wollte etwas, das **kostenlos ist, keine Anmeldung braucht, nichts hochlädt, an einem Ort gespeichert wird, den nicht einmal der Betreiber umschreiben kann, und bei WordPress bei jeder Veröffentlichung automatisch läuft**. Ich habe es nicht gefunden, also habe ich es gebaut.

## Die Regeln, die ich mir gesetzt habe

### Nichts annehmen außer einem Hash

DateSealed erhält nur den SHA-256-Hash Ihrer Datei oder Ihres Textes, einen Fingerabdruck aus 64 Zeichen. Der Hash wird in Ihrem Browser berechnet; Fotos und Entwürfe verlassen Ihren Rechner nicht. Gerade Unveröffentlichtes will man festhalten – müsste man es dafür aus der Hand geben, wäre der Zweck verfehlt.

### Sie sollen mir nicht vertrauen müssen

Jeder Eintrag erhält zwei Daten. Das eine ist ein RFC-3161-Zeitstempel, signiert von DateSealeds eigener Zeitstempelstelle und sofort zurückgegeben. Das andere wird über OpenTimestamps in einem Bitcoin-Block verankert, meist innerhalb weniger Stunden.

Das erste ist nur so vertrauenswürdig wie ich. Das zweite kann ich nicht ändern. Ist es einmal verankert, lässt sich das Datum allein mit der Nachweisdatei (`.ots`) und dem Bitcoin-Ledger prüfen, auch wenn es DateSealed nicht mehr gibt. Jede Nachweisseite nennt die Befehle, mit denen Sie das auf Ihrem eigenen Rechner prüfen können.

Der Wurzelschlüssel der Zeitstempelstelle wurde auf meinem eigenen Computer erzeugt und wird mit einer Passphrase verschlüsselt aufbewahrt. Auf dem Server liegt nur der Signaturschlüssel.

### Nie löschen, nie umschreiben

Selbst die Verwaltungsoberfläche hat keine Funktion, um einen Eintrag zu löschen oder Hash und Zeit zu ändern. Ein Register ist nur etwas wert, wenn sein Betreiber es nicht anfassen kann. Wenn Sie einen Beitrag aktualisieren, bleibt der alte Eintrag bestehen und ein neuer kommt hinzu. Das WordPress-Plugin folgt derselben Regel.

### Von vornherein sagen, was es nicht kann

Ein Eintrag zeigt, dass Daten mit diesem Hash zu diesem Zeitpunkt existierten. Mehr nicht. Er zeigt nicht, dass Sie das Werk geschaffen haben, dass es Ihnen gehört oder dass es inhaltlich stimmt, und er **garantiert keine Rechtswirkung**. Ich sage das an vielen Stellen der Website, weil falsche Erwartungen am meisten Schaden anrichten.

### Offen sagen, was erfasst wird

Um Missbrauch zu verhindern, Limits durchzusetzen, Fehler zu suchen und die Nutzung zu verstehen, wird jede Nutzung mit der IP-Adresse und einigen weiteren Angaben protokolliert. Diese Daten werden nicht für Werbung genutzt und nicht verkauft. IP-Adressen und Hostnamen bleiben 30 Tage auf diesem Server, danach liegen sie bis zu 13 Monate auf einem separaten Speicher, den ich selbst verwalte; anschließend wird das Ende der Adresse entfernt und es bleibt nur die Statistik. Die Einzelheiten stehen in den [Nutzungsbedingungen](/de/terms).

## Für alle

Es ist kostenlos und braucht kein Konto. Die Oberfläche gibt es in 20 Sprachen. Dazu kommen ein Stempel für Fotos, die Möglichkeit, eine veröffentlichte URL festzuhalten, eine API und ein WordPress-Plugin. Das [Plugin können Sie auf der API-Seite herunterladen](/api#wordpress); ein Eintrag auf wordpress.org ist in Prüfung.

Wie Sie Fotos und Entwürfe Schritt für Schritt mit einem Datum versehen und was dabei im deutschsprachigen Raum gilt, steht in „[So zeigen Sie, dass Ihr Werk zuerst da war](/de/column/prove-you-made-it-first)“.

## Sagen Sie mir, was nicht funktioniert

Ich würde gern hören, wo DateSealed Ihnen im Weg steht und was es als Nächstes können sollte – besonders von Fotografinnen, Fotografen und Bloggern, die schon einmal in einem Streit darüber standen, wer zuerst da war. Die Kontaktdaten stehen unten auf der Seite.
