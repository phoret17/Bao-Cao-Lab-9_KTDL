#Báo cáo Bài tập 2 - Web Scraping và Phân tích Dữ liệu Khí Hậu

###Thực hiện bởi: Lê Đức Hòa  
###Mã sinh viên: 23632141  

---

## 1. Giới thiệu

Bài tập này yêu cầu sinh viên xây dựng một chương trình Python có khả năng:

- Truy cập trang web chứa dữ liệu khí hậu định dạng file.
- Tìm kiếm file dựa theo thời điểm **Last Modified = `2024-01-19 10:27`**.
- Tải đúng file đó về bằng cách tự động phân tích HTML, **không được tra cứu thủ công**.
- Phân tích dữ liệu bằng thư viện `pandas`, in ra các bản ghi có **HourlyDryBulbTemperature cao nhất**.

---

## 2. Mục tiêu

- Truy cập:  
  `https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/`
  
- Phân tích HTML để tìm file có `Last Modified = 2024-01-19 10:27`
- Tự động tải file `.csv` từ URL.
- Sử dụng `pandas` để:
  - Đọc dữ liệu.
  - Tìm giá trị lớn nhất trong cột `HourlyDryBulbTemperature`.
  - In ra các dòng dữ liệu tương ứng.

---

## 3. Quá trình thực hiện

### 3.1 Web Scraping
- Dùng `requests.get()` để lấy HTML trang web.
- Dùng `BeautifulSoup` để tìm bảng chứa danh sách file.
- Duyệt qua các dòng, so sánh cột thời gian với giá trị yêu cầu.

### 3.2 Tải và Lưu file
- Từ tên file tìm được, xây dựng URL đầy đủ.
- Tải file `.csv` bằng `requests`, lưu vào thư mục hiện tại.

### 3.3 Phân tích bằng Pandas
- Đọc file `.csv` bằng `pd.read_csv()`.
- Xử lý các cột cần thiết.
- Tìm nhiệt độ cao nhất trong cột `HourlyDryBulbTemperature`.
- Lọc ra và in các bản ghi tương ứng.

---

## 4. Kết quả

### ✅ File được tìm thấy:
- Tên file: `725300-94846-2021.csv` *(dựa trên thời gian sửa đổi `2024-01-19 10:27`)*

### 📈 Phân tích dữ liệu:
- Nhiệt độ cao nhất (`HourlyDryBulbTemperature`) tìm được: **107.0°F**
- Số dòng có nhiệt độ này: `1`

### 🖥️ Ví dụ kết quả in ra:

