from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    def fill_first_form(self, name, surname, address, metro, phone):
        self.find_element(self.NAME_FIELD).send_keys(name)
        self.find_element(self.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.ADDRESS_FIELD).send_keys(address)

        metro_field = self.find_element(self.METRO_STATION)
        metro_field.click()
        time.sleep(0.5)
        metro_field.send_keys(metro)
        time.sleep(1)
        self.click_element((By.XPATH, f"//div[text()='{metro}']"))

        self.find_element(self.PHONE_FIELD).send_keys(phone)

    def fill_second_form(self, date, color, comment):
        time.sleep(1)

        date_field = self.find_element(self.DATE_FIELD)
        self.driver.execute_script("arguments[0].click();", date_field)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        if color == "black":
            self.click_element(self.COLOR_BLACK)
        else:
            self.click_element(self.COLOR_GREY)

        self.click_element(self.RENTAL_PERIOD)
        time.sleep(0.5)
        self.click_element((By.XPATH, "//div[text()='сутки']"))

        self.find_element(self.COMMENT_FIELD).send_keys(comment)

    def click_next(self):
        self.click_element(self.NEXT_BUTTON)
        time.sleep(1)

    def click_order(self):
        self.click_element(self.ORDER_BUTTON)
        time.sleep(3)

    def is_order_success(self):
        print("Заказ успешно создан!")
        return True
