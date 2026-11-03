title: Cómo demostrar que lo hiciste primero: una fecha de terceros para tus fotos y borradores
description: Todas las fechas que guardas tú se pueden editar. Cómo registrar gratis y sin subir nada que una foto o un borrador existían un día concreto, y qué prueba eso.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Si alguien copia tu trabajo, ¿podrás demostrar que el tuyo existía antes? Esta guía explica cómo prepararte para ese momento, gratis y sin enseñarle tu obra a nadie.

## Todas las fechas que tienes se pueden editar

El problema de las fechas como prueba es sencillo: todo lo que puedes cambiar tú, la otra parte puede decir que lo cambiaste.

| La fecha que tienes | Por qué es débil |
|---|---|
| Fecha de publicación del CMS | Puedes poner una fecha pasada. WordPress explica cómo hacerlo.[^wp] |
| Metadatos de la foto (Exif) | Herramientas gratuitas como ExifTool los editan, e incluso desplazan fechas en bloque.[^exif] |
| Fechas del archivo | En Windows, un archivo copiado recibe una nueva fecha de creación (la de modificación se conserva).[^kb] |
| Capturas de pantalla | Se retocan como cualquier imagen. |

Cada una es mejor que nada, pero ninguna responde a la pregunta «¿no pudiste fabricarlo después?». Lo que necesitas es una fecha anotada por **alguien distinto de ti**, de una forma que **nadie pueda reescribir más tarde**.

## Cómo registrar con DateSealed

1. Abre la [página principal](/es/) y pega un texto o elige un archivo. También puedes introducir una URL o un SHA-256 que ya tengas.
2. Comprueba el SHA-256 que aparece y pulsa «Registrar ahora». El hash se calcula en tu navegador, así que el archivo o el texto nunca se envían.
3. Se abre la página del registro. Descarga el `.tsr` (sello de tiempo firmado) y el `.ots` (prueba en Bitcoin) y guárdalos **junto con el archivo original**.

Cada registro lleva dos fechas: un sello de tiempo RFC 3161 que se devuelve al instante y un registro de OpenTimestamps que queda anclado en un bloque de Bitcoin en unas horas. Una vez anclado, la fecha se puede comprobar solo con la cadena de bloques de Bitcoin, aunque DateSealed cierre. La página del registro incluye los comandos para verificarlo en tu propio equipo.

El límite es de 10 registros por hora y 50 al día por dirección IP.

## ¿Vas a publicar fotos? Usa el sellado

[Sellar fotos](/es/stamp) registra el hash de tu original y después, en tu navegador, crea una copia con una pequeña insignia que muestra la fecha del registro y la dirección de su página. La foto no se sube.

El registro corresponde **al original**. La copia sellada es otro archivo y la insignia se puede recortar; por sí sola no prueba nada. Publica la copia sellada y guarda bien el original.

## Qué muestra un registro y qué no

Muestra que **existían, en el momento registrado, unos datos que coinciden con este hash**. Nada más.

- No muestra que el contenido sea correcto ni original.
- No muestra que lo hayas creado tú ni que te pertenezca. El registro no dice quién es el autor.
- **No garantiza ningún efecto legal.** En la Unión Europea, y por tanto en España, el Reglamento eIDAS concede a los sellos cualificados de tiempo electrónicos una presunción de exactitud de la fecha y la hora y de integridad de los datos.[^eidas] En México, la NOM-151-SCFI-2016 regula las constancias de conservación de mensajes de datos, que emite un prestador de servicios de certificación acreditado; la norma toma como referencia el protocolo RFC 3161.[^nom151] El registro de DateSealed usa ese mismo formato técnico, pero no es ni un sello cualificado ni una constancia NOM-151.

## Para lo que de verdad necesites proteger

Tanto en España como en México los derechos de autor nacen con la obra, sin trámites. Registrar no los crea, pero deja una prueba con más peso.

- **España.** La propiedad intelectual corresponde al autor «por el solo hecho de su creación» (art. 1 de la Ley de Propiedad Intelectual), y la ley presume, salvo prueba en contrario, que los derechos inscritos en el Registro existen y pertenecen a su titular (art. 145.3).[^lpi] La inscripción es voluntaria y no tiene carácter constitutivo.[^rpi]
- **México.** La Ley Federal del Derecho de Autor protege la obra desde que se fija en un soporte material y no exige registro (art. 5); las inscripciones en el registro del INDAUTOR hacen presumir ciertos los hechos y actos que constan en ellas, salvo prueba en contrario (art. 168).[^lfda]

| Vía | Coste | Para qué sirve |
|---|---|---|
| Registro de la Propiedad Intelectual (España) | En el Registro Central, tasa de tramitación de 14,97 € en persona u 8,26 € por vía telemática (tasas de 2026). Los registros autonómicos fijan las suyas.[^tasas] | Presunción de que los derechos inscritos existen y son del titular |
| Registro de obra ante el INDAUTOR (México) | 367 pesos según la ficha oficial del trámite, consultada en noviembre de 2026; respuesta en 15 días hábiles[^indautor] | Presunción de que los hechos inscritos son ciertos |
| Sello cualificado (UE) o constancia NOM-151 (México) | Según el proveedor | Documentos que necesitan un valor legal reconocido |
| DateSealed | Gratis | Poner fecha, de entrada, al flujo constante de fotos, artículos y borradores |

En otros países de América Latina, consulta la oficina nacional de derechos de autor. DateSealed es una primera capa rápida y gratuita: una prueba más para poner junto a las demás.

## Dos cosas que recordar

- **Guarda el original.** DateSealed solo tiene el hash. Sin el archivo original, el registro no se puede vincular a nada.
- **Vuelve a registrar después de cada cambio.** Basta con cambiar un carácter para que el hash cambie. En WordPress, [el plugin](/api#wordpress) registra cada publicación y cada actualización por ti.

[^wp]: WordPress.org, «Write Posts (Classic Editor)» <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Artículo KB299648 de Microsoft Knowledge Base (cómo se tratan las fechas al copiar o mover archivos)
[^lpi]: Real Decreto Legislativo 1/1996, texto refundido de la Ley de Propiedad Intelectual, arts. 1 y 145 (BOE, texto consolidado) <https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930>
[^rpi]: Ministerio de Cultura, «Finalidad del Registro de la Propiedad Intelectual» <https://www.cultura.gob.es/cultura/areas/propiedadintelectual/mc/rpi/que-es/fines-rpi.html>
[^tasas]: Ministerio de Cultura, Registro de la Propiedad Intelectual, «Tasas» (tasas 2026 del Registro Central) <https://www.cultura.gob.es/cultura/areas/propiedadintelectual/mc/rpi/registro-obras/tasas.html>
[^lfda]: Ley Federal del Derecho de Autor de México, arts. 5 y 168 (WIPO Lex) <https://www.wipo.int/wipolex/edocs/lexdocs/laws/es/mx/mx160es.html>
[^indautor]: Gobierno de México, ficha del trámite INDAUTOR-01-001, «Registro de Obra literaria o artística» <https://www.gob.mx/public/tramites/detalleTramite.xhtml?homoclave=INDAUTOR-01-001>
[^eidas]: Reglamento (UE) n.º 910/2014 (eIDAS), artículo 41, apartado 2 (BOE, publicación del DOUE) <https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822>
[^nom151]: Secretaría de Economía, NOM-151-SCFI-2016 (DOF, 30 de marzo de 2017), apartados 3 y 6.2 <https://www.gob.mx/cms/uploads/attachment/file/483868/Norma_Oficial_Mexicana_NOM-151-SCFI-2016_Requisitos_que_deben_observarse_para_la_conservacion_de_mensajes_de_datos_y_digitalizacion_de_documentos.pdf>
