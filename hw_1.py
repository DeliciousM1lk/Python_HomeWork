import requests
import aiohttp
import asyncio
import time

urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 100


def fetch_all_sync(urls):
    start_time = time.time()
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.text)
    end_time = time.time()
    print(f"Синхронная загрузка завершена за {end_time - start_time:.2f} секунд.")
    return results


async def fetch_all_async(urls):
    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.text()

    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Асинхронная загрузка завершена за {end_time - start_time:.2f} секунд.")
    return results


if __name__ == "__main__":
    print("Запуск синхронной загрузки...")
    sync_results = fetch_all_sync(urls)

    print("\nЗапуск асинхронной загрузки...")
    asyncio.run(fetch_all_async(urls))
