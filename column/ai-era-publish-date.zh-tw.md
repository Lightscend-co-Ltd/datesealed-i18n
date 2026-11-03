title: 發布日期是自己說了算：AI 時代替部落格留一個改不了的日期
description: 現在改寫、複製一篇文章只要片刻，CMS 上的發布日期本身證明不了誰先誰後。這裡介紹怎樣在每次發布時留下第三方日期、怎樣在 WordPress 上自動完成，以及這種紀錄的極限。
date: 2026-11-03
author: 中澤祐樹 (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
假設你發文的隔天早上，出現一篇幾乎一樣的文章：段落換了順序，說法改了一下，骨架完全相同。你要怎麼證明自己的在先？

## 改寫變得很便宜

改寫、調整結構、翻成別的語言，過去要花人的時間，現在交給語言模型，一下子就好了。下面這些數字說明，機器寫、機器讀的內容已經很普遍。

| 來源 | 發現 |
|---|---|
| Imperva《2025 惡意機器人報告》 | 2024 年網路流量有 51% 來自自動程式，惡意機器人占 37%，比前一年的 32% 高[^imperva] |
| Cloudflare（2025 年 7 月） | 在其網路上，GPTBot 的請求量從 2024 年 5 月到 2025 年 5 月成長 305%[^cf1] |
| Cloudflare（2025 年 8 月） | 過去一年的 AI 爬取中，約 80% 是為了訓練模型[^cf2] |
| NewsGuard | 幾乎沒有人工把關、發布 AI 生成內容的新聞網站：2023 年 5 月有 49 個，2026 年 6 月達 3,749 個[^newsguard] |
| Ahrefs（2025 年 5 月） | 2025 年 4 月首次發布的 90 萬個網頁中，74.2% 含有 AI 生成的內容[^ahrefs] |
| NeurIPS 2023 論文 | 經過改寫模型處理後，某個 AI 文字偵測器的準確率從 70.3% 降到 4.6%[^neurips] |

這些是廠商或研究者各用不同方法做出的估計，都不是「你的文章被抄的機率」。但它們說明，改寫很容易，也很難看出來。

台灣立法院在 2025 年 12 月 23 日三讀通過《人工智慧基本法》；依數位發展部的說明，其中包括對人工智慧的產出做適當資訊揭露或標記的內容。[^moda] 不過標記是針對 AI 產出的要求，不能替你證明你的文章在先。

## 發布日期是自己說了算

發布日期是你自己決定的。WordPress 可以用過去的日期發布，也可以改已發布文章的日期。[^wp] 對方網站的日期一樣是自己決定的，兩邊都說「我先」，什麼也解決不了。網頁典藏有幫助，但它什麼時候、會不會收錄你的頁面，你控制不了。

你需要的是：**在發布的當下**，由**你以外的人**記下日期，放在**事後誰都改不了**的地方。

## DateSealed 做什麼

- 只接收文章的 **SHA-256 雜湊值**，在你的瀏覽器裡計算（用 WordPress 外掛時在你自己的伺服器上計算）。內文不會送出。
- 替雜湊值加上馬上傳回的 **RFC 3161 時間戳記**，以及透過 OpenTimestamps 在幾小時內寫入的**比特幣紀錄**。
- 誰都無法事後在比特幣帳本裡補寫時間。寫入之後，就算 DateSealed 不在了，只憑證明檔和帳本也能核對日期。

更多說明請見〈[怎樣證明是你先做出來的](/zh-tw/column/prove-you-made-it-first)〉和〈[我為什麼做 DateSealed](/zh-tw/column/why-i-built-datesealed)〉。

## WordPress 上自動完成

要靠記性維持的習慣，忙一個禮拜就斷了。DateSealed 的 WordPress 外掛：

- 每次發布和更新時，在你的伺服器上計算內文的雜湊值，只送出雜湊值；
- 每次更新都**新增一筆紀錄**，第一次發布的紀錄不會被覆蓋，修訂的歷程會累積下來；
- 可以顯示一個連到紀錄頁的標記（可選）；
- 需要 WordPress 5.8 以上、PHP 8.2 以上。

從 [API 頁面下載](/api#wordpress)，然後在 WordPress 後台進入 *Plugins → Add New → Upload Plugin*，啟用後打開 *Settings → DateSealed*。在 wordpress.org 上架還在審查中。

## 紀錄不說明什麼

- 不說明文章是人寫的還是模型寫的。
- 不說明內容正確或具有原創性，不說明是誰寫的、歸誰所有。
- **不保證法律效力。** 在台灣，著作權登記制度已經廢除，著作完成的時間要由作者自己舉證；[^tipo] DateSealed 的紀錄可以是其中一份材料，但它不是公證或認證。

「在這個時間已經存在」，是開始溝通的好起點，但它本身不能了結爭議。請把紀錄當作一份證據，和其他證據擺在一起用。

## 讓紀錄有用的幾個習慣

1. **留好原文。** DateSealed 只有雜湊值。
2. **留好證明檔。** 把 `.tsr` 和 `.ots` 和原文放在一起，不靠 DateSealed 也能驗證。
3. **發布時就記錄。** 紀錄的時間就是你記錄的時間，每晚一天，證據就弱一分。
4. **不要誇大它。** 真正要爭的事，再搭配智慧財產局建議的方法，例如保留創作過程的資料、請公證人認證或請律師出具證明。[^tipo]

[^imperva]: Imperva, "2025 Imperva Bad Bot Report"（2025 年 4 月 15 日，依 Imperva 網路資料） <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare 部落格（2025 年 7 月 1 日） <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare 部落格（2025 年 8 月 29 日） <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?"（2025 年 5 月 19 日，使用 Ahrefs 自己的偵測器，該公司也說明並不完美） <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna 等, "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^moda]: 數位發展部新聞稿〈立法院三讀通過《人工智慧基本法》 構築我國AI創新與安全治理基石〉（2025 年 12 月 24 日） <https://moda.gov.tw/press/press-releases/18316>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^tipo]: 經濟部智慧財產局著作權主題網〈著作人舉證責任及方法〉（2025 年 5 月更新） <https://www.tipo.gov.tw/tw/copyright/696-21213.html>
