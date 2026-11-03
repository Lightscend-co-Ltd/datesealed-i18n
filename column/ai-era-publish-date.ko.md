title: 게시일은 내가 적어 넣은 날짜일 뿐: AI 시대, 블로그에 아무도 고칠 수 없는 날짜 남기기
description: 글을 바꿔 쓰고 다시 올리는 일이 금방 끝나는 지금, CMS 게시일만으로는 누가 먼저인지 보여 줄 수 없습니다. 글마다 제3자의 날짜를 남기는 방법, WordPress에서 자동으로 하는 법, 그리고 그 한계를 정리했습니다.
date: 2026-11-03
author: 나카자와 유키 (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
글을 올린 다음 날 아침, 거의 똑같은 글이 나타났다고 해 봅시다. 문단 순서를 바꾸고 표현만 손봤을 뿐, 뼈대는 그대로입니다. 내 글이 먼저였다는 것을 무엇으로 보여 줄 수 있을까요?

## 바꿔 쓰기에 드는 비용이 거의 없어졌다

다른 말로 바꾸기, 구성 바꾸기, 다른 언어로 옮기기는 예전에는 사람의 시간이 들던 일입니다. 지금은 언어 모델이 순식간에 해냅니다. 기계가 쓰고 기계가 읽는 콘텐츠가 이미 얼마나 흔한지 숫자로 보면 이렇습니다.

| 출처 | 내용 |
|---|---|
| Imperva, 2025 Bad Bot Report | 2024년 웹 트래픽의 51%가 자동화된 것이었고, 악성 봇이 37%로 전년 32%에서 늘었다[^imperva] |
| Cloudflare(2025년 7월) | 자사 네트워크에서 GPTBot 요청이 2024년 5월부터 2025년 5월까지 305% 늘었다[^cf1] |
| Cloudflare(2025년 8월) | 지난 1년간 AI 크롤링의 약 80%가 모델 학습용이었다[^cf2] |
| NewsGuard | 사람의 관리 없이 AI 생성 콘텐츠를 내는 뉴스 사이트: 2023년 5월 49곳에서 2026년 6월 3,749곳으로[^newsguard] |
| Ahrefs(2025년 5월) | 2025년 4월에 처음 공개된 페이지 90만 개 가운데 74.2%에 AI가 만든 부분이 있었다[^ahrefs] |
| NeurIPS 2023 논문 | 바꿔 쓰기 모델을 거치자 AI 글 탐지기의 정확도가 70.3%에서 4.6%로 떨어졌다[^neurips] |

모두 업체나 연구자가 각자의 방법으로 낸 추정치이고, "내 글이 베껴질 확률"을 뜻하지는 않습니다. 그래도 바꿔 쓰기가 쉽고, 알아보기 어렵다는 것은 보여 줍니다.

한국에서는 2026년 1월 22일 시행된 인공지능기본법이 생성형 AI를 활용한 제품·서비스를 제공하는 사업자에게 결과물에 그 사실을 표시하도록 했습니다(과기정통부는 최소 1년 이상 규제를 유예한다고 밝혔습니다).[^msit] 다만 이 표시는 AI 결과물에 대한 의무이고, 내 글이 먼저였다는 것을 대신 증명해 주지는 않습니다.

## 게시일은 내가 적어 넣은 날짜일 뿐

게시일은 내가 정합니다. WordPress에서는 과거 날짜로 게시할 수도, 이미 게시한 글의 날짜를 바꿀 수도 있습니다.[^wp] 상대 사이트의 날짜도 마찬가지로 자기가 적어 넣은 것입니다. 서로 "내가 먼저"라고 해 봐야 결론이 나지 않습니다. 웹 아카이브가 도움이 되지만, 내 페이지를 언제 저장할지, 저장하기는 할지는 내가 정할 수 없습니다.

필요한 것은 **게시하는 그 순간에**, **내가 아닌 누군가가** 날짜를 적어 **나중에 아무도 고칠 수 없는 곳**에 두는 것입니다.

## DateSealed가 하는 일

- 글의 **SHA-256 해시**만 받습니다. 계산은 브라우저 안에서(WordPress 플러그인이라면 내 서버에서) 하고, 본문은 보내지 않습니다.
- 해시에 바로 돌아오는 **RFC 3161 타임스탬프**와, 몇 시간 안에 새겨지는 **비트코인 기록**(OpenTimestamps)을 붙입니다.
- 비트코인 원장에 나중에 시각을 끼워 넣을 수는 없습니다. 새겨진 뒤에는 DateSealed가 사라져도 증명 파일과 원장만으로 날짜를 확인할 수 있습니다.

자세한 설명은 「[먼저 만든 사람이 나라는 것을 보여 주려면](/ko/column/prove-you-made-it-first)」과 「[DateSealed를 만든 이유](/ko/column/why-i-built-datesealed)」에 있습니다.

## WordPress에서는 자동으로

기억에 의존하는 습관은 바쁜 한 주를 넘기지 못합니다. DateSealed WordPress 플러그인은 다음과 같이 동작합니다.

- 글을 게시·수정할 때마다 내 서버에서 본문의 해시를 계산해 해시만 보냅니다.
- 수정할 때마다 **새 기록을 추가**하므로 처음 게시한 기록은 덮어쓰이지 않고, 수정 이력이 쌓입니다.
- 기록 페이지로 연결되는 배지를 표시할 수 있습니다(선택).
- WordPress 5.8 이상, PHP 8.2 이상에서 동작합니다.

[API 페이지에서 내려받은](/api#wordpress) 뒤, WordPress 관리 화면의 *Plugins → Add New → Upload Plugin*에서 올려 활성화하고 *Settings → DateSealed*를 엽니다. wordpress.org 등록은 심사 중입니다.

## 기록이 말해 주지 않는 것

- 글을 사람이 썼는지 모델이 썼는지는 보여 주지 않습니다.
- 내용이 정확하거나 독창적인지, 누가 썼는지, 누구에게 권리가 있는지도 보여 주지 않습니다.
- **법적 효력은 보장하지 않습니다.** 한국에서 법률에 근거한 제도로는 창작연월일 등을 추정해 주는 한국저작권위원회의 저작권 등록,[^kcc] 원본을 내보이지 않고 보유 사실과 시점을 증명하는 영업비밀 원본증명[^kipo] 등이 있습니다. DateSealed는 그 어느 것도 아닙니다.

"그 시각에 존재했다"는 사실은 대화를 시작하기에 좋은 출발점입니다. 그것만으로 다툼이 끝나지는 않습니다. 기록은 다른 증거와 나란히 놓는 증거 중 하나로 쓰세요.

## 기록을 쓸모 있게 만드는 습관

1. **원본을 보관한다.** DateSealed에 있는 것은 해시뿐입니다.
2. **증명 파일을 보관한다.** `.tsr`와 `.ots`를 원본과 함께 두면 DateSealed 없이도 검증할 수 있습니다.
3. **게시할 때 기록한다.** 기록의 시각은 기록한 시각입니다. 하루 늦을수록 증거는 약해집니다.
4. **과하게 기대하지 않는다.** 정말 다툴 일에는 저작권 등록 같은 공적인 제도를 함께 쓰세요.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report"(2025년 4월 15일, Imperva 네트워크 데이터) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Cloudflare 블로그(2025년 7월 1일) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Cloudflare 블로그(2025년 8월 29일) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?"(2025년 5월 19일, Ahrefs 자체 탐지기 기준이며 완벽하지 않다고 밝힘) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna 외, "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^msit]: 대한민국 정책브리핑(과학기술정보통신부) 「'인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무」(2026년 1월 21일) <https://www.korea.kr/news/policyNewsView.do?newsId=148958380>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^kcc]: 한국저작권위원회 「저작권 등록」 안내 <https://www.copyright.or.kr/business/registration/index.do>
[^kipo]: 특허청 보도자료 「영업비밀 원본증명서비스, 민간기관에서도 이용 가능」(2025년 1월 20일) <https://www.kipo.go.kr/ko/kpoBultnDetail.do?menuCd=SCD0200618&ntatcSeq=20382&aprchId=BUT0000029&sysCd=SCD02>
