title: Tanggal Terbit Anda Hanyalah Pengakuan Sendiri: Menyimpan Tanggal yang Tak Bisa Diubah di Era AI
description: Menulis ulang artikel kini sekejap, dan tanggal CMS tidak membuktikan apa-apa. Cara memberi tiap tulisan tanggal dari pihak ketiga dan mengotomatiskannya di WordPress.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Bayangkan, pagi setelah Anda menerbitkan tulisan, muncul tulisan yang hampir sama: paragrafnya diacak, kalimatnya diganti, kerangkanya persis. Bagaimana Anda menunjukkan bahwa tulisan Anda yang lebih dulu?

## Menulis ulang kini murah

Memparafrasekan, menyusun ulang, dan menerjemahkan dulu memakan waktu manusia. Sekarang model bahasa mengerjakannya dalam sekejap. Angka-angka berikut menunjukkan betapa umumnya konten yang ditulis dan dibaca mesin.

| Sumber | Temuan |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% lalu lintas web pada 2024 bersifat otomatis; bot jahat 37%, naik dari 32%[^imperva] |
| Cloudflare, Juli 2025 | Permintaan GPTBot di jaringannya naik 305% dari Mei 2024 ke Mei 2025[^cf1] |
| Cloudflare, Agustus 2025 | Sekitar 80% perayapan AI selama setahun terakhir untuk melatih model[^cf2] |
| NewsGuard | Situs berita yang menerbitkan konten buatan AI dengan sedikit pengawasan manusia: 49 pada Mei 2023, 3.749 pada Juni 2026[^newsguard] |
| Ahrefs, Mei 2025 | 74,2% dari 900.000 halaman yang pertama terbit pada April 2025 mengandung konten buatan AI[^ahrefs] |
| Makalah NeurIPS 2023 | Model parafrase menurunkan akurasi pendeteksi teks AI dari 70,3% menjadi 4,6%[^neurips] |

Ini perkiraan vendor dan peneliti, masing-masing dengan metodenya sendiri, dan tidak satu pun menyatakan peluang tulisan *Anda* dijiplak. Yang terlihat: menulis ulang itu mudah dan sulit dideteksi.

## Tanggal terbit Anda hanyalah pengakuan sendiri

Anda yang memilih tanggal terbit. WordPress memungkinkan Anda menerbitkan dengan tanggal mundur dan mengubah tanggal tulisan yang sudah tayang.[^wp] Tanggal di situs lain juga sama-sama pengakuan sendiri, jadi dua orang yang sama-sama berkata "saya lebih dulu" tidak menyelesaikan apa pun. Arsip web membantu, tetapi Anda tidak bisa menentukan apakah atau kapan halaman Anda diarsipkan.

Yang Anda perlukan adalah **pihak selain Anda** yang menuliskan tanggalnya **saat Anda menerbitkan**, di tempat yang **tidak bisa diubah siapa pun sesudahnya**.

## Apa yang dilakukan DateSealed

- Hanya menerima **hash SHA-256** tulisan Anda, yang dihitung di browser Anda (atau di server Anda sendiri bila memakai plugin WordPress). Teksnya tidak pernah dikirim.
- Memberikan **tanda waktu RFC 3161** yang langsung dikembalikan, dan **catatan Bitcoin** melalui OpenTimestamps yang tertambat dalam beberapa jam.
- Tidak ada yang bisa menuliskan waktu ke buku besar Bitcoin belakangan. Setelah tertambat, tanggalnya bisa diperiksa hanya dengan file bukti dan buku besar itu, bahkan jika DateSealed sudah tidak ada.

Penjelasan lebih lengkap ada di "[Cara menunjukkan bahwa Anda yang membuatnya lebih dulu](/id/column/prove-you-made-it-first)" dan "[Mengapa saya membuat DateSealed](/id/column/why-i-built-datesealed)".

## Otomatis di WordPress

Kebiasaan yang harus diingat-ingat tidak akan bertahan di minggu yang sibuk. Plugin WordPress DateSealed:

- menghitung hash teks tulisan di server Anda setiap kali terbit dan diperbarui, dan hanya mengirim hash;
- **menambahkan catatan baru** untuk setiap pembaruan, sehingga penerbitan pertama tidak pernah tertimpa dan riwayat revisi terus bertambah;
- bisa menampilkan lencana yang menautkan ke halaman catatan (opsional);
- memerlukan WordPress 5.8+ dan PHP 8.2+.

[Unduh dari halaman API](/api#wordpress), lalu di WordPress buka *Plugins → Add New → Upload Plugin*, aktifkan, dan buka *Settings → DateSealed*. Pendaftaran di wordpress.org sedang ditinjau.

## Yang tidak dikatakan catatan

- Tidak menunjukkan apakah teks ditulis manusia atau model.
- Tidak menunjukkan bahwa isinya benar atau orisinal, siapa penulisnya, atau siapa pemiliknya.
- **Tidak menjamin akibat hukum apa pun.** Di Indonesia, Peraturan Menteri Kominfo Nomor 11 Tahun 2022 mengatur penanda waktu elektronik tersertifikasi yang diselenggarakan melalui PSrE Indonesia;[^pm11] di Uni Eropa, kedudukan khusus dimiliki tanda waktu elektronik berkualifikasi.[^eidas] Catatan DateSealed bukan keduanya.

"Ini sudah ada pada waktu itu" adalah awal yang baik untuk sebuah pembicaraan. Kalimat itu tidak akan menyelesaikan sengketa sendirian. Pakai catatan sebagai satu bukti di samping bukti lainnya.

## Kebiasaan yang membuat catatan berharga

1. **Simpan file aslinya.** DateSealed hanya memegang hash.
2. **Simpan file buktinya.** Simpan `.tsr` dan `.ots` bersama file asli agar bisa diverifikasi tanpa DateSealed.
3. **Catat saat menerbitkan.** Waktu catatan adalah saat Anda membuatnya; setiap hari penundaan melemahkannya.
4. **Jangan membesar-besarkannya.** Untuk perkara yang penting, tambahkan pencatatan ciptaan di DJKI atau penanda waktu tersertifikasi.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (15 April 2025; data jaringan Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog Cloudflare (1 Juli 2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog Cloudflare (29 Agustus 2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (19 Mei 2025; detektor milik Ahrefs sendiri, yang diakuinya tidak sempurna) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^pm11]: Peraturan Menteri Komunikasi dan Informatika Nomor 11 Tahun 2022 tentang Tata Kelola Penyelenggaraan Sertifikasi Elektronik <https://jdih.komdigi.go.id/produk_hukum/view/id/833/t/peraturan+menteri+komunikasi+dan+informatika+nomor+11+tahun+2022>
[^eidas]: Regulasi eIDAS (EU) No 910/2014, Pasal 41(2) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
