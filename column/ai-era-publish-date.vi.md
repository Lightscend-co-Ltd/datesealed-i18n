title: Ngày đăng bài chỉ là lời tự khai: giữ một mốc ngày không ai sửa được trong thời AI
description: Viết lại một bài giờ chỉ mất vài giây, và ngày trên CMS không chứng minh được gì. Cách gắn ngày của bên thứ ba cho mọi bài viết và tự động hóa trên WordPress.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/03/datesealed_one_date_ai_cannot_backdate_en/
---
Giả sử sáng hôm sau ngày bạn đăng bài, xuất hiện một bài gần như y hệt: đoạn văn đảo thứ tự, câu chữ đổi đi, bộ khung giữ nguyên. Bạn sẽ chỉ ra bài của mình có trước bằng cách nào?

## Viết lại đã trở nên rẻ

Diễn đạt lại, sắp xếp lại, dịch lại trước đây tốn thời gian của con người. Giờ một mô hình ngôn ngữ làm việc đó trong chốc lát. Các con số cho thấy nội dung do máy viết và máy đọc đã phổ biến đến mức nào.

| Nguồn | Kết quả |
|---|---|
| Imperva, 2025 Bad Bot Report | 51% lưu lượng web năm 2024 là tự động; bot độc hại chiếm 37%, tăng từ 32%[^imperva] |
| Cloudflare, tháng 7/2025 | Lượng yêu cầu của GPTBot trên mạng lưới của họ tăng 305% từ tháng 5/2024 đến tháng 5/2025[^cf1] |
| Cloudflare, tháng 8/2025 | Khoảng 80% hoạt động thu thập dữ liệu của AI trong năm qua là để huấn luyện mô hình[^cf2] |
| NewsGuard | Số trang tin đăng nội dung do AI tạo với rất ít giám sát của con người: 49 vào tháng 5/2023, 3.749 vào tháng 6/2026[^newsguard] |
| Ahrefs, tháng 5/2025 | 74,2% trong 900.000 trang đăng lần đầu vào tháng 4/2025 có chứa nội dung do AI tạo[^ahrefs] |
| Bài báo NeurIPS 2023 | Một mô hình diễn đạt lại làm độ chính xác của công cụ phát hiện văn bản AI giảm từ 70,3% xuống 4,6%[^neurips] |

Đây là ước tính của các công ty và nhà nghiên cứu, mỗi bên một phương pháp, và không con số nào là xác suất bài *của bạn* bị sao chép. Chúng cho thấy việc viết lại thì dễ, còn phát hiện thì khó.

## Ngày đăng bài chỉ là lời tự khai

Ngày đăng do bạn chọn. WordPress cho phép đăng với ngày trong quá khứ và đổi ngày của bài đã đăng.[^wp] Ngày trên trang kia cũng là lời tự khai như vậy, nên hai người cùng nói "tôi có trước" thì chẳng giải quyết được gì. Các kho lưu trữ web có giúp ích, nhưng bạn không quyết định được họ có lưu trang của bạn hay lưu vào lúc nào.

Điều bạn cần là **người khác ngoài bạn** ghi lại ngày **ngay khi bạn đăng**, ở nơi **không ai sửa được về sau**.

## DateSealed làm gì

- Chỉ nhận **mã băm SHA-256** của bài viết, được tính trong trình duyệt của bạn (hoặc trên máy chủ của bạn nếu dùng plugin WordPress). Văn bản không bao giờ được gửi đi.
- Gắn một **dấu thời gian RFC 3161** trả về ngay, và một **bản ghi Bitcoin** qua OpenTimestamps, được neo trong vài giờ.
- Không ai có thể ghi lùi thời gian vào sổ cái Bitcoin. Sau khi neo, thời điểm có thể được kiểm tra chỉ bằng tệp bằng chứng và sổ cái, kể cả khi DateSealed không còn.

Chi tiết hơn có trong "[Làm sao chứng tỏ bạn là người làm ra trước](/vi/column/prove-you-made-it-first)" và "[Vì sao tôi làm DateSealed](/vi/column/why-i-built-datesealed)".

## Tự động trên WordPress

Một thói quen phải tự nhớ sẽ không trụ nổi qua một tuần bận rộn. Plugin WordPress của DateSealed:

- tính mã băm nội dung bài viết trên máy chủ của bạn mỗi lần đăng và cập nhật, và chỉ gửi mã băm;
- **thêm một bản ghi mới** cho mỗi lần cập nhật, nên lần đăng đầu tiên không bao giờ bị ghi đè và lịch sử chỉnh sửa cứ thế tích lũy;
- có thể hiển thị huy hiệu liên kết tới trang bản ghi (tùy chọn);
- cần WordPress 5.8 trở lên và PHP 8.2 trở lên.

[Tải từ trang API](/api#wordpress), rồi trong WordPress vào *Plugins → Add New → Upload Plugin*, kích hoạt và mở *Settings → DateSealed*. Việc đưa lên wordpress.org đang được xét duyệt.

## Những điều bản ghi không nói

- Không cho biết văn bản do người hay do mô hình viết.
- Không cho biết nội dung đúng hay là sáng tạo riêng, ai viết, hay ai sở hữu.
- **Không bảo đảm hiệu lực pháp lý.** Ở Việt Nam, dịch vụ cấp dấu thời gian là dịch vụ tin cậy, do tổ chức có giấy phép kinh doanh dịch vụ tin cậy của cơ quan quản lý nhà nước cung cấp;[^gddt] ở Liên minh châu Âu, vị thế đặc biệt thuộc về dấu thời gian điện tử đủ điều kiện (qualified).[^eidas] Bản ghi DateSealed không thuộc loại nào trong số đó.

"Nó đã tồn tại vào lúc này" là điểm khởi đầu tốt cho một cuộc trao đổi. Tự nó sẽ không giải quyết được tranh chấp. Hãy dùng bản ghi như một chứng cứ đặt cạnh những chứng cứ khác.

## Những thói quen làm bản ghi có giá trị

1. **Giữ tệp gốc.** DateSealed chỉ giữ mã băm.
2. **Giữ tệp bằng chứng.** Cất `.tsr` và `.ots` cùng tệp gốc để có thể tự kiểm tra mà không cần DateSealed.
3. **Ghi lại ngay lúc đăng.** Thời điểm của bản ghi là lúc bạn tạo nó; mỗi ngày chậm trễ làm nó yếu đi.
4. **Đừng thổi phồng nó.** Với việc quan trọng, hãy thêm đăng ký quyền tác giả hoặc dấu thời gian của tổ chức được cấp phép.

[^imperva]: Imperva, "2025 Imperva Bad Bot Report" (15/4/2025; dữ liệu mạng lưới Imperva) <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>
[^cf1]: Blog Cloudflare (1/7/2025) <https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/>
[^cf2]: Blog Cloudflare (29/8/2025) <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>
[^newsguard]: NewsGuard, "AI Tracking Center" <https://www.newsguardtech.com/special-reports/ai-tracking-center>
[^ahrefs]: Ahrefs, "What Percentage of New Content Is AI-Generated?" (19/5/2025; công cụ phát hiện riêng của Ahrefs, được chính họ thừa nhận là chưa hoàn hảo) <https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/>
[^neurips]: Krishna et al., "Paraphrasing evades detectors of AI-generated text", NeurIPS 2023 <https://proceedings.neurips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html>
[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^gddt]: Văn phòng Quốc hội, văn bản hợp nhất Luật Giao dịch điện tử (2026), Điều 28 và 31 <https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/154-vbhn-vpqh.signed.pdf>
[^eidas]: Quy định eIDAS (EU) số 910/2014, Điều 41(2) <https://www.legislation.gov.uk/eur/2014/910/article/41/adopted>
