import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def main():
    try:
        # URL của trang web cần scrape
        base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
        
        # 1. Tải nội dung trang web
        print("Đang tải trang web...")
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        # 2. Phân tích HTML để tìm file
        print("Đang phân tích nội dung HTML...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tìm tất cả các hàng trong bảng (bỏ qua hàng header)
        rows = soup.find_all('tr')[1:]
        
        target_file = None
        target_date = datetime(2024, 1, 19, 10, 27)  # Ngày cần tìm
        
        # 3. Tìm file có ngày sửa đổi trùng khớp
        print("Đang tìm file được sửa đổi vào 2024-01-19 10:27...")
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                filename = cols[0].text.strip()
                date_str = cols[1].text.strip()
                
                try:
                    file_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    if file_date == target_date:
                        target_file = filename
                        print(f"Đã tìm thấy file: {target_file}")
                        break
                except ValueError:
                    continue
        
        if not target_file:
            raise Exception("Không tìm thấy file với ngày sửa đổi phù hợp")

        # 4. Tải file về
        download_url = base_url + target_file
        os.makedirs("downloads", exist_ok=True)  # Tạo thư mục nếu chưa có
        local_path = os.path.join("downloads", target_file)
        
        print(f"Đang tải file {target_file}...")
        file_response = requests.get(download_url, timeout=30)
        file_response.raise_for_status()
        
        with open(local_path, 'wb') as f:
            f.write(file_response.content)
        print(f"Đã tải xuống thành công: {local_path}")

        # 5. Đọc file và tìm nhiệt độ cao nhất
        print("Đang phân tích dữ liệu...")
        df = pd.read_csv(local_path)
        
        # Chuyển đổi cột nhiệt độ sang số, bỏ qua giá trị không hợp lệ
        df['HourlyDryBulbTemperature'] = pd.to_numeric(
            df['HourlyDryBulbTemperature'], errors='coerce'
        )
        
        # Tìm nhiệt độ cao nhất
        max_temp = df['HourlyDryBulbTemperature'].max()
        max_records = df[df['HourlyDryBulbTemperature'] == max_temp]
        
        # 6. In kết quả
        print("\nCác bản ghi có HourlyDryBulbTemperature cao nhất:")
        print(max_records.to_string(index=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {str(e)}")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    main()