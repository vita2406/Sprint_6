import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    print("Запускаем браузер Firefox")
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.education-services.ru/")
    driver.maximize_window()
    yield driver
    print("Закрываем браузер")
    driver.quit()
