import os
import requests
import random


def download_image(url, folder, image_number):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/image_{image_number}.jpg", "wb") as file:
            file.write(response.content)


image_url = [
    "https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg",
]

for i in range(10):
    url = random.choice(image_url)
    folder_name = f"folder_{i + 1}"  # Папки будут называться folder_1, folder_2 и т.д.
    download_image(url, folder_name, i + 1)
