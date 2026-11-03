title: Why I Built DateSealed: A Note from the Developer
description: It started with wanting to protect property photos from tampering and copying. Here is what I found when I looked at existing options, and the rules I set for a free record that takes nothing from you and that even I cannot rewrite.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed is a free tool that records when a piece of text, a photo or a web page existed. I am Yuki Nakazawa, and I built it. This note is about why, and about the decisions I made along the way.

## It started with property photos

I run a real-estate company in Japan, and we photograph and publish our listings. I wanted to be ready for the day someone altered one of those photos or posted it on another site, so that I could show the original was ours and existed first.

I had the original files, and my posts had publish dates. But I could edit every one of those myself, and anyone holding a copy could claim the same dates. What I needed was a date written down by **someone other than me**, in a form **nobody could change afterwards**.

## What I found first

I looked at what was available in Japan as of November 2026.

- **A notary's certified date.** 700 yen per document. There is an electronic version, but it accepts only text, PDF and XML files up to 10 MB, and the procedure runs on weekdays.
- **Registration with the Agency for Cultural Affairs.** 3,000 yen per work, filed on paper, one work at a time. It creates a presumption that the work was published on the registered date.
- **Time stamps from providers accredited by the Ministry of Internal Affairs and Communications.** These are the ones with an official status in Japan. Pricing is mostly aimed at companies.
- **Blockchain-based record services.** The ones I found were for businesses, or paid.
- **In-camera signatures (C2PA).** Some cameras sign photos as they are taken. That tells you where a file came from, which is a different question from when it existed.

All of these are useful, and for the one thing you really need to protect, you should use them. But paying and filing for every new photo or article is not realistic. What I wanted was **free, with no sign-up, uploading nothing, kept somewhere even the operator cannot rewrite, and automatic on WordPress every time you publish**. I could not find it, so I built it.

## The rules I set

### Take nothing but a hash

DateSealed receives only the SHA-256 hash of your file or text, a 64-character fingerprint. The hash is computed in your browser, so your photos and drafts never leave your computer. Unpublished work is exactly what people want to record, and handing it over to get it recorded would defeat the point.

### You should not have to trust me

Each record gets two dates. One is an RFC 3161 time stamp signed by DateSealed's own time-stamping authority, returned immediately. The other is anchored in a Bitcoin block through OpenTimestamps, usually within hours.

The first is only as trustworthy as I am. The second is not mine to change. Once it is anchored, you can check the date with the proof file (`.ots`) and the Bitcoin ledger alone, even if DateSealed disappears. Every record page lists the commands to verify it on your own machine.

The root key of the time-stamping authority was created on my own computer and is kept encrypted with a passphrase. The server holds only the signing key.

### Never delete, never rewrite

Even the admin screens have no way to delete a record or change its hash or time. A ledger is worth something only if its operator cannot touch it. When you update a post, the old record stays and a new one is added. The WordPress plugin follows the same rule.

### Say what it cannot do, up front

A record shows that data matching the hash existed at that time. Nothing more. It does not show that you made it, that you own it, or that it is accurate, and it does **not guarantee legal effect**. I say this in many places on the site, because the wrong expectation is how people get hurt.

### Be plain about what is collected

To prevent abuse, enforce limits, debug and understand usage, each use is logged with the IP address and a few other details. It is not used for advertising and not sold. IP addresses and host names stay on this server for 30 days, then move to separate storage I manage for up to 13 months, after which the end of the address is removed and only statistics remain. The details are in the [terms](/terms).

## For anyone

It is free and needs no account. The interface is available in 20 languages. There is also a stamp for photos, a way to record a published URL, an API and a WordPress plugin. You can [download the plugin from the API page](/api#wordpress); a listing on wordpress.org is under review. For a step-by-step guide, and how a record fits next to US copyright registration and the evidence habits suggested in the UK and Australia, see "[How to show you made it first](/column/prove-you-made-it-first)".

## Tell me what breaks

I would like to hear where DateSealed gets in your way and what you would like it to do next, especially from photographers and bloggers who have been in a "who was first" dispute. Contact details are at the bottom of the page.
