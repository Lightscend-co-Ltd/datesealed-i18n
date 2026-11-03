# DateSealed translations

The interface text and the articles of [DateSealed](https://datesealed.com/) (a free tool that records when a text, photo or web page existed) in 20 languages.

**The translations were written with AI and have not been reviewed by native speakers yet. If you read one of these languages, you can make them better.** It takes a minute.

## The easiest way: report one sentence

Open an [issue with the translation form](../../issues/new/choose), pick the language, paste the sentence that sounds wrong and write what it should say. That is all.

## Editing the files yourself

Every language is one file in [`lang/`](lang/) (`ja.json`, `fr.json`, …). The English file, [`lang/en.json`](lang/en.json), is the source. You can edit a file in your browser (the pencil icon on GitHub) and open a pull request. A check runs automatically and tells you if something is off (a missing key, a leftover English sentence, and so on); we also read each change before using it.

## Please keep

- **The legal wording.** DateSealed does **not** guarantee legal effect, and people who need an accredited timestamp should use an accredited provider. Please never make a record sound "certified", "official" or like "legal proof". The sentences in `footer` and `terms.not_p` must keep their negation.
- **One word per idea.** Choose one word for "record" and one for "hash" and use it everywhere in your language.
- **Brand and technical names as they are:** DateSealed, Bitcoin, OpenTimestamps, RFC 3161, SHA-256, `.tsr`, `.ots`, WordPress, API.
- **The keys and their order.** Change only the values (the text on the right).

## The articles

The [articles](https://datesealed.com/column) are in [`column/`](column/), one Markdown file per article and language (`prove-you-made-it-first.fr.md`, …), plus the few words around them in [`column/ui/`](column/ui/). They are not word-for-word translations: each language version uses examples from the countries where it is read (registration offices, notaries, electronic timestamp law, fees). They were written with AI, and every local fact was checked against an official source linked in the footnotes, but no native speaker or lawyer has read them yet.

Help is welcome with any of these:

- **A sentence that sounds unnatural.** Use the [form](../../issues/new/choose), as above.
- **A local fact that is wrong or out of date** (a fee, a law, the name of an office). Tell us what it should say and, if you can, link the official page.
- **A source link that does not open** in your browser. Some official sites block automatic checks, so we cannot always tell.

When you edit an article, keep the line `---` and the lines above it (`title`, `description`, `date`, `author`), keep links to the site with the language prefix (`/fr/stamp`, not `/stamp`), and do not add claims about DateSealed that the English version does not make. `python scripts/validate_column.py fr` checks the format.

More detail: [TRANSLATION_BRIEF.md](TRANSLATION_BRIEF.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Credit and license

Contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md) (tell us if you would rather not be). Contributions are made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and are used on datesealed.com.

DateSealed is operated by Lightscend Co., Ltd.

---

## 日本語

[DateSealed](https://datesealed.com/ja/) の画面の文言を 20 言語で管理しています。翻訳は AI で作ったもので、母語話者の確認はまだです。不自然な文を見つけたら、[翻訳の修正フォーム](../../issues/new/choose)から、言語・直したい文・直し方を送ってください。1 文だけでも助かります。

[コラム](https://datesealed.com/ja/column)の記事も [`column/`](column/) にあります。各言語版は、その言語が読まれる国の制度(登録・公証・電子タイムスタンプの法律・料金)を例にして書いており、直訳ではありません。AI で書き、各国の事実は脚注の公式の出典で確かめましたが、母語話者や法律家はまだ読んでいません。不自然な文、古い・誤った制度や料金、開けない出典リンクを見つけたら、同じフォームから知らせてください。
