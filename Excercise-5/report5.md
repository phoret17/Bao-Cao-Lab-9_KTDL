# Báo cáo Bài tập 5 - Mô hình hóa Dữ liệu với Postgres và Python

### Thực hiện bởi: Nguyễn Minh Hoàng  
### Mã sinh viên: 23635051 

---

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
