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

### Danh sách file JSON đã xử lý:
- `data/region1/data_1.json`
- `data/region2/city/data_2.json`
- `data/data_3.json`

### Kết quả chuyển đổi:
- Tạo ra 3 file CSV tương ứng.
- Dữ liệu được làm phẳng đầy đủ, không bị lỗi định dạng.

---

