title: 公開日は自己申告 ― AI 時代のブログに「書き換えられない日付」を残す
description: 生成 AI で記事の言い換えや複製が簡単になった今、CMS の公開日だけでは「どちらが先か」を示せません。公開のたびに第三者の台帳へ日付を残す方法と、WordPress での自動化、その限界をまとめました。
date: 2026-11-03
author: 中澤祐樹(ライトセンド株式会社)
source: https://nkzw.jp/2026/11/03/datesealed_ai_era_date_record_2026/
---
記事を公開した翌日に、段落の順番と言い回しだけを変えた、よく似た記事が出ていたら。「先に書いたのは自分だ」と、何で示せるでしょうか。

## 言い換えと複製は、簡単になった

文章を言い換える、構成を変える、別の言語に訳す。以前は人の時間がかかった作業が、今は生成 AI に頼めば短い時間で済みます。調査を見ると、AI が書いた文章はすでにありふれています。

| 調査 | わかったこと |
|---|---|
| Graphite(2026 年 5 月) | Common Crawl の記事 5.54 万本のうち、2026 年第 1 四半期は 49.9% が「主に AI が書いた」と判定[^graphite] |
| Ahrefs(2025 年 5 月) | 2025 年 4 月の新規ページ 90 万件の 74.2% に、AI が生成した部分が含まれていた[^ahrefs] |
| NewsGuard | 人の監督なしに AI 記事を量産するニュースサイトは、2023 年 5 月の 49 から 2026 年 6 月には 3,749 に[^newsguard] |
| NeurIPS 2023 の論文 | 言い換え用のモデルを通すと、AI 文章の検出精度が 70.3% から 4.6% に下がった[^neurips] |

いずれも各社の基準や検出器による推計で、「あなたの記事が複製される確率」を示すものではありません。それでも、言い換えが機械的にでき、見分けにくくなっていることはわかります。

## 公開日は、自己申告でしかない

ブログの公開日は自分で決められます。WordPress では、過去の日付で公開することも、公開済みの記事の日付を変えることもできます。[^wp] 相手の記事の日付も同じです。互いに「こちらが先だ」と言い合うだけでは決着しません。

Internet Archive のような第三者の保存は役に立ちますが、公開直後に保存されているとは限りません。必要なのは、**公開したその場で、自分以外の誰かに日付を書いてもらい、誰にも書き換えられない場所に置く**ことです。

## DateSealed がすること

- 記事そのものではなく、記事の **SHA-256 ハッシュ**だけを受け取ります。計算はブラウザ(WordPress ならあなたのサーバー)の中で行い、本文は送られません。
- ハッシュに、すぐ返る **RFC 3161 の時刻署名**と、数時間で刻まれる**ビットコインの記録**(OpenTimestamps)を付けます。
- ビットコインに刻まれた時刻を、後から過去に作ることはできません。DateSealed が無くなっても、証明ファイルと台帳だけで確かめられます。

仕組みの詳しい説明は、コラム「[「先に作ったのは自分だ」と示すための準備](/ja/column/prove-you-made-it-first)」と「[なぜ DateSealed を作ったのか](/ja/column/why-i-built-datesealed)」にあります。

## WordPress なら、公開のたびに自動で

手で続ける習慣は途切れます。DateSealed の WordPress プラグインは、次のように動きます。

- 記事を公開・更新するたびに、あなたのサーバーの中で本文のハッシュを計算し、ハッシュだけを送ります。
- 更新のたびに**新しい記録を追加**します。最初の公開の記録は上書きされず、改訂の履歴が残ります。
- 記事の末尾に、記録ページへのバッジを出せます(設定で選べます)。
- WordPress 5.8 以上、PHP 8.2 以上で動きます。

入手は [API のページ](/api#wordpress)からのダウンロードです。管理画面の「プラグイン → 新規追加 → プラグインのアップロード」で zip を選んで有効化し、「設定 → DateSealed」で使い方を選びます。wordpress.org への掲載は審査中です。

## 記録が示さないこと

- 記事を人間が書いたのか、AI が書いたのかは示しません。
- 内容が正しいこと、独創的であること、誰が書いたか、権利を持っているかも示しません。
- **法的効力は保証しません。** 日本で制度上の位置づけがあるのは、総務大臣が認定した時刻認証業務のタイムスタンプです。[^soumu]

「先に存在していた」という一点は、話し合いの出発点として意味があります。ただし、それだけで決着がつくとは限りません。DateSealed の記録は「証拠の一つ」として、ほかの証拠と並べて使ってください。

## 記録を取るときの作法

1. **元のデータを残す。** DateSealed が持っているのはハッシュだけです。
2. **証明ファイルを保管する。** `.tsr` と `.ots` を元のデータと一緒に置けば、DateSealed に頼らず検証できます。
3. **公開と同時に記録する。** 記録の時刻は記録を取った時刻です。公開から日が空くほど、証拠は弱くなります。
4. **過度に期待しない。** 本気で争う案件では、文化庁の登録や認定タイムスタンプも組み合わせてください。

[^graphite]: Graphite「AI Now Writes as Many Online Articles as Humans Do」(2026 年 5 月 15 日、3 種類の検出器の平均による推計) <https://graphite.io/five-percent/ai-now-writes-as-many-online-articles-as-humans-do>
[^ahrefs]: Ahrefs「What Percentage of New Content Is AI-Generated?」(2025 年 5 月 19 日、自社の検出器による推計) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^newsguard]: NewsGuard「AI Tracking Center」 <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^neurips]: Krishna ほか「Paraphrasing evades detectors of AI-generated text」NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org「Write Posts (Classic Editor)」 <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^soumu]: 総務省「タイムスタンプ(時刻認証業務)の認定制度」 <https://www.soumu.go.jp/main_sosiki/joho_tsusin/top/ninshou-law/timestamp.html>
