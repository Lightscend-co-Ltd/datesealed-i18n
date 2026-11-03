title: Jak pokazać, że twoje było pierwsze: data od strony trzeciej dla zdjęć i szkiców
description: Każdą datę, którą masz u siebie, da się zmienić. Jak za darmo i bez wysyłania plików zapisać, że zdjęcie lub tekst istniały danego dnia, i czego to dowodzi.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Jeśli ktoś skopiuje twoją pracę, czy zdołasz pokazać, że twoja była pierwsza? Ten poradnik wyjaśnia, jak przygotować się na taką chwilę — za darmo i bez pokazywania pracy komukolwiek.

## Każdą datę, którą masz, da się zmienić

Problem z dowodami daty jest prosty: wszystko, co możesz zmienić sam, druga strona może uznać za zmienione przez ciebie.

| Data, którą masz | Dlaczego jest słaba |
|---|---|
| Data publikacji w CMS | Można ustawić datę wsteczną. WordPress opisuje, jak to zrobić.[^wp] |
| Metadane zdjęcia (Exif) | Darmowe narzędzia, takie jak ExifTool, je edytują, także hurtowo przesuwając daty.[^exif] |
| Daty plików | W Windows skopiowany plik dostaje nową datę utworzenia (data modyfikacji zostaje).[^kb] |
| Zrzuty ekranu | Można je edytować jak każdy obraz. |

Każda z nich jest lepsza niż nic, ale żadna nie odpowiada na pytanie „czy nie zrobiłeś tego później?”. Potrzebna jest data zapisana przez **kogoś innego niż ty**, w formie, której **nikt nie może później zmienić**.

## Co w Polsce służy do wykazania daty

**Prawo autorskie nie wymaga formalności.** Utwór jest chroniony od chwili ustalenia, nawet nieukończony, a ustawa mówi wprost: „Ochrona przysługuje twórcy niezależnie od spełnienia jakichkolwiek formalności”.[^upa] Domniemywa się też, że twórcą jest osoba, której nazwisko w tym charakterze uwidoczniono na egzemplarzach utworu.[^upa] Prawo powstaje więc samo, ale w sporze i tak trzeba wykazać, czyja wersja istniała wcześniej.

**Notariusz poświadcza datę okazania dokumentu.** To jedno z poświadczeń wymienionych w Prawie o notariacie; na żądanie notariusz wpisuje także godzinę i minutę.[^not] Od 5 listopada 2026 r. maksymalna taksa za poświadczenie czasu okazania dokumentu wynosi 12 zł za każdą rozpoczętą stronę od 1 do 10, 10 zł za strony od 11 do 20 i 8 zł od strony 21.[^taksa] Według Kodeksu cywilnego wzmianka notariusza na dokumencie daje objętej nim czynności prawnej tzw. datę pewną.[^kc]

**Kwalifikowany elektroniczny znacznik czasu.** W całej UE korzysta z domniemania dokładności daty i czasu oraz integralności danych, z którymi są połączone.[^eidas] W Polsce Kodeks cywilny dodaje, że czynność prawna w dokumencie elektronicznym opatrzonym takim znacznikiem ma datę pewną od chwili jego opatrzenia.[^kc]

Zapis DateSealed **nie jest** ani poświadczeniem notarialnym, ani kwalifikowanym znacznikiem czasu i nie daje tych skutków.

## Zapis w DateSealed

1. Otwórz [stronę główną](/pl/) i wklej tekst albo wybierz plik. Możesz też podać adres URL lub posiadany już skrót SHA-256.
2. Sprawdź wyświetlony skrót SHA-256 i naciśnij przycisk zapisu. Skrót jest liczony w przeglądarce, więc sam plik ani tekst nie są nigdzie wysyłane.
3. Otworzy się strona zapisu. Pobierz `.tsr` (podpisany znacznik czasu) i `.ots` (dowód w Bitcoinie) i przechowuj je **razem z oryginalnym plikiem**.

Każdy zapis dostaje dwie daty: znacznik czasu RFC 3161 zwracany od razu i zapis OpenTimestamps zakotwiczony w bloku Bitcoina w ciągu kilku godzin. Po zakotwiczeniu datę da się sprawdzić samym rejestrem Bitcoina, nawet jeśli DateSealed przestanie działać. Na stronie zapisu są polecenia do weryfikacji na własnym komputerze.

Limity: 10 zapisów na godzinę i 50 na dobę z jednego adresu IP.

## Publikujesz zdjęcia? Użyj stempla

[Stempel na zdjęcia](/pl/stamp) zapisuje skrót oryginału, a potem w przeglądarce tworzy kopię z małą plakietką z datą zapisu i adresem strony zapisu. Samo zdjęcie nie jest wysyłane.

Zapis dotyczy **oryginału**. Ostemplowana kopia to inny plik, a plakietkę można wyciąć — sama niczego nie dowodzi. Publikuj kopię ze stemplem, a oryginał trzymaj bezpiecznie.

## Co zapis pokazuje, a czego nie

Pokazuje, że **dane pasujące do tego skrótu istniały w zapisanym momencie**. Tylko tyle.

- Nie pokazuje, że treść jest prawdziwa ani oryginalna.
- Nie pokazuje, że to ty ją stworzyłeś ani że do ciebie należy. Zapis nie mówi, kto jest autorem.
- **Nie gwarantuje skutków prawnych.** Nie nadaje daty pewnej w rozumieniu Kodeksu cywilnego i nie jest kwalifikowanym znacznikiem czasu w rozumieniu eIDAS.

## Do tej jednej rzeczy, którą naprawdę trzeba chronić

Sięgnij też po formalne środki: poświadczenie daty u notariusza albo kwalifikowany elektroniczny znacznik czasu. DateSealed to tania i szybka pierwsza warstwa dla stałego strumienia zdjęć, artykułów i szkiców — jeszcze jeden dowód, który kładzie się obok pozostałych.

## Dwie rzeczy do zapamiętania

- **Zachowaj oryginał.** DateSealed przechowuje tylko skrót. Bez oryginalnego pliku zapisu nie da się z niczym powiązać.
- **Zapisuj ponownie po każdej zmianie.** Zmiana jednego znaku zmienia skrót. W WordPressie [wtyczka](/api#wordpress) zapisuje każdą publikację i aktualizację za ciebie.

[^wp]: WordPress.org, „Write Posts (Classic Editor)” <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Microsoft Knowledge Base, artykuł KB299648 (jak traktowane są daty przy kopiowaniu i przenoszeniu plików)
[^upa]: Ustawa z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych, art. 1 ust. 3–4 i art. 8 ust. 2 (tekst jednolity Dz.U. 2025 poz. 24) <https://api.sejm.gov.pl/eli/acts/DU/2025/24/text.pdf>
[^not]: Ustawa z dnia 14 lutego 1991 r. – Prawo o notariacie, art. 96 pkt 3 i art. 99 § 1 (tekst jednolity Dz.U. 2026 poz. 614) <https://eli.gov.pl/api/acts/DU/2026/614/text/T/D20260614L.pdf>
[^taksa]: Rozporządzenie Ministra Sprawiedliwości z dnia 13 października 2026 r. zmieniające rozporządzenie w sprawie maksymalnych stawek taksy notarialnej, § 1 pkt 6 (Dz.U. 2026 poz. 1370) <https://api.sejm.gov.pl/eli/acts/DU/2026/1370/text/O/D20261370.pdf>
[^kc]: Kodeks cywilny, art. 81 § 2 pkt 2 i 3 (tekst jednolity Dz.U. 2026 poz. 795) <https://eli.gov.pl/api/acts/DU/2026/795/text/T/D20260795L.pdf>
[^eidas]: Rozporządzenie eIDAS (UE) nr 910/2014, art. 41 ust. 2 <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted> (tekst w wersji przejętej przez prawo brytyjskie)
