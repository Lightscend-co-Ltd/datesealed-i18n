title: Vì sao tôi làm DateSealed: đôi lời từ người phát triển
description: Bắt đầu từ mong muốn bảo vệ ảnh bất động sản khỏi bị sao chép. Những gì tôi tìm thấy, và nguyên tắc cho một bản ghi miễn phí mà chính tôi cũng không sửa được.
date: 2026-11-03
author: Yuki Nakazawa (Lightscend Co., Ltd.)
source: https://nkzw.jp/2026/11/02/datesealed_free_publication_date_record_2026_en/
---
DateSealed là công cụ miễn phí ghi lại thời điểm một đoạn văn bản, một bức ảnh hay một trang web đã tồn tại. Tôi là Yuki Nakazawa, người làm ra nó. Bài này kể vì sao tôi làm, và những quyết định tôi đưa ra trong lúc làm.

## Bắt đầu từ ảnh bất động sản

Tôi điều hành một công ty bất động sản ở Nhật Bản. Chúng tôi tự chụp ảnh các bất động sản đang chào bán rồi đăng lên mạng. Tôi muốn sẵn sàng cho ngày có ai đó chỉnh sửa một bức ảnh như vậy hoặc đăng nó lên trang khác, để có thể chỉ ra rằng ảnh gốc là của chúng tôi và đã có trước.

Tôi giữ các tệp gốc, và bài đăng có ngày đăng. Nhưng tất cả những thứ đó tôi đều tự sửa được, và người nào có bản sao cũng có thể nhận cùng những ngày ấy. Điều tôi cần là một ngày tháng do **người khác ngoài tôi** ghi lại, dưới dạng **không ai sửa được về sau**.

## Những gì tôi tìm thấy trước tiên

Tôi xem những gì có ở Nhật Bản tính đến tháng 11 năm 2026.

- **Ngày xác nhận của công chứng viên.** 700 yên mỗi văn bản. Có bản điện tử, nhưng chỉ nhận tệp văn bản, PDF và XML tối đa 10 MB, và thủ tục làm vào ngày làm việc.
- **Đăng ký tại Cục Văn hóa Nhật Bản.** 3.000 yên mỗi tác phẩm, nộp bằng giấy, mỗi lần một tác phẩm. Tác phẩm được suy đoán là công bố vào ngày đã đăng ký.
- **Dấu thời gian của các nhà cung cấp được Bộ Nội vụ và Truyền thông Nhật Bản công nhận.** Đây là loại có vị thế chính thức ở Nhật. Giá chủ yếu nhắm tới doanh nghiệp.
- **Dịch vụ ghi nhận dựa trên blockchain.** Những dịch vụ tôi tìm được là dành cho doanh nghiệp, hoặc phải trả phí.
- **Chữ ký trong máy ảnh (C2PA).** Một số máy ảnh ký lên ảnh ngay khi chụp. Điều đó cho biết tệp đến từ đâu, một câu hỏi khác với việc nó tồn tại từ khi nào.

Tất cả đều hữu ích, và với thứ bạn thật sự cần bảo vệ, hãy dùng chúng. Nhưng trả phí và nộp hồ sơ cho mỗi bức ảnh hay bài viết mới thì không thực tế. Điều tôi muốn là thứ **miễn phí, không cần đăng ký, không tải gì lên, được lưu ở nơi mà ngay cả người vận hành cũng không sửa được, và tự động chạy trên WordPress mỗi lần đăng bài**. Tôi không tìm thấy, nên tôi tự làm.

## Những nguyên tắc tôi đặt ra

### Không lấy gì ngoài mã băm

DateSealed chỉ nhận mã băm SHA-256 của tệp hoặc văn bản của bạn, một "dấu vân tay" dài 64 ký tự. Mã băm được tính ngay trong trình duyệt, nên ảnh và bản thảo của bạn không rời khỏi máy. Người ta thường muốn ghi lại chính những tác phẩm chưa công bố; nếu phải giao tác phẩm cho ai đó mới ghi lại được thì mất hết ý nghĩa.

### Bạn không cần phải tin tôi

Mỗi bản ghi có hai mốc thời gian. Mốc thứ nhất là dấu thời gian RFC 3161 do đơn vị cấp dấu thời gian của chính DateSealed ký, trả về ngay. Mốc thứ hai được neo vào một khối Bitcoin thông qua OpenTimestamps, thường trong vòng vài giờ.

Mốc thứ nhất chỉ đáng tin bằng mức bạn tin tôi. Mốc thứ hai thì tôi không có quyền thay đổi. Sau khi đã neo, bạn có thể kiểm tra thời điểm chỉ bằng tệp bằng chứng (`.ots`) và sổ cái Bitcoin, kể cả khi DateSealed không còn nữa. Mỗi trang bản ghi đều liệt kê các lệnh để tự kiểm tra trên máy của bạn.

Khóa gốc của đơn vị cấp dấu thời gian được tạo trên máy tính của tôi và được mã hóa bằng cụm mật khẩu. Máy chủ chỉ giữ khóa dùng để ký.

### Không xóa, không sửa

Ngay cả màn hình quản trị cũng không có cách nào xóa bản ghi hay đổi mã băm và thời gian của nó. Một cuốn sổ chỉ có giá trị khi người giữ sổ không động vào được. Khi bạn cập nhật bài viết, bản ghi cũ vẫn còn và một bản ghi mới được thêm vào. Plugin WordPress cũng theo đúng nguyên tắc này.

### Nói trước những gì nó không làm được

Bản ghi cho thấy dữ liệu khớp với mã băm đã tồn tại vào thời điểm đó. Không hơn. Nó không cho thấy bạn là người làm ra, bạn là chủ sở hữu, hay nội dung là đúng, và **không bảo đảm hiệu lực pháp lý**. Tôi ghi điều này ở nhiều chỗ trên trang, vì kỳ vọng sai chính là lúc người ta bị thiệt.

### Nói rõ những gì được thu thập

Để chống lạm dụng, áp dụng giới hạn, tìm lỗi và hiểu cách sử dụng, mỗi lần dùng đều được ghi lại cùng địa chỉ IP và một vài chi tiết khác. Dữ liệu này không dùng cho quảng cáo và không bán. Địa chỉ IP và tên máy chủ được giữ trên máy chủ này 30 ngày, sau đó chuyển sang nơi lưu trữ riêng do tôi quản lý tối đa 13 tháng; hết thời hạn đó, phần cuối địa chỉ bị xóa và chỉ còn lại số liệu thống kê. Chi tiết có trong [điều khoản](/vi/terms).

## Cho bất kỳ ai

Miễn phí và không cần tài khoản. Giao diện có 20 ngôn ngữ. Ngoài ra còn có tính năng đóng dấu cho ảnh, cách ghi lại một URL đã đăng, API và plugin WordPress. Bạn có thể [tải plugin từ trang API](/api#wordpress); việc đưa lên wordpress.org đang được xét duyệt.

Cách dùng cho ảnh và bản thảo của bạn, cùng vị trí của nó bên cạnh việc đăng ký quyền tác giả ở Việt Nam, có trong bài "[Làm sao chứng minh bạn làm ra trước](/vi/column/prove-you-made-it-first)".

## Hãy cho tôi biết chỗ nào vướng

Tôi muốn nghe DateSealed gây khó ở đâu và bạn muốn nó làm gì tiếp theo, nhất là từ những nhiếp ảnh gia và blogger từng vướng vào tranh chấp "ai có trước". Thông tin liên hệ ở cuối trang.
