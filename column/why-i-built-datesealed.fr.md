title: Pourquoi j'ai créé DateSealed : le mot du développeur
description: Tout est parti de photos immobilières. Ce que j'ai trouvé parmi les solutions existantes, et les règles d'une preuve gratuite que même moi je ne peux réécrire.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed est un outil gratuit qui enregistre à quel moment un texte, une photo ou une page web existait. Je m'appelle Yuki Nakazawa et c'est moi qui l'ai conçu. Ce texte explique pourquoi, et quels choix j'ai faits en chemin.

## Au départ, des photos de biens immobiliers

Je dirige une agence immobilière au Japon. Nous photographions nos biens et publions ces images. Je voulais être prêt le jour où quelqu'un retoucherait l'une de ces photos ou la reprendrait sur un autre site, pour pouvoir montrer que l'original était le nôtre et qu'il existait avant.

J'avais les fichiers originaux, et mes publications portaient une date. Mais je pouvais modifier tout cela moi-même, et quiconque détient une copie peut revendiquer les mêmes dates. Il me fallait une date notée par **quelqu'un d'autre que moi**, sous une forme que **personne ne puisse modifier ensuite**.

## Ce que j'ai trouvé d'abord

J'ai regardé ce qui existait au Japon en novembre 2026 :

- **La date certaine d'un notaire.** 700 yens par document. Il existe une version électronique, mais elle n'accepte que des fichiers texte, PDF et XML de 10 Mo au plus, et la procédure ne fonctionne que les jours ouvrés.
- **L'enregistrement auprès de l'Agence japonaise des affaires culturelles.** 3 000 yens par œuvre, sur papier, une œuvre à la fois. Il fait présumer que l'œuvre a été publiée à la date enregistrée.
- **Les horodatages de prestataires accrédités par le ministère japonais des Affaires intérieures et des Communications.** Ce sont eux qui ont un statut officiel au Japon. Leurs tarifs visent surtout les entreprises.
- **Les services de preuve sur blockchain.** Ceux que j'ai trouvés s'adressaient aux entreprises ou étaient payants.
- **Les signatures dans l'appareil photo (C2PA).** Certains boîtiers signent les photos à la prise de vue. Cela renseigne sur l'origine d'un fichier, ce qui est une autre question que celle de sa date d'existence.

Tout cela est utile, et pour la chose que vous devez vraiment protéger, il faut s'en servir. Mais payer et déposer un dossier pour chaque nouvelle photo ou chaque article n'est pas réaliste. Je voulais un service **gratuit, sans inscription, qui ne reçoive aucun fichier, conservé là où même l'exploitant ne peut rien réécrire, et automatique sur WordPress à chaque publication**. Je ne l'ai pas trouvé, alors je l'ai construit.

## Les règles que je me suis fixées

### Ne recevoir qu'une empreinte

DateSealed ne reçoit que l'empreinte SHA-256 de votre fichier ou de votre texte, une suite de 64 caractères. Elle est calculée dans votre navigateur : vos photos et vos brouillons ne quittent pas votre ordinateur. Ce sont justement les travaux non publiés que l'on veut dater ; devoir les confier à un tiers pour cela n'aurait pas de sens.

### Vous ne devriez pas avoir à me faire confiance

Chaque enregistrement reçoit deux dates. La première est un horodatage RFC 3161 signé par l'autorité d'horodatage propre à DateSealed, renvoyé immédiatement. La seconde est ancrée dans un bloc Bitcoin via OpenTimestamps, en général en quelques heures.

La première ne vaut que la confiance que vous m'accordez. La seconde ne dépend pas de moi. Une fois l'ancrage fait, la date se vérifie avec le seul fichier de preuve (`.ots`) et le registre Bitcoin, même si DateSealed disparaît. Chaque page d'enregistrement indique les commandes pour le vérifier sur votre propre machine.

La clé racine de l'autorité d'horodatage a été créée sur mon propre ordinateur et y est conservée chiffrée par une phrase secrète. Le serveur ne détient que la clé de signature.

### Ne jamais effacer, ne jamais réécrire

Même l'interface d'administration ne permet ni de supprimer un enregistrement ni de modifier son empreinte ou son heure. Un registre n'a de valeur que si son exploitant ne peut pas y toucher. Quand vous mettez à jour un article, l'ancien enregistrement reste et un nouveau s'ajoute. L'extension WordPress suit la même règle.

### Dire d'emblée ce qu'il ne fait pas

Un enregistrement montre que des données correspondant à l'empreinte existaient à ce moment-là. Rien de plus. Il ne montre pas que vous en êtes l'auteur, que vous en êtes titulaire, ni que le contenu est exact, et il **ne garantit aucun effet juridique**. Je le répète à de nombreux endroits du site, parce que c'est une attente erronée qui fait le plus de dégâts.

### Être clair sur ce qui est collecté

Pour prévenir les abus, appliquer les limites, corriger les erreurs et comprendre l'usage, chaque utilisation est journalisée avec l'adresse IP et quelques autres informations. Elles ne servent pas à la publicité et ne sont pas vendues. Les adresses IP et les noms d'hôte restent 30 jours sur ce serveur, puis sont déplacés vers un stockage séparé que je gère, pour 13 mois au plus ; ensuite la fin de l'adresse est supprimée et il ne reste que des statistiques. Les détails figurent dans les [conditions d'utilisation](/fr/terms).

## Pour tout le monde

C'est gratuit et sans compte. L'interface existe en 20 langues. Il y a aussi un tampon pour les photos, un moyen d'enregistrer une URL publiée, une API et une extension WordPress. Vous pouvez [télécharger l'extension sur la page de l'API](/api#wordpress) ; sa publication sur wordpress.org est en cours d'examen.

Pour la marche à suivre pas à pas, et les dispositifs qui existent en France, voir « [Comment montrer que vous l'avez créé en premier](/fr/column/prove-you-made-it-first) ».

## Dites-moi ce qui coince

J'aimerais savoir où DateSealed vous gêne et ce que vous aimeriez qu'il fasse ensuite, en particulier si vous êtes photographe ou blogueur et avez déjà connu un litige sur la question de savoir qui était le premier. Les coordonnées sont en bas de page.
