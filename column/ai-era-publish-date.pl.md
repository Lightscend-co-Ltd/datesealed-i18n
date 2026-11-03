title: Data publikacji to deklaracja autora: jak w erze AI zachować datę, której nikt nie przepisze
description: Przepisanie artykułu trwa chwilę, a data w CMS niczego nie dowodzi. Jak zdobyć datę od strony trzeciej dla każdego wpisu, także automatycznie w WordPressie.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Wyobraź sobie, że rano po publikacji pojawia się niemal kopia twojego tekstu: akapity w innej kolejności, inne sformułowania, ten sam szkielet. Jak pokażesz, że twój był pierwszy?

## Przepisywanie stało się tanie

Parafraza, przebudowa i tłumaczenie kiedyś wymagały czasu człowieka. Teraz model językowy robi to w chwilę. Liczby pokazują, jak powszechne są już treści pisane i czytane przez maszyny.

| Źródło | Ustalenie |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% ruchu w sieci w 2024 r. było zautomatyzowane; złośliwe boty stanowiły 37%, wobec 32% rok wcześniej[^imperva] |
| Cloudflare, lipiec 2025 | Liczba żądań GPTBot w jego sieci wzrosła o 305% od maja 2024 do maja 2025[^cf1] |
| Cloudflare, sierpień 2025 | Około 80% indeksowania przez boty AI w poprzednim roku służyło trenowaniu modeli[^cf2] |
| NewsGuard | Serwisy informacyjne publikujące treści AI przy niewielkim nadzorze człowieka: 49 w maju 2023, 3749 do czerwca 2026[^newsguard] |
| Ahrefs, maj 2025 | 74,2% z 900 000 stron opublikowanych po raz pierwszy w kwietniu 2025 zawierało jakąś treść wygenerowaną przez AI[^ahrefs] |
| Praca z NeurIPS 2023 | Model parafrazujący obniżył skuteczność detektora tekstu AI z 70,3% do 4,6%[^neurips] |

To szacunki firm i badaczy, każdy z własną metodą, i żaden nie mówi, jakie jest ryzyko skopiowania *twojego* wpisu. Pokazują natomiast, że przepisywanie jest łatwe i trudne do wykrycia.

## Data publikacji to deklaracja autora

Datę publikacji wybierasz sam. WordPress pozwala opublikować wpis z datą wsteczną i zmienić datę wpisu, który już jest w sieci.[^wp] Data na cudzej stronie jest tak samo deklaracją, więc dwie osoby mówiące „byłem pierwszy” niczego nie rozstrzygają. Archiwa internetowe pomagają, ale nie decydujesz, czy i kiedy zapiszą twoją stronę.

Potrzeba, żeby **ktoś inny niż ty** zapisał datę **w chwili publikacji**, w miejscu, którego **nikt nie może później przepisać**.

## Co robi DateSealed

- Otrzymuje wyłącznie **skrót SHA-256** wpisu, liczony w przeglądarce (albo na twoim serwerze, jeśli używasz wtyczki WordPress). Sam tekst nie jest wysyłany.
- Dołącza **znacznik czasu RFC 3161**, zwracany od razu, i **zapis w Bitcoinie** przez OpenTimestamps, zakotwiczony w ciągu kilku godzin.
- Nikt nie może dopisać czasu do rejestru Bitcoina po fakcie. Po zakotwiczeniu datę da się sprawdzić samym plikiem dowodu i rejestrem, nawet jeśli DateSealed zniknie.

Więcej w tekstach „[Jak pokazać, że twoje było pierwsze](/pl/column/prove-you-made-it-first)” i „[Dlaczego zbudowałem DateSealed](/pl/column/why-i-built-datesealed)”.

## Automatycznie w WordPressie

Nawyk, o którym trzeba pamiętać, nie przetrwa pracowitego tygodnia. Wtyczka DateSealed do WordPressa:

- przy każdej publikacji i aktualizacji liczy skrót treści wpisu na twoim serwerze i wysyła tylko skrót;
- przy każdej aktualizacji **dodaje nowy zapis**, więc pierwsza publikacja nigdy nie zostaje nadpisana, a historia wersji się powiększa;
- może pokazywać plakietkę z odnośnikiem do strony zapisu (opcjonalnie);
- wymaga WordPressa 5.8+ i PHP 8.2+.

[Pobierz ją ze strony API](/api#wordpress), a potem w WordPressie wybierz *Plugins → Add New → Upload Plugin*, włącz wtyczkę i otwórz *Settings → DateSealed*. Wpis w katalogu wordpress.org czeka na weryfikację.

## Czego zapis nie mówi

- Nie pokazuje, czy tekst napisał człowiek, czy model.
- Nie pokazuje, że treść jest prawdziwa lub oryginalna, kto ją napisał ani do kogo należy.
- **Nie gwarantuje skutków prawnych.** W UE domniemanie dokładności daty i czasu ma kwalifikowany elektroniczny znacznik czasu,[^eidas] a polski Kodeks cywilny wiąże z nim datę pewną.[^kc] Zapis DateSealed nie jest żadnym z nich.

„To istniało w tym momencie” to dobry punkt wyjścia do rozmowy. Sam jej nie zakończy. Traktuj zapis jako jeden z dowodów, obok pozostałych.

## Nawyki, dzięki którym zapis jest coś wart

1. **Zachowaj oryginał.** DateSealed przechowuje tylko skróty.
2. **Zachowaj pliki dowodu.** Trzymaj `.tsr` i `.ots` razem z oryginałem, żeby móc je sprawdzić bez DateSealed.
3. **Zapisuj w chwili publikacji.** Czas zapisu to chwila, w której go zrobiłeś; każdy dzień zwłoki go osłabia.
4. **Nie przeceniaj go.** W ważnej sprawie dodaj poświadczenie notarialne albo kwalifikowany znacznik czasu.

[^imperva]: Imperva, „2025 Imperva Bad Bot Report” (15 kwietnia 2025; dane z sieci Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog Cloudflare (1 lipca 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog Cloudflare (29 sierpnia 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, „AI Tracking Center” <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, „What Percentage of New Content Is AI-Generated?” (19 maja 2025; własny detektor Ahrefs, który według firmy nie jest doskonały) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna i in., „Paraphrasing evades detectors of AI-generated text”, NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, „Write Posts (Classic Editor)” <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^eidas]: Rozporządzenie eIDAS (UE) nr 910/2014, art. 41 ust. 2 <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted> (tekst w wersji przejętej przez prawo brytyjskie)
[^kc]: Kodeks cywilny, art. 81 § 2 pkt 3 (tekst jednolity Dz.U. 2026 poz. 795) <https://eli.gov.pl/api/acts/DU/2026/795/text/T/D20260795L.pdf>
