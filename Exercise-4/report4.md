# Báo cáo Bài tập 4 - Chuyển đổi JSON sang CSV trong Thư mục Lồng Nhiều Cấp


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
