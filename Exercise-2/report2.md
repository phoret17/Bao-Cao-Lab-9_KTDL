# Báo cáo Bài tập 2 - Web Scraping và Phân tích Dữ liệu Khí Hậu

### Thực hiện bởi: Nguyễn Minh Huy
### Mã sinh viên: 23635041

---

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
