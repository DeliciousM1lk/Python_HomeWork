import os
import aiohttp
import asyncio

folder = "json_files_aiohttp"
os.makedirs(folder, exist_ok=True)

url = "https://jsonplaceholder.typicode.com/posts"


async def fetch_and_save():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()

                for i, obj in enumerate(json_data, start=1):
                    file_path = os.path.join(folder, f"post_{i}.json")
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(str(obj))
                print(f"Файлы успешно сохранены в папке '{folder}'.")
            else:
                print(f"Ошибка при загрузке данных: {response.status}")


if __name__ == "__main__":
    asyncio.run(fetch_and_save())
