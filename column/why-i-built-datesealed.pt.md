title: Por que criei o DateSealed: um recado do desenvolvedor
description: Começou com fotos de imóveis que eu queria proteger de cópias. O que encontrei nas opções existentes e as regras de um registro grátis que nem eu posso reescrever.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
O DateSealed é uma ferramenta gratuita que registra quando um texto, uma foto ou uma página da web existiam. Eu sou Yuki Nakazawa e fui eu que o desenvolvi. Este texto conta por quê, e quais decisões tomei no caminho.

## Começou com fotos de imóveis

Tenho uma imobiliária no Japão; fotografamos os imóveis e publicamos os anúncios. Eu queria estar preparado para o dia em que alguém alterasse uma dessas fotos ou a publicasse em outro site, e poder mostrar que o original era nosso e existia antes.

Eu tinha os arquivos originais, e as publicações tinham data. Mas eu mesmo podia mudar todas essas datas, e qualquer pessoa com uma cópia podia alegar as mesmas. O que eu precisava era de uma data anotada por **alguém que não fosse eu**, de um jeito que **ninguém pudesse alterar depois**.

## O que encontrei primeiro

Pesquisei o que havia no Japão em novembro de 2026:

- **Data certificada por um notário.** 700 ienes por documento. Existe uma versão eletrônica, mas ela aceita só arquivos de texto, PDF e XML de até 10 MB, e funciona em dias úteis.
- **Registro na Agência de Assuntos Culturais.** 3.000 ienes por obra, em papel e uma de cada vez. Gera a presunção de que a obra foi publicada na data registrada.
- **Carimbos do tempo de provedores credenciados pelo Ministério de Assuntos Internos e Comunicações.** São os que têm reconhecimento oficial no Japão, com preços voltados principalmente para empresas.
- **Serviços de registro em blockchain.** Os que encontrei eram para empresas ou pagos.
- **Assinatura na própria câmera (C2PA).** Algumas câmeras assinam a foto no momento do clique. Isso diz de onde veio um arquivo, que é uma pergunta diferente de quando ele existia.

Tudo isso é útil e, para aquilo que você realmente precisa proteger, vale a pena usar. Mas pagar e fazer um pedido para cada foto ou artigo novo não é realista. Eu queria algo **gratuito, sem cadastro, sem enviar nada, guardado onde nem o operador consiga reescrever e automático no WordPress a cada publicação**. Não encontrei, então construí.

## As regras que defini

### Receber só um hash

O DateSealed recebe apenas o hash SHA-256 do seu arquivo ou texto, uma impressão digital de 64 caracteres. O hash é calculado no seu navegador, então suas fotos e rascunhos não saem do seu computador. O que as pessoas querem registrar é justamente o que ainda não publicaram, e ter de entregar isso para registrar não faria sentido.

### Você não deveria precisar confiar em mim

Cada registro recebe duas datas. Uma é um carimbo do tempo RFC 3161 assinado pela autoridade de carimbo do tempo do próprio DateSealed, devolvido na hora. A outra é ancorada em um bloco do Bitcoin por meio do OpenTimestamps, normalmente em poucas horas.

A primeira vale o quanto vale a minha palavra. A segunda não depende de mim. Depois de ancorada, você pode conferir a data só com o arquivo de prova (`.ots`) e o livro-razão do Bitcoin, mesmo que o DateSealed deixe de existir. Cada página de registro traz os comandos para verificar no seu próprio computador.

A chave raiz da autoridade de carimbo do tempo foi criada no meu próprio computador e é guardada criptografada com uma frase-senha. O servidor tem apenas a chave de assinatura.

### Nunca apagar, nunca reescrever

Nem as telas de administração permitem apagar um registro ou mudar seu hash ou horário. Um livro de registros só tem valor se quem o mantém não puder mexer nele. Quando você atualiza um post, o registro antigo fica e um novo é acrescentado. O plugin para WordPress segue a mesma regra.

### Dizer logo de início o que ele não faz

Um registro mostra que dados correspondentes ao hash existiam naquele momento. Nada além disso. Não mostra que foi você quem criou, que você é o titular nem que o conteúdo é correto, e **não garante efeito jurídico**. Repito isso em vários pontos do site, porque é a expectativa errada que acaba prejudicando as pessoas.

### Ser transparente sobre o que é coletado

Para evitar abusos, aplicar os limites, investigar falhas e entender o uso, cada uso é registrado com o endereço IP e alguns outros dados. Isso não é usado para publicidade nem vendido. Endereços IP e nomes de host ficam neste servidor por 30 dias; depois vão para um armazenamento separado que eu administro, por até 13 meses, e então o final do endereço é removido e só restam estatísticas. Os detalhes estão nos [termos](/pt/terms).

## Para qualquer pessoa

É gratuito e não precisa de conta. A interface está disponível em 20 idiomas. Também há um carimbo para fotos, uma forma de registrar uma URL publicada, uma API e um plugin para WordPress. Você pode [baixar o plugin na página da API](/api#wordpress); a publicação no wordpress.org está em análise.

Para o passo a passo, e para as vias formais que existem no Brasil, leia [Como mostrar que você fez primeiro](/pt/column/prove-you-made-it-first).

## Me conte o que não funciona

Quero saber onde o DateSealed atrapalha e o que você gostaria que ele fizesse, principalmente se você é fotógrafo ou blogueiro e já passou por uma disputa de "quem fez primeiro". Os contatos estão no rodapé da página.
