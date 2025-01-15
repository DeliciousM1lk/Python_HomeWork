import os
import requests

folder = "json_files_requests"
os.makedirs(folder, exist_ok=True)

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
if response.status_code == 200:
    json_data = response.json()

    for i, obj in enumerate(json_data, start=1):
        file_path = os.path.join(folder, f"post_{i}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(obj))
    print(f"Файлы успешно сохранены в папке '{folder}'.")
else:
    print(f"Ошибка при загрузке данных: {response.status_code}")
