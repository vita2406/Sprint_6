import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from constants import BASE_URL


@pytest.fixture
def driver():
    print("Запускаем браузер Firefox")
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    print("Закрываем браузер")
    driver.quit()
