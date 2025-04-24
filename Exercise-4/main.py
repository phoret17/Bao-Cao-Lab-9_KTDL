import os
import glob
import json
import csv

def flatten_json(y, parent_key='', sep='_'):
    """Hàm đệ quy để làm phẳng cấu trúc JSON lồng nhau"""
    items = []
    for k, v in y.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            if all(isinstance(i, (int, float, str)) for i in v):
                items.append((new_key, ','.join(map(str, v))))
            else:
                for i, item in enumerate(v):
                    items.extend(flatten_json(item, f"{new_key}{sep}{i}", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def json_to_csv(json_path, csv_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
    except Exception as e:
        print(f"❌ Lỗi đọc file JSON {json_path}: {e}")
        return

    # Làm phẳng dữ liệu
    if isinstance(data, list):
        flattened_data = [flatten_json(item) for item in data]
    else:
        flattened_data = [flatten_json(data)]

    if not flattened_data:
        print(f"⚠️ Không có dữ liệu để chuyển đổi trong file {json_path}")
        return

    # Ghi dữ liệu ra file CSV
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.DictWriter(cf, fieldnames=flattened_data[0].keys())
            writer.writeheader()
            writer.writerows(flattened_data)
        print(f"✅ Đã chuyển đổi thành công: {json_path} → {csv_path}")
    except Exception as e:
        print(f"❌ Lỗi ghi file CSV {csv_path}: {e}")

def main():
    # Tìm tất cả các file .json trong thư mục data (bao gồm thư mục con)
    json_files = glob.glob("data/**/*.json", recursive=True)

    if not json_files:
        print("❌ Không tìm thấy file JSON nào trong thư mục data/")
        return

    for json_file in json_files:
        csv_file = json_file.replace(".json", ".csv")
        json_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()
