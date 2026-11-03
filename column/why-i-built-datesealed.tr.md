title: DateSealed'i Neden Yaptım: Geliştiriciden Bir Not
description: Emlak fotoğraflarını kopyalanmaya karşı korumak istedim. Mevcut seçeneklerde ne bulduğum ve benim bile değiştiremediğim ücretsiz bir kayıt için kurallarım.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed, bir metnin, fotoğrafın ya da web sayfasının ne zaman var olduğunu kaydeden ücretsiz bir araç. Ben Yuki Nakazawa, aracı ben yaptım. Bu yazı, neden yaptığımı ve yol boyunca verdiğim kararları anlatıyor.

## Başlangıç emlak fotoğraflarıydı

Japonya'da bir emlak şirketi yönetiyorum; ilanlarımızın fotoğraflarını çekip yayımlıyoruz. Bir gün biri bu fotoğraflardan birini değiştirir ya da başka bir sitede yayımlarsa, aslının bizim olduğunu ve önce var olduğunu gösterebilmek istedim.

Orijinal dosyalar elimdeydi, yazılarımın yayın tarihleri vardı. Ama bunların hepsini kendim değiştirebilirdim; kopyası olan herkes de aynı tarihleri iddia edebilirdi. İhtiyacım olan, **benden başka biri** tarafından, **sonradan kimsenin değiştiremeyeceği** bir biçimde yazılmış bir tarihti.

## Önce ne buldum

Kasım 2026 itibarıyla Japonya'da nelerin mevcut olduğuna baktım:

- **Noterden kesin tarih.** Belge başına 700 yen. Elektronik bir sürümü var, ama yalnızca 10 MB'a kadar metin, PDF ve XML dosyalarını kabul ediyor ve işlemler hafta içi yapılıyor.
- **Kültür İşleri Ajansı'na tescil.** Eser başına 3.000 yen, kâğıt üzerinde ve her eser için ayrı başvuru. Eserin tescil edilen tarihte yayımlandığı karinesini doğuruyor.
- **İçişleri ve İletişim Bakanlığı'nın onayladığı sağlayıcıların zaman damgaları.** Japonya'da resmî statüsü olanlar bunlar. Fiyatlandırma çoğunlukla şirketlere yönelik.
- **Blokzincir tabanlı kayıt hizmetleri.** Bulduklarım işletmelere yönelikti ya da ücretliydi.
- **Kamera içi imza (C2PA).** Bazı kameralar fotoğrafları çekildiği anda imzalıyor. Bu, dosyanın nereden geldiğini söyler; ne zaman var olduğu ise ayrı bir sorudur.

Bunların hepsi işe yarar ve gerçekten korumanız gereken o tek şey için kullanmalısınız. Ama her yeni fotoğraf ya da yazı için ödeme yapıp başvuru doldurmak gerçekçi değil. Benim istediğim **ücretsiz, üyelik gerektirmeyen, hiçbir şey yüklenmeyen, işletenin bile değiştiremeyeceği bir yerde saklanan ve WordPress'te her yayında otomatik çalışan** bir şeydi. Bulamadım, ben de yaptım.

## Koyduğum kurallar

### Özetten başka bir şey almamak

DateSealed yalnızca dosyanızın ya da metninizin SHA-256 özetini, yani 64 karakterlik bir parmak izini alır. Özet tarayıcınızda hesaplanır; fotoğraflarınız ve taslaklarınız bilgisayarınızdan çıkmaz. İnsanların kaydetmek istediği tam da yayımlanmamış işlerdir; kaydettirmek için onları teslim etmek amacı boşa çıkarırdı.

### Bana güvenmek zorunda kalmamalısınız

Her kayda iki tarih verilir. Biri, DateSealed'in kendi zaman damgası otoritesinin imzaladığı ve hemen dönen bir RFC 3161 zaman damgasıdır. Diğeri, OpenTimestamps aracılığıyla genellikle birkaç saat içinde bir Bitcoin bloğuna işlenir.

İlki ancak benim kadar güvenilirdir. İkincisini değiştirmek benim elimde değil. İşlendikten sonra, DateSealed ortadan kalksa bile, tarihi yalnızca kanıt dosyası (`.ots`) ve Bitcoin defteriyle doğrulayabilirsiniz. Her kayıt sayfasında, kendi bilgisayarınızda doğrulamak için gereken komutlar yer alır.

Zaman damgası otoritesinin kök anahtarı kendi bilgisayarımda oluşturuldu ve bir parolayla şifrelenmiş olarak saklanıyor. Sunucuda yalnızca imzalama anahtarı var.

### Asla silmemek, asla değiştirmemek

Yönetim ekranlarında bile bir kaydı silmenin ya da özetini veya zamanını değiştirmenin yolu yok. Bir defter, ancak işleteni ona dokunamıyorsa bir değer taşır. Bir yazıyı güncellediğinizde eski kayıt kalır, yenisi eklenir. WordPress eklentisi de aynı kuralı izler.

### Yapamadıklarını baştan söylemek

Bir kayıt, özetle eşleşen verinin o anda var olduğunu gösterir. Fazlasını değil. Onu sizin yaptığınızı, sizin olduğunu ya da doğru olduğunu göstermez ve **hukuki bir etkiyi garanti etmez**. Bunu sitenin birçok yerinde söylüyorum, çünkü insanlara zarar veren şey yanlış beklentidir.

### Toplananlar konusunda açık olmak

Kötüye kullanımı önlemek, sınırları uygulamak, hataları ayıklamak ve kullanımı anlamak için her kullanımda IP adresi ve birkaç başka bilgi kaydedilir. Reklam için kullanılmaz ve satılmaz. IP adresleri ve ana makine adları bu sunucuda 30 gün kalır, sonra benim yönettiğim ayrı bir depolamaya taşınarak en fazla 13 ay saklanır; ardından adresin son kısmı silinir ve yalnızca istatistik kalır. Ayrıntılar [koşullarda](/tr/terms).

## Herkes için

Ücretsiz ve hesap gerektirmiyor. Arayüz 20 dilde. Fotoğraflar için bir damga, yayımlanmış bir URL'yi kaydetmenin bir yolu, bir API ve bir WordPress eklentisi de var. [Eklentiyi API sayfasından indirebilirsiniz](/api#wordpress); wordpress.org'daki listelemesi incelemede.

"Kim önceydi" tartışmasına pratikte nasıl hazırlanacağınızı merak ediyorsanız [Önce sizin yaptığınızı nasıl gösterirsiniz](/tr/column/prove-you-made-it-first) yazısına bakın.

## Neyin aksadığını bana söyleyin

DateSealed'in nerede işinizi zorlaştırdığını ve bundan sonra ne yapmasını istediğinizi duymak isterim; özellikle "kim önceydi" tartışması yaşamış fotoğrafçılardan ve blog yazarlarından. İletişim bilgileri sayfanın altında.
