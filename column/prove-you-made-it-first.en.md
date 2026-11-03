title: How to Show You Made It First: Give Your Photos and Drafts a Third-Party Date
description: How to record, free and without uploading, that a photo or draft existed on a given day, and how that fits next to US, UK and Australian copyright practice.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
If someone copies your work, can you show that yours came first? This guide explains how to prepare for that moment, for free, without showing your work to anyone.

## Every date you hold can be edited

The trouble with date evidence is simple: anything you can change yourself, the other side can say you changed.

| The date you have | Why it is weak |
|---|---|
| Your CMS publish date | You can set a past date. WordPress documents how.[^wp] |
| Photo metadata (Exif) | Free tools such as ExifTool edit it, and can shift dates in bulk.[^exif] |
| File timestamps | On Windows, a copied file gets a new creation time (the modified time is kept).[^kb] |
| Screenshots | They can be edited like any image. |

Each is better than nothing, but none of them answers "couldn't you have made this up afterwards?" What you need is a date written down by **someone other than you**, in a form **nobody can rewrite later**.

## Recording with DateSealed

1. Open the [home page](/) and paste text or pick a file. You can also enter a URL or a SHA-256 you already have.
2. Check the SHA-256 shown and press the button to record it. The hash is computed in your browser, so the file or text itself is never sent.
3. The record page opens. Download the `.tsr` (signed time stamp) and the `.ots` (Bitcoin proof) and keep them **together with the original file**.

Each record gets two dates: an RFC 3161 time stamp returned immediately, and an OpenTimestamps record anchored in a Bitcoin block within hours. Once anchored, the date can be checked against the Bitcoin ledger alone, even if DateSealed shuts down. The record page lists the commands to verify it on your own machine.

The limits are 10 records an hour and 50 a day per IP address.

## Publishing photos? Use the stamp

[Stamp photos](/stamp) records the hash of your original and then, in your browser, makes a copy with a small badge showing the record date and the record page address. The photo itself is not uploaded.

The record points to **the original**. The stamped copy is a different file, and the badge can be cropped out; on its own it proves nothing. Publish the stamped copy and keep the original safe.

## What a record shows, and what it does not

It shows that **data matching this hash existed at the recorded time**. That is all.

- It does not show that the content is accurate or original.
- It does not show that you made it or own it. The record does not say who created it.
- It does **not guarantee legal effect**. It is not a copyright registration, and it is not a qualified electronic time stamp of the kind UK law presumes accurate.[^ukeidas]

Hashes themselves are nothing exotic in court. Since December 1, 2017, US Federal Rule of Evidence 902(14) has let data copied from a device or file be self-authenticated by a qualified person's certification, and the committee note says such copies are ordinarily authenticated by hash value.[^fre][^fjc] That certification settles authenticity only; the other side can still object on other grounds. A DateSealed record is not such a certification, but it rests on the same idea: the hash ties your file to the record.

## For the one thing you really need to protect

In all three countries, copyright arises without any filing. What differs is what you can add on top.

| | United States | United Kingdom | Australia |
|---|---|---|---|
| When copyright starts | When the work is created and fixed in a tangible form[^usfaq] | Automatically; no application or fee[^ukgov] | Free and automatic under the Copyright Act 1968[^aubiz] |
| Official register | Yes, voluntary. Online filing is $45 (Single Application) or $65 (Standard), per the Copyright Office fee schedule as of November 2026[^usfees] | None. There is no register of copyright works in the UK[^ukgov] | None. Australian law has no registration system for copyright[^auipa] |
| What the formal route gives you | For a US work, registration is required before suing. Statutory damages and attorney's fees generally need registration before the infringement began, or within three months of publication. Registration within five years of publication is prima facie evidence[^us17] | A qualified electronic time stamp is presumed accurate as to date, time and data integrity under UK eIDAS[^ukeidas] | No official equivalent. IP Australia notes that private paid registers can give dated evidence of creation, and warns about their downsides[^auipa] |
| Evidence habits suggested | Mailing a copy to yourself is not a substitute for registration, says the Copyright Office[^usfaq] | The British Library's IP guide suggests depositing work with a solicitor or bank, posting it to yourself sealed, and keeping records of digital files and emails[^bl] | If ownership is disputed, creators typically produce original drafts, manuscripts or sketches and call witnesses[^ausa] |

So: in the US, register what matters; it is inexpensive next to a lawsuit, and the timing rules reward doing it early. In the UK and Australia there is nothing to register, so the evidence is yours to build, and the earlier and more independent it is, the better. DateSealed is the cheap, quick first layer for the steady stream of photos, articles and drafts: one more piece of evidence to put next to the rest.

## Two things to remember

- **Keep the original.** DateSealed holds only the hash. Without the original file, the record cannot be tied to anything.
- **Record again after every edit.** Change one character and the hash changes. On WordPress, [the plugin](/api#wordpress) records each publish and update for you.

[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Microsoft Knowledge Base article KB299648 (how dates are handled when files are copied or moved)
[^ukeidas]: UK eIDAS (Regulation (EU) No 910/2014 as retained in UK law), Article 41 <https://www.legislation.gov.uk/eur/2014/910/article/41>
[^fre]: Federal Rules of Evidence, Rule 902(13) and (14), with the 2017 committee notes (Legal Information Institute) <https://www.law.cornell.edu/rules/fre/rule_902>
[^fjc]: Federal Judicial Center, on Rules 902(13) and 902(14), effective December 1, 2017 <https://www.fjc.gov/node/4023016>
[^usfaq]: US Copyright Office, "Copyright in General" (FAQ) <https://www.copyright.gov/help/faq/faq-general.html>
[^usfees]: US Copyright Office, "Fees" (checked November 2026; the same amounts appear in Circular 4, revised 11/2024) <https://www.copyright.gov/about/fees.html>
[^us17]: 17 U.S.C. §§ 410(c), 411(a), 412 <https://www.copyright.gov/title17/92chap4.html>
[^ukgov]: GOV.UK, "How copyright protects your work" <https://www.gov.uk/copyright>
[^bl]: British Library Business & IP Centre, "IP Guide: Copyright" (updated October 2025) <https://www.bl.uk/files/v5dwkion/production/b9766f2e578750bd27ee47911b1625cf37a5e9db.pdf/bipc-ip-guide-copyright.pdf>
[^aubiz]: business.gov.au, "Copyright" <https://business.gov.au/planning/protect-your-brand-idea-or-creation/copyright>
[^auipa]: IP Australia, "Beware of unofficial invoices, correspondence and registers" <https://www.ipaustralia.gov.au/about-us/doing-business-with-us/fraud-and-corruption/beware-of-unofficial-invoices-correspondence-and-registers>
[^ausa]: Legal Services Commission of South Australia, Law Handbook, Copyright chapter (questions and answers) <https://lawhandbook.sa.gov.au/ch11s13.php>
