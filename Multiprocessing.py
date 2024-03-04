from multiprocessing import Pool
import requests
from urllib.parse import urlparse
import os
import time


def download_image(url):
    start_time = time.time()
    filename = os.path.basename(urlparse(url).path)
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return f"{filename} скачан за {time.time() - start_time:.2f} сек."


def main(urls):
    total_start = time.time()
    with Pool() as pool:
        for result in pool.imap_unordered(download_image, urls):
            print(result)
    print(f"Все изображения скачаны за {time.time() - total_start:.2f} сек.")


if __name__ == "__main__":
    import sys
    urls = sys.argv[1:]
    main(urls)
