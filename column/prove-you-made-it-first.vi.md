title: Làm sao chứng tỏ bạn là người làm ra trước: gắn ngày của bên thứ ba cho ảnh và bản thảo
description: Mọi mốc ngày bạn giữ đều sửa được. Cách ghi lại miễn phí, không tải gì lên, rằng ảnh hay bản thảo đã tồn tại vào một ngày, và khác gì với đăng ký quyền tác giả.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
---
Nếu ai đó sao chép tác phẩm của bạn, bạn có chỉ ra được rằng tác phẩm của mình có trước không? Bài hướng dẫn này giải thích cách chuẩn bị cho lúc đó, miễn phí, mà không phải cho ai xem tác phẩm.

## Mọi mốc ngày bạn giữ đều sửa được

Khó khăn của chứng cứ về ngày tháng rất đơn giản: thứ gì bạn tự sửa được thì bên kia có thể nói là bạn đã sửa.

| Mốc ngày bạn có | Vì sao yếu |
|---|---|
| Ngày đăng trên CMS | Có thể đặt ngày trong quá khứ. Tài liệu của WordPress hướng dẫn cách làm.[^wp] |
| Siêu dữ liệu ảnh (Exif) | Công cụ miễn phí như ExifTool sửa được, và có thể dời ngày hàng loạt.[^exif] |
| Ngày của tệp | Trên Windows, tệp được sao chép sẽ có thời gian tạo mới (thời gian sửa đổi được giữ nguyên).[^kb] |
| Ảnh chụp màn hình | Chỉnh sửa được như mọi hình ảnh khác. |

Có còn hơn không, nhưng không thứ nào trả lời được câu hỏi "chẳng phải anh có thể dựng lên sau đó sao?". Điều bạn cần là một mốc ngày do **người khác ngoài bạn** ghi lại, dưới dạng **không ai sửa được về sau**.

## Ghi lại bằng DateSealed

1. Mở [trang chủ](/vi/), dán văn bản hoặc chọn tệp. Bạn cũng có thể nhập URL hoặc một mã SHA-256 đã có sẵn.
2. Kiểm tra mã SHA-256 hiện ra và bấm nút để ghi lại. Mã băm được tính trong trình duyệt, nên bản thân tệp hay văn bản không bao giờ được gửi đi.
3. Trang bản ghi mở ra. Tải về `.tsr` (dấu thời gian có chữ ký) và `.ots` (bằng chứng Bitcoin), rồi cất **cùng với tệp gốc**.

Mỗi bản ghi có hai mốc: dấu thời gian RFC 3161 trả về ngay, và bản ghi OpenTimestamps được neo vào một khối Bitcoin trong vài giờ. Sau khi neo, thời điểm có thể được kiểm tra chỉ bằng sổ cái Bitcoin, kể cả khi DateSealed ngừng hoạt động. Trang bản ghi có các lệnh để tự kiểm tra trên máy của bạn.

Giới hạn là 10 bản ghi mỗi giờ và 50 bản ghi mỗi ngày cho mỗi địa chỉ IP.

## Đăng ảnh? Hãy dùng tính năng đóng dấu

[Đóng dấu ảnh](/vi/stamp) ghi lại mã băm của ảnh gốc, rồi ngay trong trình duyệt tạo một bản sao có huy hiệu nhỏ ghi ngày bản ghi và địa chỉ trang bản ghi. Ảnh không được tải lên.

Bản ghi trỏ tới **ảnh gốc**. Bản đã đóng dấu là một tệp khác, và huy hiệu có thể bị cắt đi; tự huy hiệu không chứng minh được gì. Hãy đăng bản đã đóng dấu và cất giữ cẩn thận ảnh gốc.

## Các con đường chính thức ở Việt Nam

- **Quyền tác giả phát sinh tự động.** Theo Luật Sở hữu trí tuệ, quyền tác giả phát sinh kể từ khi tác phẩm được sáng tạo và được thể hiện dưới một hình thức vật chất nhất định, dù đã đăng ký hay chưa (Điều 6).[^shtt]
- **Đăng ký quyền tác giả không bắt buộc nhưng có giá trị chứng cứ.** Việc nộp hồ sơ để được cấp Giấy chứng nhận đăng ký quyền tác giả không phải là thủ tục bắt buộc (Điều 49 khoản 2). Người đã được cấp Giấy chứng nhận không có nghĩa vụ chứng minh quyền tác giả thuộc về mình khi có tranh chấp, trừ trường hợp có chứng cứ ngược lại (Điều 49 khoản 3). Người nộp phải chịu trách nhiệm về thông tin trong hồ sơ (khoản 2a, từ ngày 1/4/2026), và phải nộp phí, lệ phí (khoản 4).[^shtt]
- **Dấu thời gian là dịch vụ tin cậy có giấy phép.** Luật Giao dịch điện tử xếp dịch vụ cấp dấu thời gian vào nhóm dịch vụ tin cậy; tổ chức cung cấp phải có giấy phép kinh doanh dịch vụ tin cậy do cơ quan quản lý nhà nước cấp (Điều 28), và dấu thời gian được tạo ra dưới dạng chữ ký số (Điều 31). Giá trị làm chứng cứ của thông điệp dữ liệu được xác định căn cứ vào độ tin cậy của cách khởi tạo, lưu trữ và cách bảo đảm tính toàn vẹn (Điều 11).[^gddt]

Bản ghi DateSealed không phải Giấy chứng nhận đăng ký quyền tác giả, và DateSealed không phải tổ chức cung cấp dịch vụ cấp dấu thời gian được cấp phép tại Việt Nam.

## Bản ghi cho thấy gì, và không cho thấy gì

Bản ghi cho thấy **dữ liệu khớp với mã băm này đã tồn tại vào thời điểm được ghi**. Chỉ vậy.

- Không cho thấy nội dung là đúng hay là sáng tạo riêng.
- Không cho thấy bạn là người làm ra hay chủ sở hữu. Bản ghi không nói ai tạo ra nó.
- **Không bảo đảm hiệu lực pháp lý.**

## Với thứ bạn thật sự cần bảo vệ

| Cách | Chi phí | Phù hợp khi |
|---|---|---|
| Đăng ký quyền tác giả | Có phí, lệ phí theo quy định | Tác phẩm quan trọng, có thể bị tranh chấp quyền sở hữu |
| Dấu thời gian của tổ chức được cấp phép | Theo nhà cung cấp | Tài liệu cần dịch vụ tin cậy theo Luật Giao dịch điện tử |
| DateSealed | Miễn phí | Ảnh, bài viết, bản thảo liên tục tăng lên, cần có ngày trước đã |

DateSealed là lớp đầu tiên rẻ và nhanh: thêm một chứng cứ để đặt cạnh những chứng cứ khác.

## Hai điều cần nhớ

- **Giữ tệp gốc.** DateSealed chỉ giữ mã băm. Không có tệp gốc thì bản ghi không gắn được với thứ gì.
- **Sửa xong thì ghi lại lần nữa.** Chỉ cần đổi một ký tự là mã băm đổi. Trên WordPress, [plugin](/api#wordpress) tự ghi lại mỗi lần đăng và cập nhật.

[^wp]: WordPress.org, "Write Posts (Classic Editor)" <https://wordpress.org/documentation/article/write-posts-classic-editor/>
[^exif]: ExifTool <https://exiftool.org/>
[^kb]: Bài viết Microsoft Knowledge Base KB299648 (cách xử lý ngày tháng khi sao chép hoặc di chuyển tệp)
[^shtt]: Văn phòng Quốc hội, văn bản hợp nhất Luật Sở hữu trí tuệ (2026), Điều 6 và Điều 49 <https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/160-vbhn-vpqh.signed.pdf>
[^gddt]: Văn phòng Quốc hội, văn bản hợp nhất Luật Giao dịch điện tử (2026), Điều 11, 28, 31 <https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/154-vbhn-vpqh.signed.pdf>
