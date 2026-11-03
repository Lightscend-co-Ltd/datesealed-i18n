title: Cara Menunjukkan Bahwa Anda yang Membuatnya Lebih Dulu: Beri Foto dan Naskah Tanggal dari Pihak Ketiga
description: Semua tanggal yang Anda pegang bisa diubah. Cara mencatat gratis tanpa mengunggah bahwa foto atau naskah sudah ada pada suatu hari, dan bedanya dengan pencatatan DJKI.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Jika seseorang menjiplak karya Anda, bisakah Anda menunjukkan bahwa karya Anda yang lebih dulu ada? Panduan ini menjelaskan cara bersiap untuk saat itu, gratis, tanpa memperlihatkan karya Anda kepada siapa pun.

## Semua tanggal yang Anda pegang bisa diubah

Masalah bukti tanggal itu sederhana: apa pun yang bisa Anda ubah sendiri, pihak lawan bisa bilang sudah Anda ubah.

| Tanggal yang Anda punya | Mengapa lemah |
|---|---|
| Tanggal terbit di CMS | Anda bisa memasang tanggal mundur. Dokumentasi WordPress menjelaskan caranya.[^wp] |
| Metadata foto (Exif) | Alat gratis seperti ExifTool bisa mengubahnya, bahkan menggeser tanggal banyak foto sekaligus.[^exif] |
| Tanggal file | Di Windows, file yang disalin mendapat waktu pembuatan baru (waktu modifikasinya tetap).[^kb] |
| Tangkapan layar | Bisa disunting seperti gambar lain. |

Semua itu lebih baik daripada tidak ada, tetapi tidak satu pun menjawab pertanyaan "bukankah ini bisa Anda buat belakangan?". Yang Anda perlukan adalah tanggal yang ditulis oleh **pihak selain Anda**, dalam bentuk yang **tidak bisa diubah siapa pun sesudahnya**.

## Mencatat dengan DateSealed

1. Buka [halaman utama](/id/), lalu tempel teks atau pilih file. Anda juga bisa memasukkan URL atau SHA-256 yang sudah Anda punya.
2. Periksa SHA-256 yang muncul, lalu tekan tombol untuk mencatatnya. Hash dihitung di browser Anda, jadi file atau teksnya sendiri tidak pernah dikirim.
3. Halaman catatan terbuka. Unduh `.tsr` (tanda waktu bertanda tangan) dan `.ots` (bukti Bitcoin), lalu simpan **bersama file aslinya**.

Setiap catatan mendapat dua tanggal: tanda waktu RFC 3161 yang langsung dikembalikan, dan catatan OpenTimestamps yang tertambat ke blok Bitcoin dalam beberapa jam. Setelah tertambat, tanggalnya bisa diperiksa hanya dengan buku besar Bitcoin, bahkan jika DateSealed tutup. Halaman catatan memuat perintah untuk memverifikasinya di komputer Anda sendiri.

Batasnya 10 catatan per jam dan 50 per hari untuk setiap alamat IP.

## Menerbitkan foto? Pakai stempel

[Stempel foto](/id/stamp) mencatat hash foto asli Anda, lalu di dalam browser membuat salinan dengan lencana kecil berisi tanggal catatan dan alamat halaman catatan. Fotonya sendiri tidak diunggah.

Catatan itu menunjuk ke **foto asli**. Salinan berstempel adalah file yang berbeda, dan lencananya bisa dipotong; lencana saja tidak membuktikan apa-apa. Terbitkan salinan berstempel dan simpan foto aslinya baik-baik.

## Jalur resmi di Indonesia

- **Hak cipta lahir otomatis.** Menurut Undang-Undang Nomor 28 Tahun 2014 tentang Hak Cipta, hak cipta timbul secara otomatis berdasarkan prinsip deklaratif setelah ciptaan diwujudkan dalam bentuk nyata (Pasal 1 angka 1), dan pencatatan ciptaan bukan syarat untuk mendapatkan hak cipta (Pasal 64 ayat 2).[^uuhc]
- **Pencatatan ciptaan di DJKI tetap berguna sebagai bukti.** Direktorat Jenderal Kekayaan Intelektual (DJKI) menganjurkan pencatatan sebagai bukti kepemilikan bila terjadi sengketa.[^djki] Orang yang namanya disebut dalam surat pencatatan ciptaan dianggap sebagai Pencipta, kecuali terbukti sebaliknya (Pasal 31). Namun pencatatan bukan pengesahan atas isi, arti, maksud, atau bentuk ciptaan (Pasal 72).[^uuhc]
- **Biaya sedang berubah.** Menurut DJKI, berdasarkan PP Nomor 30 Tahun 2026, pencatatan hak cipta untuk lagu dan musik gratis mulai 1 Agustus 2026, dan pemerintah membuka peluang untuk memperluasnya ke jenis karya lain.[^djkitarif] Periksa tarif yang berlaku untuk jenis ciptaan Anda di laman DJKI sebelum mengajukan.
- **Penanda waktu elektronik.** Peraturan Menteri Kominfo Nomor 11 Tahun 2022 membedakan penanda waktu elektronik *tersertifikasi*, yang memakai Sertifikat Elektronik dan tanda tangan dari PSrE Indonesia, dan yang *tidak tersertifikasi*, yang dibuat tanpa jasa PSrE Indonesia (Pasal 42–43).[^pm11]

DateSealed bukan pencatatan ciptaan dan bukan PSrE Indonesia. Tanda waktunya dibuat tanpa jasa PSrE Indonesia.

## Apa yang ditunjukkan catatan, dan apa yang tidak

Catatan menunjukkan bahwa **data yang cocok dengan hash ini sudah ada pada waktu yang tercatat**. Itu saja.

- Tidak menunjukkan bahwa isinya benar atau orisinal.
- Tidak menunjukkan bahwa Anda pembuat atau pemiliknya. Catatan tidak menyebut siapa penciptanya.
- **Tidak menjamin akibat hukum apa pun.**

## Untuk satu karya yang benar-benar harus dilindungi

| Cara | Biaya | Cocok untuk |
|---|---|---|
| Pencatatan ciptaan di DJKI | Menurut PP 30/2026; lagu dan musik gratis sejak 1 Agustus 2026 | Karya penting yang mungkin diperebutkan kepemilikannya |
| Penanda waktu elektronik tersertifikasi (PSrE Indonesia) | Menurut penyedia | Dokumen yang memerlukan layanan tersertifikasi |
| DateSealed | Gratis | Foto, artikel, dan naskah yang terus bertambah, supaya punya tanggal lebih dulu |

DateSealed adalah lapisan pertama yang murah dan cepat: satu bukti lagi untuk diletakkan di samping bukti lainnya.

## Dua hal yang perlu diingat

- **Simpan file aslinya.** DateSealed hanya memegang hash. Tanpa file asli, catatan tidak bisa dikaitkan dengan apa pun.
- **Catat lagi setiap kali menyunting.** Ubah satu karakter saja, hash-nya berubah. Di WordPress, [plugin](/api#wordpress) mencatat setiap penerbitan dan pembaruan untuk Anda.

[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Artikel Microsoft Knowledge Base KB299648 (perlakuan tanggal saat file disalin atau dipindahkan)
[^uuhc]: Undang-Undang Nomor 28 Tahun 2014 tentang Hak Cipta (LN 2014 No. 266), Pasal 1, 31, 64, 72 <https://www.dgip.go.id/unduhan/download/uu-nomor-28-tahun-2014-tentang-hak-cipta-34-2014>
[^djki]: DJKI, "Hak Cipta: Pengenalan" <https://www.dgip.go.id/menu-utama/hak-cipta/pengenalan>
[^djkitarif]: DJKI, "Pemerintah Buka Peluang Pencatatan Hak Cipta Gratis untuk Karya Selain Lagu dan Musik" (24 Juli 2026) <https://dgip.go.id/artikel/detail-artikel-berita/pemerintah-buka-peluang-pencatatan-hak-cipta-gratis-untuk-karya-selain-lagu-dan-musik?kategori=agenda-ki>
[^pm11]: Peraturan Menteri Komunikasi dan Informatika Nomor 11 Tahun 2022 tentang Tata Kelola Penyelenggaraan Sertifikasi Elektronik, Pasal 42–43 <https://jdih.komdigi.go.id/produk_hukum/view/id/833/t/peraturan+menteri+komunikasi+dan+informatika+nomor+11+tahun+2022>
