# Contributing a translation

Thank you. A few rules keep the translations safe and consistent.

1. **Write for a native reader.** Natural, short, friendly and trustworthy. Not word for word.
2. **Keep the legal wording intact.** The tool records that data existed at a time; it does not guarantee legal effect. Do not use words that mean "certified", "accredited" (for DateSealed itself), "official" or "legal proof". The "accredited timestamp (certified by Japan's Minister of Internal Affairs and Communications)" sentence refers to other providers, and the advice to use one must stay.
3. **Do not promise more than the English.** The record shows that data matching a hash existed at the recorded time. It does not show that the content is true or who made it.
4. **Keep keys and key order.** Only change values. Values are plain text (no HTML, no Markdown, no placeholders).
5. **Consistency.** One word for "record", one for "hash", one for "Bitcoin ledger" (or "blockchain" if that is what readers in your language say).
6. **Brand and technical names stay in Latin letters:** DateSealed, Bitcoin, OpenTimestamps, RFC 3161, SHA-256, .tsr, .ots, WordPress, API.
7. **Right-to-left languages (Arabic):** translate normally; do not insert direction marks.

## Articles (`column/`)

The articles follow the same rules, plus:

8. **Write for readers in your country.** Each version uses local examples (how authors usually show they had something first, registration or deposit offices, electronic timestamp law). Keep that; do not translate the English examples back in.
9. **Every local fact needs an official source.** A law, fee, statistic or office goes in a footnote (`[^name]: … <https://…>`) linking a government, court, standards body or the organisation that published the figure. If a fee has no date on the official page, say when it was checked. Do not add a fact you could not check.
10. **Keep the header and the links.** The lines above `---` (`title`, `description`, `date`, `author`, optional `updated` and `source`) stay. Links to the site keep the language prefix (`/fr/stamp`, `/fr/column/…`); the WordPress plugin link stays `/api#wordpress`.
11. **The developer's article** (`why-i-built-datesealed`) is a personal account. Fix the language, not the story.

## Checking your change

```
python scripts/validate_lang.py fr
```

prints `ok` when keys, order and basic rules are fine. For the articles:

```
python scripts/validate_column.py fr
```

checks the header, footnotes and site links. A pull request runs the same check automatically, so you do not have to.

## Licence and credit

By submitting a change you agree that it may be used on datesealed.com and is made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). We list contributors in `CONTRIBUTORS.md`; say so if you prefer not to be listed.

The English source text is maintained by the DateSealed team. If you think the English itself is unclear, open an issue.
