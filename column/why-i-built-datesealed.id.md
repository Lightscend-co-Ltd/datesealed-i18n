title: Mengapa Saya Membuat DateSealed: Catatan dari Pengembang
description: Berawal dari keinginan melindungi foto properti dari penjiplakan. Apa yang saya temukan, dan aturan untuk catatan gratis yang bahkan tidak bisa saya ubah sendiri.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed adalah alat gratis untuk mencatat kapan sebuah teks, foto, atau halaman web sudah ada. Saya Yuki Nakazawa, pembuatnya. Tulisan ini menjelaskan mengapa saya membuatnya dan keputusan apa saja yang saya ambil di sepanjang jalan.

## Berawal dari foto properti

Saya menjalankan perusahaan properti di Jepang. Kami memotret properti yang kami tawarkan lalu menayangkannya. Saya ingin siap menghadapi hari ketika seseorang mengubah salah satu foto itu atau memasangnya di situs lain, sehingga saya bisa menunjukkan bahwa foto aslinya milik kami dan sudah ada lebih dulu.

File aslinya ada di tangan saya, dan unggahan saya punya tanggal terbit. Tetapi semua itu bisa saya ubah sendiri, dan siapa pun yang memegang salinannya bisa mengklaim tanggal yang sama. Yang saya perlukan adalah tanggal yang ditulis oleh **pihak selain saya**, dalam bentuk yang **tidak bisa diubah siapa pun sesudahnya**.

## Yang pertama saya temukan

Saya menelusuri apa yang tersedia di Jepang per November 2026.

- **Tanggal pasti dari notaris.** 700 yen per dokumen. Ada versi elektroniknya, tetapi hanya menerima file teks, PDF, dan XML sampai 10 MB, dan prosesnya berjalan pada hari kerja.
- **Pendaftaran di Badan Urusan Kebudayaan Jepang.** 3.000 yen per ciptaan, diajukan di atas kertas, satu ciptaan setiap kali. Hasilnya, ciptaan dianggap diterbitkan pada tanggal yang didaftarkan.
- **Tanda waktu dari penyedia yang diakreditasi Kementerian Dalam Negeri dan Komunikasi Jepang.** Inilah yang punya kedudukan resmi di Jepang. Tarifnya kebanyakan ditujukan untuk perusahaan.
- **Layanan pencatatan berbasis blockchain.** Yang saya temukan ditujukan untuk bisnis, atau berbayar.
- **Tanda tangan di dalam kamera (C2PA).** Sebagian kamera menandatangani foto saat diambil. Itu menunjukkan dari mana sebuah file berasal, pertanyaan yang berbeda dari kapan file itu ada.

Semuanya berguna, dan untuk satu karya yang benar-benar harus Anda lindungi, sebaiknya gunakan cara-cara itu. Tetapi membayar dan mengajukan permohonan untuk setiap foto atau artikel baru tidaklah realistis. Yang saya inginkan adalah sesuatu yang **gratis, tanpa pendaftaran akun, tanpa mengunggah apa pun, disimpan di tempat yang bahkan tidak bisa diubah oleh pengelolanya, dan berjalan otomatis di WordPress setiap kali terbit**. Saya tidak menemukannya, jadi saya membuatnya.

## Aturan yang saya tetapkan

### Tidak mengambil apa pun selain hash

DateSealed hanya menerima hash SHA-256 dari file atau teks Anda, yaitu "sidik jari" sepanjang 64 karakter. Hash dihitung di browser Anda, jadi foto dan naskah Anda tidak pernah meninggalkan komputer Anda. Karya yang belum terbit justru yang paling ingin dicatat orang; kalau harus diserahkan dulu supaya bisa dicatat, tujuannya jadi hilang.

### Anda tidak perlu memercayai saya

Setiap catatan mendapat dua tanggal. Yang pertama adalah tanda waktu RFC 3161 yang ditandatangani otoritas tanda waktu milik DateSealed sendiri, dan langsung dikembalikan. Yang kedua ditambatkan ke sebuah blok Bitcoin melalui OpenTimestamps, biasanya dalam beberapa jam.

Tanggal pertama hanya bisa dipercaya sejauh Anda memercayai saya. Tanggal kedua bukan wewenang saya untuk diubah. Setelah tertambat, Anda bisa memeriksa tanggalnya hanya dengan file bukti (`.ots`) dan buku besar Bitcoin, bahkan jika DateSealed sudah tidak ada. Setiap halaman catatan memuat perintah untuk memverifikasinya di komputer Anda sendiri.

Kunci akar otoritas tanda waktu itu saya buat di komputer saya sendiri dan saya simpan terenkripsi dengan frasa sandi. Server hanya memegang kunci penandatanganan.

### Tidak menghapus, tidak mengubah

Bahkan layar admin pun tidak punya cara untuk menghapus catatan atau mengubah hash dan waktunya. Buku catatan hanya bernilai jika pengelolanya tidak bisa menyentuhnya. Ketika Anda memperbarui tulisan, catatan lama tetap ada dan catatan baru ditambahkan. Plugin WordPress mengikuti aturan yang sama.

### Menyebutkan sejak awal apa yang tidak bisa dilakukan

Catatan menunjukkan bahwa data yang cocok dengan hash itu sudah ada pada waktu tersebut. Tidak lebih. Catatan tidak menunjukkan bahwa Anda pembuatnya, bahwa Anda pemiliknya, atau bahwa isinya benar, dan **tidak menjamin akibat hukum apa pun**. Saya menuliskannya di banyak tempat di situs ini, karena harapan yang keliru adalah awal orang dirugikan.

### Terus terang soal apa yang dikumpulkan

Untuk mencegah penyalahgunaan, menerapkan batas, mencari galat, dan memahami penggunaan, setiap pemakaian dicatat beserta alamat IP dan beberapa keterangan lain. Data itu tidak dipakai untuk iklan dan tidak dijual. Alamat IP dan nama host disimpan di server ini selama 30 hari, lalu dipindahkan ke penyimpanan terpisah yang saya kelola paling lama 13 bulan, dan setelah itu bagian akhir alamatnya dihapus sehingga yang tersisa hanya statistik. Rinciannya ada di [ketentuan](/id/terms).

## Untuk siapa saja

Gratis dan tidak perlu akun. Antarmukanya tersedia dalam 20 bahasa. Ada juga stempel untuk foto, cara mencatat URL yang sudah terbit, API, dan plugin WordPress. Plugin bisa [diunduh dari halaman API](/api#wordpress); pendaftarannya di wordpress.org sedang ditinjau.

Cara memakainya untuk foto dan naskah Anda, termasuk kaitannya dengan pencatatan ciptaan di Indonesia, ada di "[Cara menunjukkan bahwa Anda yang membuatnya lebih dulu](/id/column/prove-you-made-it-first)".

## Beri tahu saya di mana yang tersendat

Saya ingin mendengar di bagian mana DateSealed merepotkan dan apa yang Anda harapkan berikutnya, terutama dari fotografer dan blogger yang pernah terlibat sengketa "siapa yang lebih dulu". Kontak ada di bagian bawah halaman.
