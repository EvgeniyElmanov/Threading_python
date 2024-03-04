import threading
import requests
import time
from urllib.parse import urlparse
import os


def download_image(url):
    start_time = time.time()
    filename = os.path.basename(urlparse(url).path)
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} скачан за {time.time() - start_time:.2f} сек.")


def main(urls):
    threads = []
    total_start = time.time()
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Все изображения скачаны за {time.time() - total_start:.2f} сек.")


if __name__ == "__main__":
    import sys
    urls = sys.argv[1:]
    main(urls)
