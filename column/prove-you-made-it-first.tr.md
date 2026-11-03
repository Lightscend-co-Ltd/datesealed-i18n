title: Önce Sizin Yaptığınızı Nasıl Gösterirsiniz: Fotoğraf ve Taslaklarınıza Üçüncü Taraf Tarihi
description: Elinizdeki her tarih değiştirilebilir. Bir işin belirli bir günde var olduğunu ücretsiz ve dosya yüklemeden kaydetmek, sınırları ve Türkiye'deki resmî yollar.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Biri işinizi kopyalarsa, sizinkinin önce olduğunu gösterebilir misiniz? Bu rehber, o ana ücretsiz ve işinizi kimseye göstermeden nasıl hazırlanacağınızı anlatıyor.

## Elinizdeki her tarih değiştirilebilir

Tarih kanıtının sorunu basit: kendinizin değiştirebildiği her şey için karşı taraf "sen değiştirdin" diyebilir.

| Elinizdeki tarih | Neden zayıf |
|---|---|
| İçerik yönetim sistemindeki yayın tarihi | Geçmiş bir tarih seçebilirsiniz; WordPress bunun nasıl yapıldığını anlatıyor.[^wp] |
| Fotoğraf üst verisi (Exif) | ExifTool gibi ücretsiz araçlar onu düzenler, tarihleri toplu olarak kaydırabilir.[^exif] |
| Dosya zaman bilgileri | Windows'ta kopyalanan dosya yeni bir oluşturma zamanı alır (değiştirme zamanı korunur).[^kb] |
| Ekran görüntüleri | Her görüntü gibi düzenlenebilir. |

Her biri hiç yoktan iyidir, ama hiçbiri "Bunu sonradan uyduramaz mıydın?" sorusuna cevap vermez. İhtiyacınız olan, **sizden başka biri** tarafından, **sonradan kimsenin değiştiremeyeceği** bir biçimde yazılmış bir tarihtir.

## DateSealed ile kayıt

1. [Ana sayfayı](/tr/) açın, metni yapıştırın ya da bir dosya seçin. Bir URL ya da elinizdeki bir SHA-256 özetini de girebilirsiniz.
2. Gösterilen SHA-256'yı kontrol edin ve kaydetmek için düğmeye basın. Özet tarayıcınızda hesaplanır; dosyanın ya da metnin kendisi gönderilmez.
3. Kayıt sayfası açılır. `.tsr` (imzalı zaman damgası) ve `.ots` (Bitcoin kanıtı) dosyalarını indirin ve **orijinal dosyayla birlikte** saklayın.

Her kayda iki tarih verilir: hemen dönen bir RFC 3161 zaman damgası ve birkaç saat içinde bir Bitcoin bloğuna işlenen bir OpenTimestamps kaydı. İşlendikten sonra tarih, DateSealed kapansa bile yalnızca Bitcoin defteriyle kontrol edilebilir. Kayıt sayfasında kendi bilgisayarınızda doğrulama komutları yer alır.

Sınır, IP adresi başına saatte 10, günde 50 kayıttır. URL girişi 2 kayıt sayılır.

## Fotoğraf mı yayımlıyorsunuz? Damgayı kullanın

[Fotoğraf damgası](/tr/stamp), orijinal fotoğrafınızın özetini kaydeder; ardından tarayıcınızda, kayıt tarihini ve kayıt sayfasının adresini gösteren küçük bir rozet taşıyan bir kopya oluşturur. Fotoğrafın kendisi yüklenmez.

Kayıt **orijinali** gösterir. Damgalı kopya farklı bir dosyadır ve rozet kırpılabilir; tek başına hiçbir şey kanıtlamaz. Damgalı kopyayı yayımlayın, orijinali güvende tutun.

## Kayıt neyi gösterir, neyi göstermez

**Bu özetle eşleşen verinin kaydedilen anda var olduğunu** gösterir. Hepsi bu.

- İçeriğin doğru ya da özgün olduğunu göstermez.
- Onu sizin yaptığınızı ya da sizin olduğunu göstermez. Kayıt, kimin oluşturduğunu söylemez.
- **Hukuki bir etkiyi garanti etmez.** Türkiye'de 5070 sayılı Elektronik İmza Kanunu zaman damgasını, bir elektronik verinin üretildiği, değiştirildiği, gönderildiği, alındığı ya da kaydedildiği zamanı tespit etmek için elektronik sertifika hizmet sağlayıcısının (ESHS) elektronik imzayla doğruladığı kayıt olarak tanımlar; ESHS'ler faaliyete Kuruma bildirimle geçer.[^5070] Bilgi Teknolojileri ve İletişim Kurumu'nun (BTK) sitesinde Kasım 2026'da 8 ESHS listeleniyor.[^btk] AB'de ise nitelikli elektronik zaman damgasının tarih, saat ve veri bütünlüğü bakımından doğru olduğu karine olarak kabul edilir.[^eidas] DateSealed bir ESHS değildir ve kaydı nitelikli bir zaman damgası da değildir.

## Gerçekten korumanız gereken şey için

Türkiye'de eser üzerindeki haklar eser sahibine aittir ve herhangi bir kurum aracılığıyla edinilmez; tescil yaptırmamak hak kaybına yol açmaz. Yine de resmî yollar var:

- **Kültür ve Turizm Bakanlığı'nda isteğe bağlı kayıt-tescil.** 5846 sayılı Fikir ve Sanat Eserleri Kanunu'nun 13. maddesine ve ilgili yönetmeliğe dayanır. Beyana dayalı bir işlemdir ve verilen belge hak veren bir belge değildir; bakanlığa göre eser sahibinin "ispat edilmesinde kolaylık sağlar". Başvuru çevrim içi yapılır, belgeler Telif Hakları Genel Müdürlüğü'ne şahsen ya da postayla gönderilir.[^ktb] Bakanlığın ücret sayfasında Kasım 2026'da işlem ücreti 1.970 TL olarak gösteriliyor.[^ktb_fee]
- **Noter.** Noterlik Kanunu'na göre noterler, getirilen kâğıtlardaki imzayı veya tarihi onaylar (m. 60), bir şeyin hâl ve şeklini tespit eder (m. 61) ve saklanmak üzere getirilen emanetleri muhafaza eder (m. 62).[^noter]
- **ESHS'lerin zaman damgası.** Kanuni çerçevesi olan elektronik zaman damgası budur.[^5070]

DateSealed, akıp giden fotoğraflar, yazılar ve taslaklar için ucuz ve hızlı ilk katmandır: diğer kanıtların yanına koyacağınız bir kanıt daha.

## Unutmamanız gereken iki şey

- **Orijinali saklayın.** DateSealed yalnızca özeti tutar. Orijinal dosya olmadan kayıt hiçbir şeye bağlanamaz.
- **Her düzenlemeden sonra yeniden kaydedin.** Tek bir karakteri değiştirmek özeti değiştirir. WordPress'te [eklenti](/api#wordpress) her yayını ve güncellemeyi sizin yerinize kaydeder.

[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Microsoft Bilgi Bankası makalesi KB299648 (dosyalar kopyalanırken veya taşınırken tarihlerin nasıl işlendiği)
[^5070]: 5070 sayılı Elektronik İmza Kanunu, m. 3(h) ve m. 8 (Mevzuat Bilgi Sistemi) <https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5070.pdf>
[^btk]: Bilgi Teknolojileri ve İletişim Kurumu, Elektronik Sertifika Hizmet Sağlayıcıları <https://www.btk.gov.tr/elektronik-sertifika-hizmet-saglayicilari>
[^eidas]: eIDAS Tüzüğü (AB) No 910/2014, Madde 41(2) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted> (Birleşik Krallık hukukunda korunan metin)
[^ktb]: Kültür ve Turizm Bakanlığı Telif Hakları Genel Müdürlüğü, İsteğe Bağlı Kayıt-Tescil <https://telifhaklari.ktb.gov.tr/TR-332370/istege-bagli-kayit-tescil.html>
[^ktb_fee]: Kültür ve Turizm Bakanlığı Telif Hakları Genel Müdürlüğü, Kayıt-Tescil Başvuru Ücreti <https://telifhaklari.ktb.gov.tr/TR-332349/kayit-tescil-basvuru-ucreti.html>
[^noter]: 1512 sayılı Noterlik Kanunu, m. 60–62 (Mevzuat Bilgi Sistemi) <https://www.mevzuat.gov.tr/mevzuatmetin/1.5.1512.pdf>
