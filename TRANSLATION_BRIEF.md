# DateSealed UI translation brief

Source of truth: `lang/en.json` (English). You write `lang/<code>.json` in the same folder: same keys, same order, UTF-8 JSON
(`ensure_ascii=false`, indent 1). Check with `python scripts/validate_lang.py <code>` until it prints `ok`.
`lang/ja.json` is the Japanese version; use it only to understand intent (the English is the master).

## What the product is
DateSealed is a free web tool. A visitor pastes a text or picks a file; the **browser** computes its SHA-256 hash and only the hash is sent.
The service returns (1) an immediate signed time stamp (RFC 3161) and (2) a record anchored in a Bitcoin block within hours (OpenTimestamps),
which stays verifiable from the Bitcoin ledger even if the service closes. Visitors: photographers, bloggers, affiliates, SEO people, anyone who wants
to show "this existed by this time". The WordPress plugin does it automatically for posts.

## Rules
1. Translate for a native reader: natural, idiomatic, short. Not word for word. UI labels (nav, buttons) must be very short.
2. Keep every key and the key order. Do not add or drop keys. Values are plain text (no HTML, no placeholders). Do not use Markdown.
3. Keep as they are (Latin letters): DateSealed, Bitcoin, OpenTimestamps, RFC 3161, SHA-256, .tsr, .ots, API, WordPress, FAQ, Lightscend Co., Ltd. (`operator` may use the company's name in your language's usual form only if that is standard; otherwise keep "Lightscend Co., Ltd.").
4. **Legal wording is critical.** Never claim or imply that a record has legal effect, is "certified", "accredited", "official" or "legal proof".
   The English says the tool does NOT guarantee legal effect and that people who need an accredited timestamp (certified by Japan's Minister of Internal Affairs
   and Communications) should use an accredited provider. Keep both statements, with the negation, in `footer` and `terms.not_p`. Do not use words meaning "legal proof", "official proof" or "certificate" for the records; call them "record" / "time stamp".
5. Do not promise more than the English: the record shows that data matching the hash existed at the recorded time; it does not show the content is true or who made it.
6. `badge_text` is the phrase placed before the link text "DateSealed" in a badge ("Publication date record DateSealed"): short noun phrase, no colon.
7. `terms.*` are plain legal-ish notices; keep them clear and neutral, no extra obligations or promises.
8. Right-to-left (ar): translate normally; do not insert direction marks.
9. `hash_is`, `or_hash`, `ph_text` etc. are short field labels. `btn_issue` is the main button: a verb phrase ("Record this now").
10. No Japanese characters may remain (zh / zh-tw use Han characters naturally). Do not leave English sentences untranslated (brand/technical terms in rule 3 excepted).
11. Register: friendly, clear, professional; second person where the language normally uses it; no exclamation marks.

## Register per language
ru: formal "вы". uk: "ви", real Ukrainian (no Russian calques). zh: Simplified Chinese, mainland vocabulary. zh-tw: Traditional Chinese, Taiwan vocabulary.
ko: polite formal (합니다/하세요체). es: neutral international Spanish, "tú". pt: Brazilian Portuguese, "você". fr: French (France), "vous". de: German, "Sie".
it: "tu". id: Indonesian, "Anda". vi: "bạn". th: Thai, polite and gender-neutral (no ครับ/ค่ะ). tr: "siz". ar: Modern Standard Arabic.
hi: Hindi (Devanagari), "आप"; common tech terms may stay in Latin script. pl: Polish, direct and friendly. nl: Dutch, "je/jij".
