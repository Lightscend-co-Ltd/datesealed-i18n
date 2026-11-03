title: Yayın Tarihiniz Beyandan İbaret: Yapay Zekâ Çağında Kimsenin Değiştiremeyeceği Bir Tarih
description: Bir yazıyı yeniden yazıp yayımlamak saniyeler sürüyor ve CMS tarihi tek başına bir şey kanıtlamıyor. Her yazıya üçüncü taraf tarihi, WordPress'te otomatik.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Yayımladığınızın ertesi sabahı neredeyse aynı bir kopyanın ortaya çıktığını düşünün: paragrafların yeri değişmiş, ifadeler farklı, iskelet aynı. Sizinkinin önce olduğunu nasıl gösterirdiniz?

## Yeniden yazmak ucuzladı

Başka sözcüklerle anlatmak, yeniden kurgulamak ve çevirmek eskiden insan zamanı isterdi. Şimdi bir dil modeli bunu anında yapıyor. Rakamlar, makinelerin yazdığı ve okuduğu içeriğin ne kadar yaygınlaştığını gösteriyor.

| Kaynak | Bulgu |
|---|---|
| Imperva, 2025 Bad Bot Report | 2024'te web trafiğinin %51'i otomatikti; kötü niyetli botların payı %32'den %37'ye çıktı[^imperva] |
| Cloudflare, Temmuz 2025 | Ağındaki GPTBot istekleri Mayıs 2024'ten Mayıs 2025'e %305 arttı[^cf1] |
| Cloudflare, Ağustos 2025 | Önceki yıldaki yapay zekâ taramalarının yaklaşık %80'i model eğitimi içindi[^cf2] |
| NewsGuard | Az insan denetimiyle yapay zekâ üretimi içerik yayımlayan haber siteleri: Mayıs 2023'te 49, Haziran 2026'ya kadar 3.749[^newsguard] |
| Ahrefs, Mayıs 2025 | Nisan 2025'te ilk kez yayımlanan 900.000 sayfanın %74,2'si bir miktar yapay zekâ üretimi içerik barındırıyordu[^ahrefs] |
| NeurIPS 2023 makalesi | Bir yeniden ifade modeli, bir yapay zekâ metin dedektörünün doğruluğunu %70,3'ten %4,6'ya düşürdü[^neurips] |

Bunlar her biri kendi yöntemine sahip şirket ya da araştırmacı tahminleri; hiçbiri *sizin* yazınızın kopyalanma olasılığı değil. Ama yeniden yazmanın kolay, fark edilmesinin zor olduğunu gösteriyorlar.

## Yayın tarihiniz beyandan ibaret

Yayın tarihini siz seçersiniz. WordPress geçmiş bir tarihle yayımlamaya ve yayındaki bir yazının tarihini değiştirmeye izin verir.[^wp] Öbür sitenin tarihi de aynı ölçüde beyandır; iki kişinin "ben önceydim" demesi hiçbir şeyi çözmez. Web arşivleri yardımcı olur, ama sayfanızı yakalayıp yakalamayacakları ya da ne zaman yakalayacakları sizin elinizde değildir.

İhtiyacınız olan, **sizden başka birinin**, tarihi **yayımladığınız anda**, **sonradan kimsenin değiştiremeyeceği** bir yere yazmasıdır.

## DateSealed ne yapar

- Yazınızın yalnızca tarayıcınızda (WordPress eklentisiyle kendi sunucunuzda) hesaplanan **SHA-256 özetini** alır. Metin gönderilmez.
- Hemen dönen bir **RFC 3161 zaman damgası** ve birkaç saat içinde işlenen, OpenTimestamps üzerinden bir **Bitcoin kaydı** ekler.
- Kimse Bitcoin defterine sonradan bir zaman yazamaz. İşlendikten sonra tarih, DateSealed ortadan kalksa bile yalnızca kanıt dosyası ve defterle kontrol edilebilir.

Ayrıntılar "[Önce sizin yaptığınızı nasıl gösterirsiniz](/tr/column/prove-you-made-it-first)" ve "[DateSealed'i neden yaptım](/tr/column/why-i-built-datesealed)" yazılarında.

## WordPress'te otomatik

Hatırlamanız gereken bir alışkanlık yoğun bir haftayı atlatamaz. DateSealed WordPress eklentisi:

- her yayında ve güncellemede yazı metninin özetini sunucunuzda hesaplar ve yalnızca özeti gönderir;
- her güncelleme için **yeni bir kayıt ekler**; ilk yayın asla üzerine yazılmaz ve sürüm geçmişi birikir;
- kayıt sayfasına bağlantı veren bir rozet gösterebilir (isteğe bağlı);
- WordPress 5.8+ ve PHP 8.2+ gerektirir.

[API sayfasından indirin](/api#wordpress), ardından WordPress'te *Plugins → Add New → Upload Plugin* yolunu izleyin, eklentiyi etkinleştirin ve *Settings → DateSealed*'i açın. wordpress.org listelemesi incelemede.

## Kaydın söylemedikleri

- Metni bir insanın mı yoksa bir modelin mi yazdığını göstermez.
- İçeriğin doğru ya da özgün olduğunu, kimin yazdığını ya da kimin sahibi olduğunu göstermez.
- **Hukuki bir etkiyi garanti etmez.** Türkiye'de kanuni çerçevesi olan zaman damgası, 5070 sayılı Elektronik İmza Kanunu kapsamında elektronik sertifika hizmet sağlayıcılarının verdiği zaman damgasıdır;[^5070] AB'de ise nitelikli elektronik zaman damgası.[^eidas] DateSealed kaydı ikisi de değildir.

"Bu anda vardı" bir tartışmayı başlatmak için yararlı bir noktadır; tek başına onu bitirmez. Kaydı, diğer kanıtların yanında bir kanıt olarak kullanın.

## Kaydı değerli kılan alışkanlıklar

1. **Orijinali saklayın.** DateSealed yalnızca özetleri tutar.
2. **Kanıt dosyalarını saklayın.** DateSealed olmadan doğrulayabilmek için `.tsr` ve `.ots` dosyalarını orijinalle birlikte tutun.
3. **Yayın anında kaydedin.** Kaydın zamanı onu oluşturduğunuz zamandır; geciken her gün onu zayıflatır.
4. **Abartmayın.** Önemli bir durum için Kültür ve Turizm Bakanlığı'nda isteğe bağlı kayıt-tescili ya da bir ESHS'nin zaman damgasını ekleyin; ayrıntılar [rehberde](/tr/column/prove-you-made-it-first).

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (15 Nisan 2025; Imperva ağ verileri) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare blogu (1 Temmuz 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare blogu (29 Ağustos 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (19 Mayıs 2025; Ahrefs'in kendi dedektörü, şirket kusursuz olmadığını belirtiyor) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna vd., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^5070]: 5070 sayılı Elektronik İmza Kanunu, m. 3(h) ve m. 8 (Mevzuat Bilgi Sistemi) <https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5070.pdf>
[^eidas]: eIDAS Tüzüğü (AB) No 910/2014, Madde 41(2) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
