title: Como mostrar que você fez primeiro: uma data de terceiros para suas fotos e rascunhos
description: Toda data que fica com você pode ser editada. Como registrar, de graça e sem enviar nada, que uma foto ou um rascunho existiam em certo dia, e o que isso prova.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Se alguém copiar o seu trabalho, você consegue mostrar que o seu veio antes? Este guia explica como se preparar para esse momento, de graça e sem mostrar a obra para ninguém.

## Toda data que você tem pode ser editada

O problema das datas como prova é simples: tudo o que você mesmo pode mudar, a outra parte pode dizer que você mudou.

| A data que você tem | Por que é fraca |
|---|---|
| Data de publicação no CMS | Dá para escolher uma data passada. O WordPress explica como.[^wp] |
| Metadados da foto (Exif) | Ferramentas gratuitas como o ExifTool editam esses dados e até deslocam datas em lote.[^exif] |
| Datas do arquivo | No Windows, um arquivo copiado ganha uma nova data de criação (a de modificação é mantida).[^kb] |
| Capturas de tela | Podem ser editadas como qualquer imagem. |

Cada uma é melhor do que nada, mas nenhuma responde à pergunta "você não poderia ter montado isso depois?". O que você precisa é de uma data anotada por **alguém que não seja você**, de um jeito que **ninguém consiga reescrever depois**.

## Como registrar no DateSealed

1. Abra a [página inicial](/pt/) e cole um texto ou escolha um arquivo. Você também pode informar uma URL ou um SHA-256 que já tenha.
2. Confira o SHA-256 exibido e clique em "Registrar agora". O hash é calculado no seu navegador, então o arquivo ou o texto nunca são enviados.
3. A página do registro se abre. Baixe o `.tsr` (carimbo do tempo assinado) e o `.ots` (prova no Bitcoin) e guarde-os **junto com o arquivo original**.

Cada registro recebe duas datas: um carimbo do tempo RFC 3161, devolvido na hora, e um registro do OpenTimestamps, ancorado em um bloco do Bitcoin em poucas horas. Depois de ancorada, a data pode ser conferida só com o livro-razão do Bitcoin, mesmo que o DateSealed saia do ar. A página do registro traz os comandos para verificar no seu próprio computador.

O limite é de 10 registros por hora e 50 por dia por endereço IP.

## Vai publicar fotos? Use o carimbo

[Carimbar fotos](/pt/stamp) registra o hash do seu original e depois, no seu navegador, cria uma cópia com um pequeno selo que mostra a data do registro e o endereço da página do registro. A foto não é enviada.

O registro se refere **ao original**. A cópia carimbada é outro arquivo, e o selo pode ser cortado; sozinho, ele não prova nada. Publique a cópia carimbada e guarde bem o original.

## O que um registro mostra, e o que não mostra

Ele mostra que **dados correspondentes a este hash existiam no momento registrado**. Só isso.

- Não mostra que o conteúdo é correto ou original.
- Não mostra que foi você quem criou nem que você é o titular. O registro não diz quem é o autor.
- **Não garante efeito jurídico.** No Brasil, o carimbo do tempo da ICP-Brasil é emitido por uma terceira parte confiável, a Autoridade de Carimbo do Tempo (ACT), e serve para comprovar que uma informação digital existia em determinada data e hora.[^iti] Em Portugal, como em toda a União Europeia, vale o regulamento eIDAS: os selos temporais qualificados gozam de presunção de exatidão da data e da hora e de integridade dos dados.[^eidas] Um registro do DateSealed usa o formato técnico RFC 3161, mas não é um carimbo da ICP-Brasil nem um selo temporal qualificado.

## Para aquilo que você realmente precisa proteger

No Brasil, a proteção do direito autoral "independe de registro" (art. 18 da Lei 9.610/1998), e o autor tem a faculdade de registrar a obra (art. 19).[^lda] O Ministério da Cultura resume: o registro é facultativo e meramente declaratório, e serve como documento que ajuda a provar a autoria se for preciso.[^minc]

| Via | Custo | Para que serve |
|---|---|---|
| Registro no Escritório de Direitos Autorais (EDA) da Biblioteca Nacional | R$ 40,00 para pessoa física e R$ 80,00 para pessoa jurídica; pedido pelo gov.br, com prazo estimado de até 90 dias (página do serviço atualizada em 16/09/2026)[^eda] | Documento oficial com os dados declarados da obra; o EDA guarda uma cópia |
| Carimbo do tempo ICP-Brasil | Conforme o fornecedor | Documentos eletrônicos que precisam do padrão ICP-Brasil |
| DateSealed | Gratuito | Pôr data, logo de saída, no fluxo constante de fotos, artigos e rascunhos |

O registro é feito de forma descentralizada: dependendo da categoria da obra, a instituição responsável pode ser outra.[^minc] O DateSealed é uma primeira camada rápida e gratuita: mais uma prova para colocar ao lado das outras.

## Duas coisas para lembrar

- **Guarde o original.** O DateSealed tem só o hash. Sem o arquivo original, o registro não se liga a nada.
- **Registre de novo a cada alteração.** Mudou um caractere, mudou o hash. No WordPress, [o plugin](/api#wordpress) registra cada publicação e cada atualização para você.

[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Artigo KB299648 da Microsoft Knowledge Base (como as datas são tratadas ao copiar ou mover arquivos)
[^iti]: Instituto Nacional de Tecnologia da Informação (ITI), perguntas frequentes, "Carimbo do Tempo" <https://www.gov.br/iti/pt-br/acesso-a-informacao/perguntas-frequentes/carimbo-do-tempo>
[^eidas]: Regulamento (UE) n.º 910/2014 (eIDAS), artigo 41.º, n.º 2 (texto em inglês, como mantido na legislação do Reino Unido) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
[^lda]: Lei n.º 9.610, de 19 de fevereiro de 1998, arts. 18 e 19 (Câmara dos Deputados) <https://www2.camara.leg.br/legin/fed/lei/1998/lei-9610-19-fevereiro-1998-365399-publicacaooriginal-1-pl.html>
[^minc]: Ministério da Cultura, "Perguntas Frequentes" sobre direitos autorais <https://www.gov.br/cultura/pt-br/assuntos/direitos-autorais/perguntas-frequentes/perguntas-frequentes>
[^eda]: gov.br, "Registrar ou Averbar Direitos Autorais na Biblioteca Nacional" <https://www.gov.br/pt-br/servicos/registrar-ou-averbar-direitos-autorais-na-biblioteca-nacional>
