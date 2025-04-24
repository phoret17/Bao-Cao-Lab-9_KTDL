import os
import requests
import zipfile
from urllib.parse import urlparse
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # URL sai để test
]

def create_download_dir():
    os.makedirs("downloads", exist_ok=True)

def get_filename_from_url(url):
    return os.path.basename(urlparse(url).path)

def download_file(url):
    try:
        filename = get_filename_from_url(url)
        filepath = os.path.join("downloads", filename)
        
        print(f"Downloading {filename}...")
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return filepath
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
        return None

def extract_zip(filepath):
    try:
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall("downloads")
        os.remove(filepath)
        print(f"Extracted and removed {filepath}")
        return True
    except Exception as e:
        print(f"Failed to extract {filepath}: {str(e)}")
        return False

async def async_download(session, url):
    try:
        filename = get_filename_from_url(url)
        filepath = os.path.join("downloads", filename)
        
        async with session.get(url) as response:
            response.raise_for_status()
            with open(filepath, 'wb') as f:
                async for chunk in response.content.iter_chunked(8192):
                    f.write(chunk)
        
        return filepath
    except Exception as e:
        print(f"Async download failed for {url}: {str(e)}")
        return None

async def download_all_async():
    async with aiohttp.ClientSession() as session:
        tasks = [async_download(session, url) for url in download_uris]
        return await asyncio.gather(*tasks)

def download_with_threadpool():
    with ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(download_file, download_uris))

def main():
    create_download_dir()
    
    print("Running synchronous downloads...")
    for url in download_uris:
        filepath = download_file(url)
        if filepath:
            extract_zip(filepath)
    
    print("\nRunning asynchronous downloads...")
    filepaths = asyncio.run(download_all_async())
    for filepath in filepaths:
        if filepath:
            extract_zip(filepath)
    
    print("\nRunning threaded downloads...")
    filepaths = download_with_threadpool()
    for filepath in filepaths:
        if filepath:
            extract_zip(filepath)
    
    print("\nDownload process completed!")

if __name__ == "__main__":
    main()