from selenium import webdriver

browser = webdriver.Firefox() # Открываем окно Firefox через вебдрайвер
browser.get('http://localhost:8000') # Открываем нужный адрес

assert 'Congratulations' in browser.title # Проверяем, есть ли слово "Congratulations" в названии вкладки