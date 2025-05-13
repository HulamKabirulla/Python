#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# URL для парсинга
url = 'YOUR URL HERE'

# Получаем HTML-код страницы
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример: парсим все заголовки <h2>
    headlines = soup.find_all('h2')

    # Выводим текст всех заголовков
    for i, h in enumerate(headlines, 1):
        print(f"{i}. {h.get_text(strip=True)}")
else:
    print("Ошибка при получении страницы:", response.status_code)

print(response.text)