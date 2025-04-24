import os
import requests
from zipfile import ZipFile
from io import BytesIO

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # URI lỗi
]

def get_filename_from_url(url):
    return url.split("/")[-1]

def download_and_extract(url, download_dir):
    try:
        print(f"Downloading: {url}")
        response = requests.get(url)
        response.raise_for_status()
        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(download_dir)
            print(f"Extracted: {url}")
    except Exception as e:
        print(f"❌ Error with {url}: {e}")

def main():
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    for url in download_uris:
        download_and_extract(url, download_dir)

if __name__ == "__main__":
    main()
