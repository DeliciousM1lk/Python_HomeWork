import requests

url = "https://yandex.kz/pogoda/astana"
response = requests.get(url)
html = response.text


start_marker = '<span class="temp__value temp__value_with-unit">'
end_marker = '</span>'

start = html.find(start_marker) + len(start_marker)
end = html.find(end_marker, start)
temperature = html[start:end]

print(f"Температура в Астане: {temperature}°C")
