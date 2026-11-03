title: Por qué creé DateSealed: nota del desarrollador
description: Empezó con fotos de inmuebles que quería proteger de copias. Qué opciones encontré y qué reglas me puse para un registro gratuito que ni yo puedo reescribir.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed es una herramienta gratuita que registra cuándo existía un texto, una foto o una página web. Me llamo Yuki Nakazawa y la desarrollé yo. En esta nota cuento por qué, y qué decisiones tomé por el camino.

## Todo empezó con fotos de inmuebles

Dirijo una empresa inmobiliaria en Japón; fotografiamos los inmuebles y publicamos los anuncios. Quería estar preparado para el día en que alguien retocara una de esas fotos o la publicara en otro sitio, y poder demostrar que el original era nuestro y que existía antes.

Tenía los archivos originales, y mis publicaciones tenían fecha. Pero todas esas fechas podía cambiarlas yo mismo, y cualquiera con una copia podía alegar las mismas. Lo que necesitaba era una fecha anotada por **alguien distinto de mí**, de una forma que **nadie pudiera cambiar después**.

## Lo que encontré primero

Revisé lo que había en Japón en noviembre de 2026:

- **Fecha cierta ante notario.** 700 yenes por documento. Existe una versión electrónica, pero solo admite archivos de texto, PDF y XML de hasta 10 MB, y se tramita en días hábiles.
- **Registro ante la Agencia de Asuntos Culturales.** 3000 yenes por obra, en papel y de una en una. Hace presumir que la obra se publicó en la fecha registrada.
- **Sellos de tiempo de proveedores acreditados por el Ministerio del Interior y Comunicaciones.** Son los que tienen reconocimiento oficial en Japón, con precios pensados sobre todo para empresas.
- **Servicios de registro en blockchain.** Los que encontré eran para empresas o de pago.
- **Firmas en la propia cámara (C2PA).** Algunas cámaras firman la foto al tomarla. Eso indica de dónde viene un archivo, que es una pregunta distinta de cuándo existía.

Todo eso es útil y, para lo que de verdad necesites proteger, conviene usarlo. Pero pagar y hacer un trámite por cada foto o artículo nuevo no es realista. Yo quería algo **gratuito, sin crear cuenta, sin subir nada, guardado donde ni el operador pueda reescribirlo y automático en WordPress cada vez que publicas**. No lo encontré, así que lo construí.

## Las reglas que me puse

### Recibir solo un hash

DateSealed recibe únicamente el hash SHA-256 de tu archivo o texto, una huella de 64 caracteres. El hash se calcula en tu navegador, así que tus fotos y borradores no salen de tu equipo. Lo que la gente quiere registrar es justamente lo que aún no ha publicado, y tener que entregarlo para registrarlo no tendría sentido.

### No deberías tener que confiar en mí

Cada registro lleva dos fechas. Una es un sello de tiempo RFC 3161 firmado por la autoridad de sellado de tiempo propia de DateSealed, que se devuelve al instante. La otra queda anclada en un bloque de Bitcoin mediante OpenTimestamps, normalmente en unas horas.

La primera vale lo que valga mi palabra. La segunda no está en mis manos. Una vez anclada, puedes comprobar la fecha solo con el archivo de prueba (`.ots`) y la cadena de bloques de Bitcoin, aunque DateSealed desaparezca. Cada página de registro incluye los comandos para verificarlo en tu propio equipo.

La clave raíz de la autoridad de sellado se generó en mi propio ordenador y se guarda cifrada con una frase de contraseña. El servidor solo tiene la clave de firma.

### Nunca borrar, nunca reescribir

Ni siquiera las pantallas de administración permiten borrar un registro ni cambiar su hash o su hora. Un registro solo vale algo si quien lo lleva no puede tocarlo. Cuando actualizas una entrada, el registro anterior se queda y se añade uno nuevo. El plugin de WordPress sigue la misma regla.

### Decir de entrada lo que no puede hacer

Un registro muestra que existían, en ese momento, unos datos que coinciden con el hash. Nada más. No muestra que tú los creaste, que te pertenecen ni que sean correctos, y **no garantiza ningún efecto legal**. Lo digo en muchos lugares del sitio, porque las expectativas equivocadas son las que acaban haciendo daño.

### Ser claro con lo que se recoge

Para evitar abusos, aplicar los límites, investigar fallos y entender el uso, cada uso se registra con la dirección IP y algunos datos más. No se usa para publicidad ni se vende. Las direcciones IP y los nombres de host permanecen en este servidor 30 días; después pasan a un almacenamiento separado que gestiono yo, durante un máximo de 13 meses, y pasado ese plazo se recorta el final de la dirección y solo quedan estadísticas. Los detalles están en los [términos](/es/terms).

## Para cualquiera

Es gratis y no hace falta crear una cuenta. La interfaz está disponible en 20 idiomas. También hay un sellado para fotos, una forma de registrar una URL ya publicada, una API y un plugin de WordPress. Puedes [descargar el plugin desde la página de la API](/api#wordpress); su publicación en wordpress.org está en revisión.

Si quieres los pasos concretos, y qué vías formales existen en España y México, lee [Cómo demostrar que lo hiciste primero](/es/column/prove-you-made-it-first).

## Cuéntame qué falla

Me gustaría saber dónde te estorba DateSealed y qué te gustaría que hiciera, sobre todo si eres fotógrafo o bloguero y has vivido una disputa de «quién fue primero». Los datos de contacto están al pie de la página.
