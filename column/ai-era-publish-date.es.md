title: Tu fecha de publicación la pones tú: una fecha que nadie pueda reescribir en la era de la IA
description: Reescribir un artículo cuesta segundos y la fecha del CMS no prueba nada. Cómo dejar una fecha de terceros en cada entrada, incluso en WordPress, y sus límites.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Imagina que, a la mañana siguiente de publicar, aparece una copia casi idéntica: párrafos reordenados, frases cambiadas, el mismo esqueleto. ¿Cómo demostrarías que la tuya fue primero?

## Reescribir se ha vuelto barato

Parafrasear, reestructurar o traducir antes costaba horas de trabajo humano. Ahora un modelo de lenguaje lo hace en un momento. Las cifras muestran lo habitual que es ya el contenido escrito y leído por máquinas.

| Fuente | Dato |
|---|---|
| Imperva, 2025 Bad Bot Report | El 51 % del tráfico web en 2024 fue automatizado; los bots maliciosos fueron el 37 %, frente al 32 %[^imperva] |
| Cloudflare, julio de 2025 | Las peticiones de GPTBot en su red crecieron un 305 % de mayo de 2024 a mayo de 2025[^cf1] |
| Cloudflare, agosto de 2025 | Cerca del 80 % del rastreo de IA del año anterior fue para entrenar modelos[^cf2] |
| NewsGuard | Sitios de noticias que publican contenido generado por IA con poca supervisión humana: 49 en mayo de 2023, 3749 en junio de 2026[^newsguard] |
| Ahrefs, mayo de 2025 | El 74,2 % de 900 000 páginas publicadas por primera vez en abril de 2025 contenía algo de texto generado por IA[^ahrefs] |
| Artículo de NeurIPS 2023 | Un modelo de paráfrasis bajó la precisión de un detector de texto de IA del 70,3 % al 4,6 %[^neurips] |

Son estimaciones de empresas o investigadores, cada una con su método, y ninguna es la probabilidad de que copien *tu* entrada. Pero muestran que reescribir es fácil y difícil de detectar.

## Tu fecha de publicación la pones tú

Tú eliges la fecha de publicación. WordPress permite publicar con una fecha pasada y cambiar la fecha de una entrada ya publicada.[^wp] La fecha del otro sitio es igual de autodeclarada, así que dos personas diciendo «yo fui primero» no resuelven nada. Los archivos web ayudan, pero no controlas si guardan tu página ni cuándo.

Lo que necesitas es que **alguien distinto de ti** anote la fecha **en el momento de publicar**, en un lugar que **nadie pueda reescribir después**.

## Qué hace DateSealed

- Recibe solo el **hash SHA-256** de tu entrada, calculado en tu navegador (o en tu propio servidor, con el plugin de WordPress). El texto nunca se envía.
- Le añade un **sello de tiempo RFC 3161**, que se devuelve al instante, y un **registro en Bitcoin** mediante OpenTimestamps, anclado en unas horas.
- Nadie puede escribir una hora en la cadena de bloques de Bitcoin a posteriori. Una vez anclada, la fecha se comprueba solo con el archivo de prueba y la cadena, aunque DateSealed desaparezca.

Hay más detalles en «[Cómo demostrar que lo hiciste primero](/es/column/prove-you-made-it-first)» y «[Por qué creé DateSealed](/es/column/why-i-built-datesealed)».

## Automático en WordPress

Un hábito que tienes que recordar no sobrevive a una semana complicada. El plugin de DateSealed para WordPress:

- calcula en tu servidor el hash del texto en cada publicación y actualización, y solo envía el hash;
- **añade un registro nuevo** en cada actualización, de modo que la primera publicación nunca se sobrescribe y el historial de revisiones se va acumulando;
- puede mostrar una insignia con enlace a la página del registro (opcional);
- requiere WordPress 5.8 o superior y PHP 8.2 o superior.

[Descárgalo desde la página de la API](/api#wordpress); luego, en WordPress, ve a *Plugins → Add New → Upload Plugin*, actívalo y abre *Settings → DateSealed* (en un WordPress en español, estos menús aparecen traducidos). Su publicación en wordpress.org está en revisión.

## Lo que el registro no dice

- No muestra si el texto lo escribió una persona o un modelo.
- No muestra que el contenido sea correcto u original, quién lo escribió ni de quién es.
- **No garantiza ningún efecto legal.** En la Unión Europea, la presunción legal de exactitud corresponde a los sellos cualificados de tiempo electrónicos (eIDAS);[^eidas] en México, la NOM-151-SCFI-2016 regula las constancias de conservación de mensajes de datos que emiten prestadores acreditados.[^nom151] DateSealed no es ninguna de las dos cosas.

«Existía en este momento» es un buen punto de partida para una conversación, pero no la zanja por sí solo. Usa el registro como una prueba más, junto a las demás.

## Hábitos que dan valor al registro

1. **Guarda el original.** DateSealed solo guarda hashes.
2. **Guarda los archivos de prueba.** Conserva el `.tsr` y el `.ots` junto al original para poder verificar sin DateSealed.
3. **Registra al publicar.** La hora del registro es la hora en que lo hiciste; cada día de retraso lo debilita.
4. **No lo sobrevalores.** Si un caso importa de verdad, añade la inscripción en el Registro de la Propiedad Intelectual (España) o en el INDAUTOR (México), o un sello de tiempo cualificado.

[^imperva]: Imperva, «2025 Imperva Bad Bot Report» (15 de abril de 2025; datos de la red de Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog de Cloudflare (1 de julio de 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog de Cloudflare (29 de agosto de 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, «AI Tracking Center» <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, «What Percentage of New Content Is AI-Generated?» (19 de mayo de 2025; con su propio detector, que la empresa reconoce imperfecto) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., «Paraphrasing evades detectors of AI-generated text», NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, «Write Posts (Classic Editor)» <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^eidas]: Reglamento (UE) n.º 910/2014 (eIDAS), artículo 41, apartado 2 (BOE, publicación del DOUE) <https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822>
[^nom151]: Secretaría de Economía, NOM-151-SCFI-2016 (DOF, 30 de marzo de 2017) <https://www.gob.mx/cms/uploads/attachment/file/483868/Norma_Oficial_Mexicana_NOM-151-SCFI-2016_Requisitos_que_deben_observarse_para_la_conservacion_de_mensajes_de_datos_y_digitalizacion_de_documentos.pdf>
