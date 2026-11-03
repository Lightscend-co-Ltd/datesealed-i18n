title: 发布日期只是自己说了算：AI 时代给博客留一个改不了的日期
description: 如今改写、复制一篇文章只要片刻，CMS 上的发布日期本身证明不了谁先谁后。这里介绍怎样在每次发布时留下第三方日期、怎样在 WordPress 上自动完成，以及这种记录的局限。
date: 2026-11-03
author: 中澤祐樹 (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
假设你发文的第二天早上，出现了一篇几乎一样的文章：段落换了顺序，说法改了改，骨架完全相同。你要怎样证明自己的在先？

## 改写变得很便宜

改写、调整结构、翻译成别的语言，过去要花人的时间，现在交给语言模型片刻就完成了。下面这些数字说明，机器写、机器读的内容已经很常见。

| 来源 | 发现 |
|---|---|
| Imperva《2025 恶意机器人报告》 | 2024 年网络流量的 51% 来自自动程序，恶意机器人占 37%，比上一年的 32% 有所上升[^imperva] |
| Cloudflare（2025 年 7 月） | 在其网络上，GPTBot 的请求量从 2024 年 5 月到 2025 年 5 月增长了 305%[^cf1] |
| Cloudflare（2025 年 8 月） | 过去一年的 AI 抓取中，约 80% 用于模型训练[^cf2] |
| NewsGuard | 几乎没有人工把关、发布 AI 生成内容的新闻网站：2023 年 5 月为 49 个，到 2026 年 6 月为 3,749 个[^newsguard] |
| Ahrefs（2025 年 5 月） | 2025 年 4 月首次发布的 90 万个网页中，74.2% 含有 AI 生成的内容[^ahrefs] |
| NeurIPS 2023 论文 | 经过改写模型处理后，某 AI 文本检测器的准确率从 70.3% 降到 4.6%[^neurips] |

这些是厂商或研究者各自用不同方法得出的估计，都不是“你的文章被抄的概率”。但它们说明，改写很容易，也很难被发现。

在中国，《人工智能生成合成内容标识办法》自 2025 年 9 月 1 日起施行，要求服务提供者给 AI 生成合成的内容加上显式标识和隐式标识。[^cac] 不过标识是对 AI 内容的要求，它不能替你证明你的文章在先。

## 发布日期只是自己说了算

发布日期是你自己定的。WordPress 允许用过去的日期发布，也允许修改已发布文章的日期。[^wp] 对方网站的日期同样是自己定的，两边都说“我先”，什么也解决不了。网页存档有帮助，但它什么时候、会不会收录你的页面，你控制不了。

你需要的是：**在发布的那一刻**，由**你以外的人**记下日期，放在**事后谁都改不了**的地方。

## DateSealed 做什么

- 只接收文章的 **SHA-256 哈希值**，在你的浏览器里计算（用 WordPress 插件时在你自己的服务器上计算）。正文不会被发送。
- 给哈希值附上马上返回的 **RFC 3161 时间戳**，以及通过 OpenTimestamps 在几小时内写入的**比特币记录**。
- 谁都不能事后往比特币账本里补写时间。写入之后，即使 DateSealed 不在了，只凭证明文件和账本也能核对日期。

更多说明见《[怎样证明是你先做出来的](/zh/column/prove-you-made-it-first)》和《[我为什么做 DateSealed](/zh/column/why-i-built-datesealed)》。

## WordPress 上自动完成

要靠记性坚持的习惯，忙起来一周就断了。DateSealed 的 WordPress 插件：

- 每次发布和更新时，在你的服务器上计算正文的哈希值，只发送哈希值；
- 每次更新都**追加一条新记录**，首次发布的记录不会被覆盖，修改的历史会积累下来；
- 可以显示一个链接到记录页的标记（可选）；
- 需要 WordPress 5.8 以上、PHP 8.2 以上。

从 [API 页面下载](/api#wordpress)，然后在 WordPress 后台进入 *Plugins → Add New → Upload Plugin*，启用后打开 *Settings → DateSealed*。在 wordpress.org 上架还在审核中。

## 记录不说明什么

- 不说明文章是人写的还是模型写的。
- 不说明内容准确或具有独创性，不说明是谁写的、归谁所有。
- **不保证法律效力。** 在中国，《人民法院在线诉讼规则》规定法院可以认定经技术核验一致的区块链数据上链后未经篡改，同时会审查存证平台是否符合国家有关部门的规定，上链前的真实性也要另行证明。[^online] DateSealed 不是按照中国有关规定设立的电子存证平台。

“在这个时间已经存在”，是开始沟通的一个好起点，但它本身不能了结争议。请把记录当作一份证据，和其他证据放在一起用。

## 让记录有用的几个习惯

1. **留好原文。** DateSealed 只有哈希值。
2. **留好证明文件。** 把 `.tsr` 和 `.ots` 和原文放在一起，不靠 DateSealed 也能验证。
3. **发布时就记录。** 记录的时间就是你记录的时间，每晚一天，证据就弱一分。
4. **不要夸大它。** 真正要争的事，再配合作品登记、公证或符合规定的电子存证。

[^imperva]: Imperva, "2025 Imperva Bad Bot Report"（2025 年 4 月 15 日，基于 Imperva 网络数据） <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare 博客（2025 年 7 月 1 日） <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare 博客（2025 年 8 月 29 日） <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?"（2025 年 5 月 19 日，使用 Ahrefs 自己的检测器，其本身也说明并不完美） <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna 等, "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^cac]: 国家互联网信息办公室《〈人工智能生成合成内容标识办法〉答记者问》（2025 年 3 月 14 日） <https://www.cac.gov.cn/2025-03/14/c_1743654685896173.htm>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^online]: 《人民法院在线诉讼规则》（法释〔2021〕12号，2021 年 8 月 1 日起施行）第十六条至第十八条 <https://www.court.gov.cn/fabu/xiangqing/309551.html>
