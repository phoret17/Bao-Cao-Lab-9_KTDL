import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Cấu hình URL và thư mục
BASE_URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
TARGET_TIMESTAMP = "2024-01-19 10:27"
DOWNLOAD_DIR = "downloads"

def fetch_file_name_by_modified_time(url, target_time):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2 and target_time in cols[1].text.strip():
            link = row.find("a")
            if link and link["href"].endswith(".csv"):
                return link["href"]
    return None

def download_file(file_name, save_dir):
    file_url = BASE_URL + file_name
    response = requests.get(file_url)
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "wb") as f:
        f.write(response.content)
    return file_path

def find_max_temperature_record(csv_path):
    df = pd.read_csv(csv_path)

    # Làm sạch dữ liệu
    df = df[pd.to_numeric(df["HourlyDryBulbTemperature"], errors='coerce').notna()]
    df["HourlyDryBulbTemperature"] = df["HourlyDryBulbTemperature"].astype(float)

    # Tìm nhiệt độ cao nhất
    max_temp = df["HourlyDryBulbTemperature"].max()
    max_rows = df[df["HourlyDryBulbTemperature"] == max_temp]

    for _, row in max_rows.iterrows():
        date = row["DATE"]
        temp = row["HourlyDryBulbTemperature"]
        print(f"🌡️ Nhiệt độ cao nhất: {temp}°F vào lúc {date}")

def main():
    print("🔍 Đang thu thập dữ liệu từ trang NOAA...")
    file_name = fetch_file_name_by_modified_time(BASE_URL, TARGET_TIMESTAMP)

    if not file_name:
        print("❌ Không tìm thấy file có Last Modified =", TARGET_TIMESTAMP)
        return

    print(f"✅ Tìm thấy file: {file_name}")
    csv_path = download_file(file_name, DOWNLOAD_DIR)
    print("📥 Đã tải xuống, đang phân tích...")

    find_max_temperature_record(csv_path)

if __name__ == "__main__":
    main()
