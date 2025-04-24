# Báo cáo Bài tập 3 - Tải và Xử lý File `.gz` từ AWS S3 bằng Boto3  

### Thực hiện bởi: Lê Đức Hòa  
### Mã sinh viên: 23632141  

---

## Giới thiệu

Bài tập yêu cầu sinh viên xây dựng một chương trình Python sử dụng thư viện `boto3` để tương tác với dịch vụ AWS S3 nhằm thực hiện các bước sau:

- Tải một file `.gz` từ S3 bucket công khai `commoncrawl`.
- Giải nén nội dung file ngay trong bộ nhớ.
- Trích xuất URI trên dòng đầu tiên của file đã giải nén.
- Tải file `.wet` tương ứng từ URI đó trên S3.
- In ra từng dòng của file `.wet` mà không tải toàn bộ file vào bộ nhớ.

---

## Mục tiêu

- Làm quen với thư viện `boto3` để tải và xử lý file từ S3.
- Giải nén và xử lý file `.gz` trực tiếp trong bộ nhớ RAM (không ghi ra ổ đĩa).
- Trích xuất đường dẫn từ nội dung file và tải tiếp file đích từ S3.
- Duyệt qua file `.wet` bằng cách đọc từng dòng và in ra stdout (command line).
- Đảm bảo chương trình tiết kiệm bộ nhớ và có thể chạy trong môi trường Docker.

---

## Quá trình thực hiện

### 1. Tải file `.gz` từ S3
- Dùng `boto3.client('s3')` và `get_object()` để lấy file từ bucket `commoncrawl`, key là `crawl-data/CC-MAIN-2022-05/wet.paths.gz`.
- Không lưu file ra đĩa mà đọc nội dung trực tiếp bằng `response['Body'].read()`.

### 2. Giải nén file `.gz` trong bộ nhớ
- Dùng `gzip.GzipFile(fileobj=io.BytesIO(gz_content))` để giải nén file ngay trong RAM.
- Đọc dòng đầu tiên để lấy URI file `.wet`.

### 3. Tải file `.wet` từ S3 dựa vào URI
- URI có định dạng như:  
  `crawl-data/CC-MAIN-2022-05/segments/1642324744477.21/wet/CC-MAIN-20220116065446-20220116095446-00000.warc.wet.gz`
- Sử dụng `get_object()` một lần nữa để tải file `.wet.gz`.

### 4. In từng dòng của file `.wet`
- Dùng `response['Body'].iter_lines()` để lặp qua từng dòng.
- In trực tiếp từng dòng sau khi giải mã `utf-8`.

---

## Kết quả

- Tải thành công file `.gz`: `crawl-data/CC-MAIN-2022-05/wet.paths.gz`.
- Đã trích xuất dòng đầu tiên thành công:
