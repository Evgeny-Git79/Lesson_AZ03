from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import csv

# Настройка WebDriver для Firefox
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Запуск браузера в фоновом режиме (без открытия окна)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    # Открытие страницы
    url = "https://www.divan.ru/vladivostok/category/pramye-divany"
    driver.get(url)
    time.sleep(5)  # Ждем загрузки страницы

    # Находим все элементы с товарами
    sofas = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')  # Блоки с товарами
    # Открытие CSV файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок столбца
        for sofa in sofas:
            # Название дивана
            title = sofa.find_element(By.CSS_SELECTOR, 'span').text

            # Цена дивана
            price = sofa.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
            writer.writerow([price])



        # Выводим данные
        #print(f"Название: {title}, Цена: {price}")
        #print(price)

finally:
    # Закрываем драйвер
    driver.quit()

