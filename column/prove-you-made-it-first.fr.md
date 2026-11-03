title: Comment montrer que vous l'avez créé en premier : une date tierce pour vos photos et brouillons
description: Vos propres dates se modifient. Comment dater gratuitement une photo ou un brouillon sans rien envoyer, ce que cela prouve, et les autres voies en France.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Si quelqu'un copie votre travail, pourrez-vous montrer que le vôtre existait avant ? Ce guide explique comment vous y préparer, gratuitement et sans montrer votre travail à qui que ce soit.

## En France, le droit d'auteur naît sans formalité

L'auteur d'une œuvre de l'esprit en a la propriété « du seul fait de sa création » (article L111-1 du Code de la propriété intellectuelle).[^cpi] Aucun dépôt n'est nécessaire pour être protégé.

C'est pratique, mais cela laisse une question ouverte en cas de litige : il faut pouvoir prouver **à quelle date** votre œuvre existait. C'est pour cela que des dispositifs de preuve existent à côté du droit lui-même.

## Toutes les dates que vous détenez peuvent être modifiées

La difficulté des preuves de date est simple : ce que vous pouvez modifier vous-même, la partie adverse peut dire que vous l'avez modifié.

| La date dont vous disposez | Pourquoi elle est fragile |
|---|---|
| Date de publication du CMS | On peut choisir une date passée. WordPress explique comment.[^wp] |
| Métadonnées de la photo (Exif) | Des outils gratuits comme ExifTool les modifient, y compris par lots.[^exif] |
| Dates des fichiers | Sous Windows, un fichier copié reçoit une nouvelle date de création (la date de modification est conservée).[^kb] |
| Captures d'écran | Elles se retouchent comme n'importe quelle image. |

Chacune vaut mieux que rien, mais aucune ne répond à l'objection « n'auriez-vous pas pu fabriquer cela après coup ? ». Il vous faut une date notée par **quelqu'un d'autre que vous**, sous une forme que **personne ne puisse réécrire ensuite**.

## Enregistrer avec DateSealed

1. Ouvrez la [page d'accueil](/fr/) et collez un texte ou choisissez un fichier. Vous pouvez aussi saisir une URL ou une empreinte SHA-256 que vous avez déjà.
2. Vérifiez l'empreinte SHA-256 affichée et cliquez sur le bouton pour l'enregistrer. Elle est calculée dans votre navigateur : le fichier ou le texte n'est jamais envoyé.
3. La page d'enregistrement s'ouvre. Téléchargez le `.tsr` (horodatage signé) et le `.ots` (preuve Bitcoin) et conservez-les **avec le fichier original**.

Chaque enregistrement reçoit deux dates : un horodatage RFC 3161 renvoyé immédiatement, et un enregistrement OpenTimestamps ancré dans un bloc Bitcoin en quelques heures. Une fois l'ancrage fait, la date se vérifie avec le seul registre Bitcoin, même si DateSealed ferme. La page d'enregistrement indique les commandes pour le vérifier sur votre propre machine.

La limite est de 10 enregistrements par heure et 50 par jour pour une même adresse IP.

## Vous publiez des photos ? Utilisez le tampon

[Tamponner une photo](/fr/stamp) enregistre l'empreinte de votre original puis crée, dans votre navigateur, une copie portant un petit badge avec la date de l'enregistrement et l'adresse de sa page. La photo elle-même n'est pas envoyée.

L'enregistrement porte sur **l'original**. La copie tamponnée est un autre fichier, et le badge peut être recadré ; à lui seul, il ne prouve rien. Publiez la copie tamponnée et gardez l'original en lieu sûr.

## Ce qu'un enregistrement montre, et ce qu'il ne montre pas

Il montre que **des données correspondant à cette empreinte existaient au moment enregistré**. C'est tout.

- Il ne montre pas que le contenu est exact ou original.
- Il ne montre pas que vous en êtes l'auteur ou le titulaire. L'enregistrement ne dit pas qui a créé l'œuvre.
- Il **ne garantit aucun effet juridique**. Selon le règlement européen eIDAS, un horodatage électronique **qualifié** bénéficie d'une présomption d'exactitude de la date et de l'heure, et d'intégrité des données.[^eidas] Un enregistrement DateSealed n'est pas un horodatage qualifié.

## Pour la chose que vous devez vraiment protéger

Utilisez aussi les voies formelles :

| Moyen | Ce qu'il apporte |
|---|---|
| e-Soleau de l'INPI | Une preuve de création à une date précise. À partir de 15 € pour un dépôt jusqu'à 50 Mo, conservé 5 ans, prorogeable (tarif indiqué par l'INPI sur une page publiée le 14 janvier 2025).[^inpi] |
| Constat de commissaire de justice | Des constatations purement matérielles qui, hors matière pénale, font foi jusqu'à preuve contraire.[^cj] |
| Horodatage électronique qualifié | La présomption prévue par eIDAS, quand vous en avez besoin. |
| DateSealed | Gratuit : une première date pour le flux continu de photos, d'articles et de brouillons. |

Ailleurs dans la francophonie : en Belgique, l'Office Benelux de la propriété intellectuelle propose l'i-DEPOT, un moyen de prouver qu'une idée existait à une date donnée ;[^idepot] en Suisse, le droit d'auteur naît aussi automatiquement et il n'existe pas de registre ;[^ige] au Canada, l'OPIC tient un registre, et le certificat d'enregistrement fait preuve de l'existence du droit et de son titulaire,[^lda] pour 63 $ en ligne.[^cipo]

DateSealed est la première couche, rapide et gratuite : une pièce de plus à placer à côté des autres.

## Deux choses à retenir

- **Gardez l'original.** DateSealed ne conserve que l'empreinte. Sans le fichier original, l'enregistrement ne se rattache à rien.
- **Enregistrez à nouveau après chaque modification.** Un seul caractère changé et l'empreinte change. Sur WordPress, [l'extension](/api#wordpress) enregistre chaque publication et chaque mise à jour pour vous.

[^cpi]: Code de la propriété intellectuelle, article L111-1 (Légifrance) <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278868>
[^wp]: WordPress.org, « Write Posts (Classic Editor) » <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Base de connaissances Microsoft, article KB299648 (traitement des dates lors de la copie ou du déplacement de fichiers)
[^eidas]: Règlement (UE) n° 910/2014 (eIDAS), article 41, paragraphe 2 <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32014R0910> ; texte anglais de l'article : <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
[^inpi]: INPI, « e-Soleau : protégez votre création » <https://www.inpi.fr/realiser-demarches/propriete-intellectuelle/deposer-une-e-soleau-ou-un-entiercement>
[^cj]: Ordonnance n° 2016-728 du 2 juin 2016 relative au statut de commissaire de justice, article 1er (Légifrance) <https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032624483>
[^idepot]: Ondernemersplein (portail public néerlandais), « Uw idee vastleggen » (en néerlandais) <https://ondernemersplein.overheid.nl/uw-idee-vastleggen/>
[^ige]: Institut Fédéral de la Propriété Intellectuelle, « Urheberrecht » (en allemand) <https://www.ige.ch/de/etwas-schuetzen/urheberrecht>
[^lda]: Loi sur le droit d'auteur (Canada), paragraphe 53(2) <https://laws-lois.justice.gc.ca/fra/lois/c-42/page-16.html>
[^cipo]: Règlement sur le droit d'auteur (Canada), annexe, article 1 (version à jour au 19 octobre 2026) <https://laws-lois.justice.gc.ca/eng/regulations/SOR-97-457/page-2.html>
