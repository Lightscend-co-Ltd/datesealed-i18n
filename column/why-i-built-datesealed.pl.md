title: Dlaczego zbudowałem DateSealed — notatka od autora
description: Zaczęło się od zdjęć nieruchomości. Co znalazłem wśród istniejących rozwiązań i jakie zasady przyjąłem dla darmowego zapisu daty, którego sam nie mogę zmienić.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed to darmowe narzędzie, które zapisuje, kiedy istniał dany tekst, zdjęcie albo strona internetowa. Nazywam się Yuki Nakazawa i to ja je zbudowałem. Ta notatka wyjaśnia, dlaczego, i jakie decyzje podjąłem po drodze.

## Zaczęło się od zdjęć nieruchomości

Prowadzę w Japonii firmę z branży nieruchomości. Fotografujemy oferty i publikujemy je w sieci. Chciałem być przygotowany na dzień, w którym ktoś przerobi któreś z tych zdjęć albo wrzuci je na inną stronę — tak, żebym mógł pokazać, że oryginał jest nasz i powstał wcześniej.

Miałem pliki źródłowe, a wpisy miały daty publikacji. Każdą z tych dat mogłem jednak sam zmienić, a każdy, kto ma kopię, może powołać się na te same daty. Potrzebowałem daty zapisanej przez **kogoś innego niż ja**, w formie, której **nikt nie może później zmienić**.

## Co znalazłem najpierw

Sprawdziłem, co było dostępne w Japonii w listopadzie 2026 r.

- **Data pewna nadana przez notariusza.** 700 jenów za dokument. Istnieje wersja elektroniczna, ale przyjmuje tylko pliki tekstowe, PDF i XML do 10 MB, a procedura działa w dni robocze.
- **Rejestracja w japońskiej Agencji do Spraw Kultury.** 3000 jenów za utwór, wniosek papierowy, jeden utwór naraz. Daje domniemanie, że utwór opublikowano w zarejestrowanym dniu.
- **Znaczniki czasu od dostawców akredytowanych przez japońskie Ministerstwo Spraw Wewnętrznych i Komunikacji.** To one mają w Japonii status urzędowy. Cenniki są skierowane głównie do firm.
- **Usługi zapisu oparte na blockchainie.** Te, które znalazłem, były dla firm albo płatne.
- **Podpis w aparacie (C2PA).** Niektóre aparaty podpisują zdjęcie w chwili wykonania. To mówi, skąd pochodzi plik — a to inne pytanie niż to, kiedy istniał.

Wszystko to jest przydatne i do tej jednej rzeczy, którą naprawdę trzeba chronić, warto z tego korzystać. Ale płacenie i składanie wniosków przy każdym nowym zdjęciu czy artykule nie jest realne. Chciałem czegoś **darmowego, bez rejestracji, bez wysyłania plików, przechowywanego tam, gdzie nawet operator niczego nie zmieni, i działającego automatycznie w WordPressie przy każdej publikacji**. Nie znalazłem, więc zbudowałem.

## Zasady, które przyjąłem

### Nie brać niczego poza skrótem

DateSealed otrzymuje wyłącznie skrót SHA-256 pliku lub tekstu — 64-znakowy „odcisk palca”. Skrót jest liczony w przeglądarce, więc zdjęcia i szkice nie opuszczają komputera. Ludzie chcą zapisywać właśnie prace jeszcze nieopublikowane, a oddawanie ich komuś, żeby je zapisać, przeczyłoby całemu celowi.

### Nie musisz mi ufać

Każdy zapis dostaje dwie daty. Pierwsza to znacznik czasu RFC 3161 podpisany przez własny urząd znakowania czasem DateSealed, zwracany od razu. Druga zostaje zakotwiczona w bloku Bitcoina przez OpenTimestamps, zwykle w ciągu kilku godzin.

Pierwsza jest warta tyle, ile moja wiarygodność. Drugiej nie mogę zmienić. Po zakotwiczeniu datę da się sprawdzić samym plikiem dowodu (`.ots`) i rejestrem Bitcoina, nawet jeśli DateSealed przestanie istnieć. Na każdej stronie zapisu są polecenia do weryfikacji na własnym komputerze.

Klucz główny urzędu znakowania czasem powstał na moim komputerze i jest przechowywany zaszyfrowany hasłem. Na serwerze jest tylko klucz do podpisywania.

### Nigdy nie usuwać, nigdy nie przepisywać

Nawet panel administracyjny nie ma funkcji usunięcia zapisu ani zmiany jego skrótu czy czasu. Rejestr jest coś wart tylko wtedy, gdy jego operator nie może go ruszyć. Kiedy aktualizujesz wpis, stary zapis zostaje, a dochodzi nowy. Wtyczka WordPress działa według tej samej zasady.

### Od razu mówić, czego nie potrafi

Zapis pokazuje, że dane pasujące do skrótu istniały w danym momencie. Nic więcej. Nie pokazuje, że to ty je stworzyłeś, że należą do ciebie ani że są prawdziwe, i **nie gwarantuje skutków prawnych**. Piszę o tym w wielu miejscach serwisu, bo błędne oczekiwania to najprostsza droga do szkody.

### Mówić wprost, co jest zbierane

Żeby zapobiegać nadużyciom, pilnować limitów, szukać błędów i rozumieć, jak serwis jest używany, przy każdym użyciu zapisuję adres IP i kilka innych informacji. Nie służą one do reklamy i nie są sprzedawane. Adresy IP i nazwy hostów zostają na tym serwerze przez 30 dni, potem trafiają do osobnego magazynu, którym zarządzam, na maksymalnie 13 miesięcy. Po tym czasie końcówka adresu jest usuwana i zostają tylko statystyki. Szczegóły są w [regulaminie](/pl/terms).

## Dla każdego

Narzędzie jest darmowe i nie wymaga konta. Interfejs jest dostępny w 20 językach. Jest też stempel na zdjęcia, zapis opublikowanego adresu URL, API i wtyczka WordPress. [Wtyczkę można pobrać ze strony API](/api#wordpress); wpis w katalogu wordpress.org czeka na weryfikację.

Jak przygotować się na spór o pierwszeństwo w praktyce, opisuję w poradniku „[Jak pokazać, że twoje było pierwsze](/pl/column/prove-you-made-it-first)”.

## Napisz, co nie działa

Chętnie dowiem się, gdzie DateSealed przeszkadza i co powinien robić dalej — szczególnie od fotografów i blogerów, którzy byli już w sporze o to, „kto był pierwszy”. Dane kontaktowe są na dole strony.
