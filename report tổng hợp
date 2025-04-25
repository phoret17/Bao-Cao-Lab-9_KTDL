# Báo cáo bài tập 1 - Tải và giải nén dữ liệu

## Giới thiệu
Bài tập này yêu cầu tải về và giải nén các file dữ liệu zip từ các URL được cung cấp. Các file zip chứa dữ liệu dưới dạng CSV và sau khi giải nén, dữ liệu sẽ được lưu trong thư mục `downloads`.

## Mục tiêu
- Tải về 7 file zip từ các URL.
- Giải nén các file zip và lưu dữ liệu vào thư mục `downloads`.
- Xóa các file zip sau khi giải nén.

## Quá trình thực hiện

1. **Tạo thư mục `downloads`**: Đầu tiên, tôi tạo thư mục `downloads` nếu nó chưa tồn tại.
2. **Tải file**: Sử dụng thư viện `requests` để tải các file zip từ các URL được cung cấp.
3. **Giải nén file**: Sau khi tải xong, tôi giải nén các file zip vào thư mục `downloads` và sau đó xóa file zip.
4. **Lỗi và giải pháp**: Trong quá trình tải file, có một vài file không tồn tại, tôi đã xử lý lỗi và tiếp tục quá trình.

## Kết quả
Sau khi thực hiện xong các bước, các file CSV đã được tải về và giải nén thành công vào thư mục `downloads`. Các file zip đã được xóa sau khi giải nén xong.

![z6535096408336_c14ec573506cebd0181d1fda559a8c76](https://github.com/user-attachments/assets/d2e4680d-e5a2-4225-96fc-65a8eceee17c)


![z6535143294280_d1b7628184edd01defb237fa286ec134](https://github.com/user-attachments/assets/24acb830-c905-4c52-964d-4e7fc0a329f8)


- Các file CSV bao gồm:
  - Divvy_Trips_2018_Q4.csv
  - Divvy_Trips_2019_Q1.csv
  - Divvy_Trips_2019_Q2.csv
  - Divvy_Trips_2019_Q3.csv
  - Divvy_Trips_2019_Q4.csv
  - Divvy_Trips_2020_Q1.csv
  - Divvy_Trips_2220_Q1.csv

# Báo cáo Bài tập 2 - Web Scraping và Phân tích Dữ liệu Khí Hậu

## Giới thiệu

Bài tập này yêu cầu sinh viên xây dựng một chương trình Python có khả năng:

- Truy cập trang web chứa dữ liệu khí hậu định dạng file.
- Tìm kiếm file dựa theo thời điểm **Last Modified = `2024-01-19 10:27`**.
- Tải đúng file đó về bằng cách tự động phân tích HTML, **không được tra cứu thủ công**.
- Phân tích dữ liệu bằng thư viện `pandas`, in ra các bản ghi có **HourlyDryBulbTemperature cao nhất**.

---

## Mục tiêu

- Truy cập:  
  `https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/`
  
- Phân tích HTML để tìm file có `Last Modified = 2024-01-19 10:27`
- Tự động tải file `.csv` từ URL.
- Sử dụng `pandas` để:
  - Đọc dữ liệu.
  - Tìm giá trị lớn nhất trong cột `HourlyDryBulbTemperature`.
  - In ra các dòng dữ liệu tương ứng.

---

## Quá trình thực hiện

### 1 Web Scraping
- Dùng `requests.get()` để lấy HTML trang web.
- Dùng `BeautifulSoup` để tìm bảng chứa danh sách file.
- Duyệt qua các dòng, so sánh cột thời gian với giá trị yêu cầu.

### 2 Tải và Lưu file
- Từ tên file tìm được, xây dựng URL đầy đủ.
- Tải file `.csv` bằng `requests`, lưu vào thư mục hiện tại.

### 3 Phân tích bằng Pandas
- Đọc file `.csv` bằng `pd.read_csv()`.
- Xử lý các cột cần thiết.
- Tìm nhiệt độ cao nhất trong cột `HourlyDryBulbTemperature`.
- Lọc ra và in các bản ghi tương ứng.

---

## Kết quả

### Phân tích dữ liệu:
- Nhiệt độ cao nhất: 54.0°F vào lúc 2021-09-22T12:20:00

### Kết quả in ra:
![Screenshot 2025-04-24 090628](https://github.com/user-attachments/assets/751ecc4b-d2a2-4a95-a5a8-c3a738c348f2)

# Báo cáo Bài tập 3 - Tải và Xử lý File `.gz` từ AWS S3 bằng Boto3  

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
- Đã trích xuất dòng đầu tiên thành công:
![z6538254500934_f30e975ab82174ffb6fc41cc13f43723](https://github.com/user-attachments/assets/b2f73cb5-158b-4e03-898d-c1aea265f6e6)
# Báo cáo Bài tập 4 - Chuyển đổi JSON sang CSV trong Thư mục Lồng Nhiều Cấp

### Thực hiện bởi: Lê Đức Hòa  
### Mã sinh viên: 23632141  

---

## Giới thiệu

Bài tập này yêu cầu sinh viên xây dựng một chương trình Python có khả năng:

- Duyệt một cây thư mục có cấu trúc lồng nhau (ragged directory).
- Tìm tất cả các file có định dạng `.json` trong thư mục `data`.
- Đọc nội dung từng file JSON, làm phẳng các cấu trúc dữ liệu lồng nhau.
- Chuyển đổi dữ liệu thành định dạng `.csv`, một file CSV tương ứng với mỗi file JSON.

---

## Mục tiêu

- Tự động quét toàn bộ thư mục `data/` để tìm file `.json`.
- Đọc và phân tích nội dung của từng file JSON.
- Làm phẳng dữ liệu, ví dụ:  
  `{"type": "Point", "coordinates": [-99.9, 16.88333]}`  
  → thành:  
  `type = Point`, `coordinates_0 = -99.9`, `coordinates_1 = 16.88333`
- Ghi dữ liệu kết quả ra file `.csv` tương ứng với từng file `.json`.

---

## Quá trình thực hiện

### 1. Quét thư mục
- Dùng `glob.glob()` với `recursive=True` để tìm tất cả file `.json` trong thư mục `data`.

### 2. Đọc file JSON
- Dùng `json.load()` để đọc từng file JSON.
- Xử lý trường hợp file chứa mảng các object hoặc một object duy nhất.

### 3. Làm phẳng cấu trúc dữ liệu
- Sử dụng đệ quy hoặc thư viện hỗ trợ để chuyển các đối tượng lồng nhau thành định dạng phẳng (flat).
- Đảm bảo mỗi trường dữ liệu đều có tên cột riêng biệt, không bị ghi đè.

### 4. Ghi ra file CSV
- Tạo file `.csv` tương ứng trong cùng thư mục hoặc thư mục khác.
- Đảm bảo các file có header và đầy đủ dữ liệu.

---

## Kết quả

- Đã chuyển đổi thành công: data/file-1.json → data/file-1.csv
- Đã chuyển đổi thành công: data/enough_already/file-4.json → data/enough_already/file-4.csv
- Đã chuyển đổi thành công: data/other_folder/file-3.json → data/other_folder/file-3.csv
- Đã chuyển đổi thành công: data/some_folder/other_folder/file-2.json → data/some_folder/other_folder/file-2.csv

![Screenshot 2025-04-24 151913](https://github.com/user-attachments/assets/d663daa7-4d39-4ad9-9544-b3510efd7bd2)

![Screenshot 2025-04-24 152009](https://github.com/user-attachments/assets/0af8fe16-d919-49c8-a039-a9fb4d5e6d20)

---

# Báo cáo Bài tập 5 - Mô hình hóa Dữ liệu với Postgres và Python

## Giới thiệu

Bài tập này yêu cầu sinh viên thực hiện các tác vụ phổ biến trong lĩnh vực Kỹ thuật Dữ liệu (Data Engineering), bao gồm:

- Phân tích cấu trúc dữ liệu từ các file `.csv`.
- Thiết kế mô hình dữ liệu (Data Modeling) tương ứng dưới dạng lệnh SQL DDL.
- Tạo các bảng trong cơ sở dữ liệu PostgreSQL kèm chỉ mục, khóa chính và khóa ngoại.
- Kết nối tới PostgreSQL bằng Python (sử dụng `psycopg2`).
- Chèn dữ liệu từ các file `.csv` vào bảng tương ứng trong PostgreSQL.

---

## Mục tiêu

- Duyệt thư mục `data/` chứa 3 file `.csv`.
- Phân tích các cột và định dạng dữ liệu, thiết kế DDL phù hợp.
- Tạo các bảng PostgreSQL sử dụng `CREATE TABLE`, thêm:
  - `PRIMARY KEY` cho mỗi bảng.
  - `FOREIGN KEY` nếu có quan hệ giữa các bảng.
  - `INDEX` cho các cột truy vấn thường xuyên.
- Viết script Python để:
  - Kết nối PostgreSQL (qua `psycopg2`).
  - Thực thi các lệnh DDL đã thiết kế.
  - Chèn dữ liệu từ các file `.csv`.

---

## Quá trình thực hiện

### 1. Phân tích dữ liệu đầu vào
- Mở từng file `.csv` trong thư mục `data/`.
- Xác định:
  - Tên cột và kiểu dữ liệu phù hợp (`INT`, `VARCHAR`, `DATE`, `FLOAT`,...).
  - Khóa chính (ID hoặc mã duy nhất).
  - Quan hệ giữa các bảng (khóa ngoại).

### 2. Thiết kế CSDL
- Viết script SQL `CREATE TABLE` cho mỗi bảng.
- Thêm `INDEX` cho các cột cần tối ưu tìm kiếm.
- Đảm bảo tính toàn vẹn dữ liệu bằng khóa chính và khóa ngoại.

### 3. Kết nối PostgreSQL bằng Python
- Sử dụng `psycopg2.connect()` để kết nối tới PostgreSQL (Docker container).
- Đọc và thực thi các câu lệnh SQL từ script.
- Tạo bảng trong cơ sở dữ liệu.

### 4. Nhập dữ liệu từ CSV
- Dùng `csv.reader()` hoặc `pandas` để đọc dữ liệu từ file.
- Duyệt từng dòng, chèn vào bảng bằng lệnh `INSERT INTO`.
- Xử lý lỗi định dạng nếu có (null, duplicate key, sai kiểu dữ liệu,...).

---

## Kết quả

![Screenshot 2025-04-24 152755](https://github.com/user-attachments/assets/1c24dc2f-74b8-421d-87ed-856277f93e69)

![Screenshot 2025-04-24 152907](https://github.com/user-attachments/assets/9a492fdd-903c-416d-82b1-0ea56fa63f43)


### Cấu trúc cơ sở dữ liệu gồm:
- **Bảng `accounts`**: chứa thông tin tài khoản.
  ![Screenshot 2025-04-24 152943](https://github.com/user-attachments/assets/755ebb34-5d4e-412c-85aa-207edc89b152)
- **Bảng `products`**: chứa thông tin sản phẩm.
  ![Screenshot 2025-04-24 153022](https://github.com/user-attachments/assets/b9615a6c-a21d-4420-96cb-cc08d215eaa5)
- **Bảng `transactions`**: chứa các giao dịch, liên kết khóa ngoại với `accounts` và `products`.
  ![Screenshot 2025-04-24 153101](https://github.com/user-attachments/assets/13a94680-8af4-402d-9356-01c0790371f7)
