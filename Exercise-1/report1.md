# Báo cáo bài tập 1 - Tải và giải nén dữ liệu

### Thực hiện bởi: Nguyễn Minh Huy
### Mã sinh viên: 23635041

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
