import requests
from bs4 import BeautifulSoup

url = "https://www.gismeteo.ru/weather-astana-5164/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

temperature_tag = soup.find('div', class_='weather-value')
if temperature_tag:
    temperature = temperature_tag.text.strip()
    print(f"Температура в Астане: {temperature}°C")
else:
    print("Не удалось найти информацию о температуре.")
