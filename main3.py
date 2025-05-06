from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Настройка Firefox WebDriver
options = Options()
options.headless = True  # Запуск в фоновом режиме, без открытия браузера
service = Service("path/to/geckodriver")  # Укажите путь к geckodriver

# Запуск браузера
driver = webdriver.Firefox(service=service, options=options)

try:
    # Открываем сайт
    url = "https://www.divan.ru/vladivostok/category/pramye-divany"
    driver.get(url)
    time.sleep(3)  # Ждем загрузки страницы

    # Парсим элементы с ценами
    product_elements = driver.find_elements(By.CLASS_NAME, "catalog-product")

    for product in product_elements:
        try:
            # Получаем название товара
            name = product.find_element(By.CLASS_NAME, "catalog-product__name").text

            # Получаем цену товара
            price = product.find_element(By.CLASS_NAME, "catalog-product__price-current").text

            print(f"Название: {name}, Цена: {price}")
        except Exception as e:
            print(f"Ошибка при обработке товара: {e}")

finally:
    # Закрываем браузер
    driver.quit()