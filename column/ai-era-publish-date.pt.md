title: A data de publicação é autodeclarada: como guardar uma data que ninguém reescreve na era da IA
description: Reescrever um artigo leva segundos, e a data do CMS não prova nada. Como ter uma data de terceiros em cada post, inclusive no WordPress, e quais são os limites.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Imagine que, na manhã seguinte à publicação, aparece uma quase cópia: parágrafos em outra ordem, frases trocadas, o mesmo esqueleto. Como você mostraria que o seu veio primeiro?

## Reescrever ficou barato

Parafrasear, reorganizar e traduzir antes exigiam tempo de uma pessoa. Hoje um modelo de linguagem faz isso em instantes. Os números mostram como o conteúdo escrito e lido por máquinas já é comum.

| Fonte | Dado |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% do tráfego da web em 2024 foi automatizado; bots maliciosos foram 37%, contra 32% antes[^imperva] |
| Cloudflare, julho de 2025 | As requisições do GPTBot em sua rede cresceram 305% de maio de 2024 a maio de 2025[^cf1] |
| Cloudflare, agosto de 2025 | Cerca de 80% do rastreamento por IA no ano anterior foi para treinar modelos[^cf2] |
| NewsGuard | Sites de notícias que publicam conteúdo gerado por IA com pouca supervisão humana: 49 em maio de 2023, 3.749 em junho de 2026[^newsguard] |
| Ahrefs, maio de 2025 | 74,2% de 900 mil páginas publicadas pela primeira vez em abril de 2025 tinham algum conteúdo gerado por IA[^ahrefs] |
| Artigo do NeurIPS 2023 | Um modelo de paráfrase derrubou a precisão de um detector de texto de IA de 70,3% para 4,6%[^neurips] |

São estimativas de empresas ou pesquisadores, cada uma com seu método, e nenhuma é a chance de o *seu* post ser copiado. Mas elas mostram que reescrever é fácil e difícil de detectar.

## A data de publicação é autodeclarada

Quem escolhe a data de publicação é você. O WordPress permite publicar com data passada e mudar a data de um post já no ar.[^wp] A data do outro site é tão autodeclarada quanto a sua, então duas pessoas dizendo "eu fui primeiro" não resolvem nada. Arquivos da web ajudam, mas você não controla se nem quando eles capturam a sua página.

O que você precisa é que **alguém que não seja você** anote a data **no momento da publicação**, em um lugar que **ninguém consiga reescrever depois**.

## O que o DateSealed faz

- Recebe apenas o **hash SHA-256** do seu post, calculado no seu navegador (ou no seu próprio servidor, com o plugin para WordPress). O texto nunca é enviado.
- Associa a ele um **carimbo do tempo RFC 3161**, devolvido na hora, e um **registro no Bitcoin** via OpenTimestamps, ancorado em poucas horas.
- Ninguém consegue gravar um horário no livro-razão do Bitcoin depois do fato. Depois de ancorada, a data pode ser conferida só com o arquivo de prova e o livro-razão, mesmo que o DateSealed deixe de existir.

Mais detalhes em "[Como mostrar que você fez primeiro](/pt/column/prove-you-made-it-first)" e "[Por que criei o DateSealed](/pt/column/why-i-built-datesealed)".

## Automático no WordPress

Um hábito que depende de memória não sobrevive a uma semana corrida. O plugin do DateSealed para WordPress:

- calcula no seu servidor o hash do texto a cada publicação e atualização, e envia só o hash;
- **acrescenta um novo registro** a cada atualização, então a primeira publicação nunca é sobrescrita e o histórico de revisões vai se acumulando;
- pode exibir um selo com link para a página do registro (opcional);
- exige WordPress 5.8 ou superior e PHP 8.2 ou superior.

[Baixe na página da API](/api#wordpress); depois, no WordPress, vá em *Plugins → Add New → Upload Plugin*, ative e abra *Settings → DateSealed* (em um WordPress em português, esses menus aparecem traduzidos). A publicação no wordpress.org está em análise.

## O que o registro não diz

- Não mostra se o texto foi escrito por uma pessoa ou por um modelo.
- Não mostra que o conteúdo é correto ou original, quem o escreveu nem quem é o titular.
- **Não garante efeito jurídico.** No Brasil, existe o carimbo do tempo da ICP-Brasil, emitido por uma Autoridade de Carimbo do Tempo segundo normas aprovadas pelo Comitê Gestor da ICP-Brasil;[^iti] na União Europeia, incluindo Portugal, a presunção legal fica com os selos temporais qualificados do eIDAS.[^eidas] O DateSealed não é nenhum dos dois.

"Existia neste momento" é um bom ponto de partida para uma conversa, mas não a encerra sozinho. Use o registro como mais uma prova, ao lado das outras.

## Hábitos que dão valor ao registro

1. **Guarde o original.** O DateSealed guarda só hashes.
2. **Guarde os arquivos de prova.** Mantenha o `.tsr` e o `.ots` junto do original para verificar sem depender do DateSealed.
3. **Registre na hora de publicar.** O horário do registro é o momento em que você o fez; cada dia de atraso o enfraquece.
4. **Não exagere no que ele prova.** Num caso que importa, some o registro na Biblioteca Nacional ou um carimbo do tempo ICP-Brasil.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (15 de abril de 2025; dados da rede da Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog da Cloudflare (1º de julho de 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog da Cloudflare (29 de agosto de 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (19 de maio de 2025; com o detector da própria empresa, que ela admite ser imperfeito) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^iti]: Instituto Nacional de Tecnologia da Informação (ITI), perguntas frequentes, "Carimbo do Tempo" <https://www.gov.br/iti/pt-br/acesso-a-informacao/perguntas-frequentes/carimbo-do-tempo>
[^eidas]: Regulamento (UE) n.º 910/2014 (eIDAS), artigo 41.º, n.º 2 (texto em inglês, como mantido na legislação do Reino Unido) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
