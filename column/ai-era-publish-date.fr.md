title: Votre date de publication est déclarative : garder une date que personne ne peut réécrire à l'ère de l'IA
description: Réécrire prend des secondes et la date du CMS ne prouve rien. Comment dater chaque article par un tiers, automatiquement sur WordPress, et avec quelles limites.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Imaginez : le lendemain de votre publication, une quasi-copie apparaît. Paragraphes réordonnés, tournures changées, même ossature. Comment montreriez-vous que la vôtre était la première ?

## Réécrire ne coûte presque plus rien

Paraphraser, restructurer, traduire demandait du temps humain. Un modèle de langage le fait aujourd'hui en un instant. Les chiffres montrent à quel point les contenus écrits et lus par des machines sont déjà courants.

| Source | Constat |
|---|---|
| Imperva, 2025 Bad Bot Report | 51 % du trafic web en 2024 était automatisé ; les robots malveillants en représentaient 37 %, contre 32 % auparavant[^imperva] |
| Cloudflare, juillet 2025 | Les requêtes de GPTBot sur son réseau ont augmenté de 305 % entre mai 2024 et mai 2025[^cf1] |
| Cloudflare, août 2025 | Environ 80 % de l'exploration par des IA sur l'année écoulée servait à l'entraînement de modèles[^cf2] |
| NewsGuard | Sites d'information publiant des contenus générés par IA avec peu de contrôle humain : 49 en mai 2023, 3 749 en juin 2026[^newsguard] |
| Ahrefs, mai 2025 | 74,2 % de 900 000 pages publiées pour la première fois en avril 2025 contenaient du contenu généré par IA[^ahrefs] |
| Article NeurIPS 2023 | Un modèle de paraphrase a fait chuter la précision d'un détecteur de texte IA de 70,3 % à 4,6 %[^neurips] |

Ce sont des estimations d'entreprises ou de chercheurs, chacune avec sa méthode, et aucune n'est la probabilité que *votre* article soit copié. Elles montrent en revanche que la réécriture est facile et difficile à détecter.

## Votre date de publication est déclarative

C'est vous qui choisissez votre date de publication. WordPress permet de publier avec une date passée et de changer la date d'un article en ligne.[^wp] La date affichée par l'autre site est tout aussi déclarative : deux personnes qui disent « j'étais le premier » ne tranchent rien. Les archives du web aident, mais vous ne décidez pas si ni quand elles capturent votre page.

En France, le droit d'auteur naît du seul fait de la création, sans dépôt.[^cpi] Il n'y a donc pas de date officielle par défaut : c'est à vous de prouver quand votre texte existait. Il vous faut **quelqu'un d'autre que vous** pour noter la date **au moment où vous publiez**, à un endroit que **personne ne puisse réécrire ensuite**.

## Ce que fait DateSealed

- Il ne reçoit que l'**empreinte SHA-256** de votre article, calculée dans votre navigateur (ou sur votre propre serveur avec l'extension WordPress). Le texte n'est jamais envoyé.
- Il y joint un **horodatage RFC 3161**, renvoyé immédiatement, et un **enregistrement Bitcoin** via OpenTimestamps, ancré en quelques heures.
- Personne ne peut inscrire une heure après coup dans le registre Bitcoin. Une fois l'ancrage fait, la date se vérifie avec le fichier de preuve et le registre seuls, même si DateSealed disparaît.

Pour aller plus loin : « [Comment montrer que vous l'avez créé en premier](/fr/column/prove-you-made-it-first) » et « [Pourquoi j'ai créé DateSealed](/fr/column/why-i-built-datesealed) ».

## Automatique sur WordPress

Une habitude qu'il faut se rappeler ne résiste pas à une semaine chargée. L'extension WordPress de DateSealed :

- calcule sur votre serveur l'empreinte du texte à chaque publication et mise à jour, et n'envoie que l'empreinte ;
- **ajoute un nouvel enregistrement** à chaque mise à jour : la première publication n'est jamais écrasée et l'historique des versions s'accumule ;
- peut afficher un badge renvoyant vers la page d'enregistrement (facultatif) ;
- nécessite WordPress 5.8 ou plus et PHP 8.2 ou plus.

[Téléchargez-la sur la page de l'API](/api#wordpress), puis dans WordPress, allez dans *Extensions → Ajouter → Téléverser une extension* (*Plugins → Add New → Upload Plugin*), téléversez le fichier ZIP, activez l'extension et ouvrez *Réglages → DateSealed* (*Settings → DateSealed*). Sa publication sur wordpress.org est en cours d'examen.

## Ce que l'enregistrement ne dit pas

- Il ne dit pas si le texte a été écrit par un humain ou par un modèle.
- Il ne dit pas que le contenu est exact ou original, qui l'a écrit ni à qui il appartient.
- Il **ne garantit aucun effet juridique**. Dans l'Union européenne, la présomption d'exactitude de la date et de l'heure est réservée aux horodatages électroniques qualifiés au sens du règlement eIDAS.[^eidas] Un enregistrement DateSealed n'en est pas un.

« Cela existait à ce moment-là » est un bon point de départ pour une discussion. Cela ne la tranche pas à lui seul. Servez-vous de l'enregistrement comme d'une pièce parmi les autres.

## Les habitudes qui donnent de la valeur à l'enregistrement

1. **Gardez l'original.** DateSealed ne conserve que des empreintes.
2. **Gardez les fichiers de preuve.** Rangez le `.tsr` et le `.ots` avec l'original pour pouvoir vérifier sans DateSealed.
3. **Enregistrez au moment de publier.** L'heure de l'enregistrement est celle où vous le faites ; chaque jour de retard l'affaiblit.
4. **N'en attendez pas trop.** Pour un enjeu réel, ajoutez une e-Soleau de l'INPI,[^inpi] un constat de commissaire de justice ou un horodatage qualifié.

[^imperva]: Imperva, « 2025 Imperva Bad Bot Report » (15 avril 2025 ; données du réseau Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog de Cloudflare (1er juillet 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog de Cloudflare (29 août 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, « AI Tracking Center » <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, « What Percentage of New Content Is AI-Generated? » (19 mai 2025 ; détecteur propre à Ahrefs, qu'elle reconnaît imparfait) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., « Paraphrasing evades detectors of AI-generated text », NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, « Write Posts (Classic Editor) » <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^cpi]: Code de la propriété intellectuelle, article L111-1 (Légifrance) <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278868>
[^eidas]: Règlement (UE) n° 910/2014 (eIDAS), article 41, paragraphe 2 <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32014R0910> ; texte anglais de l'article : <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
[^inpi]: INPI, « e-Soleau : protégez votre création » <https://www.inpi.fr/realiser-demarches/propriete-intellectuelle/deposer-une-e-soleau-ou-un-entiercement>
