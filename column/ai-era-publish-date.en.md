title: Your Publish Date Is Self-Reported: Keeping a Date No One Can Rewrite in the Age of AI
description: A CMS publish date proves nothing, and AI makes rewriting cheap. How to give every post a third-party date, automate it on WordPress, and know its limits.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Suppose that the morning after you publish, a near-copy appears: paragraphs reordered, phrasing changed, the skeleton identical. How would you show that yours came first?

## Rewriting has become cheap

Paraphrasing, restructuring and translating used to take human time. Now a language model does it in moments. The numbers show how common machine-written and machine-read content already is.

| Source | Finding |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% of web traffic in 2024 was automated; malicious bots made up 37%, up from 32%[^imperva] |
| Cloudflare, July 2025 | GPTBot requests grew 305% from May 2024 to May 2025 on its network[^cf1] |
| Cloudflare, August 2025 | About 80% of AI crawling over the previous year was for model training[^cf2] |
| NewsGuard | News sites publishing AI-generated content with little human oversight: 49 in May 2023, 3,749 by June 2026[^newsguard] |
| Ahrefs, May 2025 | 74.2% of 900,000 pages first published in April 2025 contained some AI-generated content[^ahrefs] |
| NeurIPS 2023 paper | A paraphrasing model cut an AI-text detector's accuracy from 70.3% to 4.6%[^neurips] |

These are vendor or researcher estimates, each with its own method, and none of them is the chance that *your* post gets copied. They do show that rewriting is easy and hard to detect.

## Your publish date is self-reported

You choose your publish date. WordPress lets you publish with a past date and change the date of a live post.[^wp] The other site's date is just as self-reported, so two people saying "I was first" settles nothing. Web archives help, but you do not control whether or when they capture your page.

Nor is there an official register to fall back on everywhere. The UK has no register of copyright works,[^ukgov] and Australian law has no registration system for copyright.[^auipa] The US does have one, but it is an application you file and pay for, not something that happens when you press Publish.

What you need is for **someone other than you** to write down the date **when you publish**, somewhere **nobody can rewrite later**.

## What DateSealed does

- It receives only the **SHA-256 hash** of your post, computed in your browser (or on your own server with the WordPress plugin). The text is never sent.
- It attaches an **RFC 3161 time stamp**, returned immediately, and a **Bitcoin record** through OpenTimestamps, anchored within hours.
- Nobody can write a time into the Bitcoin ledger after the fact. Once anchored, the date can be checked with the proof file and the ledger alone, even if DateSealed disappears.

More detail is in "[How to show you made it first](/column/prove-you-made-it-first)" and "[Why I built DateSealed](/column/why-i-built-datesealed)".

## Automatic on WordPress

A habit you must remember will not survive a busy week. The DateSealed WordPress plugin:

- computes the hash of the post text on your server at every publish and update, and sends only the hash;
- **adds a new record** for each update, so the first publication is never overwritten and the revision history builds up;
- can show a badge linking to the record page (optional);
- needs WordPress 5.8+ and PHP 8.2+.

[Download it from the API page](/api#wordpress), then in WordPress go to *Plugins → Add New → Upload Plugin*, activate it and open *Settings → DateSealed*. A wordpress.org listing is under review.

## What the record does not say

- It does not show whether a human or a model wrote the text. That question has legal weight of its own: in January 2025 the US Copyright Office concluded that AI outputs are protected only where a human author determined sufficient expressive elements, and that prompts alone are not enough.[^usai] A dated hash cannot answer it.
- It does not show that the content is accurate or original, who wrote it, or who owns it.
- It does **not guarantee legal effect**. It is not a US copyright registration,[^us17] and it is not a qualified electronic time stamp, which UK law presumes accurate as to date, time and data integrity.[^ukeidas]

"It existed at this time" is a useful place to start a conversation. It will not settle one by itself. Use the record as one piece of evidence next to the rest.

## Habits that make the record worth having

1. **Keep the original.** DateSealed holds only hashes.
2. **Keep the proof files.** Store the `.tsr` and `.ots` with the original so you can verify without DateSealed.
3. **Record at publish time.** The record's time is when you made it; every day of delay weakens it.
4. **Do not oversell it.** For a post that matters, add the formal route where you are: in the US, registration, which you need before suing over a US work and which governs whether statutory damages are available;[^us17] in the UK, a qualified time stamp.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (April 15, 2025; Imperva network data) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare blog (July 1, 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare blog (August 29, 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (May 19, 2025; Ahrefs' own detector, which it notes is imperfect) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^ukgov]: GOV.UK, "How copyright protects your work" <https://www.gov.uk/copyright>
[^auipa]: IP Australia, "Beware of unofficial invoices, correspondence and registers" <https://www.ipaustralia.gov.au/about-us/doing-business-with-us/fraud-and-corruption/beware-of-unofficial-invoices-correspondence-and-registers>
[^usai]: US Copyright Office, NewsNet Issue 1060 (January 29, 2025), on "Copyright and Artificial Intelligence, Part 2: Copyrightability" <https://www.copyright.gov/newsnet/2025/1060.html>
[^us17]: 17 U.S.C. §§ 411(a), 412 <https://www.copyright.gov/title17/92chap4.html>
[^ukeidas]: UK eIDAS (Regulation (EU) No 910/2014 as retained in UK law), Article 41 <https://www.legislation.gov.uk/eur/2014/910/article/41>
