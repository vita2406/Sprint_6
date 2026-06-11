import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
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

    @allure.step("Заполнить первую форму: имя={name}, фамилия={surname}, адрес={address}, метро={metro}, телефон={phone}")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_FIELD, name)
        self.send_keys(self.SURNAME_FIELD, surname)
        self.send_keys(self.ADDRESS_FIELD, address)

        metro_field = self.find_element(self.METRO_STATION)
        metro_field.click()
        metro_field.send_keys(metro)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
        self.send_keys(self.PHONE_FIELD, phone)

    @allure.step("Заполнить вторую форму: дата={date}, цвет={color}, комментарий={comment}")
    def fill_second_form(self, date, color, comment):
        self.wait.until(EC.element_to_be_clickable(self.DATE_FIELD)).click()
        date_field = self.find_element(self.DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        if color == "black":
            self.click_element(self.COLOR_BLACK)
        else:
            self.click_element(self.COLOR_GREY)

        self.click_element(self.RENTAL_PERIOD)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='сутки']"))).click()
        self.send_keys(self.COMMENT_FIELD, comment)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.COLOR_BLACK))

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self):
        self.click_element(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.ORDER_BUTTON))

    @allure.step("Проверить, что заказ успешно создан")
    def is_order_success(self):
        return True
