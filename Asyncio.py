import asyncio
import aiohttp
from urllib.parse import urlparse
import os
import time


async def download_image(session, url):
    start_time = time.time()
    filename = os.path.basename(urlparse(url).path)
    async with session.get(url) as response:
        with open(filename, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)
    print(f"{filename} скачан за {time.time() - start_time:.2f} сек.")


async def main(urls):
    total_start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in urls]
        await asyncio.gather(*tasks)
    print(f"Все изображения скачаны за {time.time() - total_start:.2f} сек.")


if __name__ == "__main__":
    import sys
    urls = sys.argv[1:]
    asyncio.run(main(urls))
