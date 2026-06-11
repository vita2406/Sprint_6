import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SAMOKAT_LOGO = (By.CSS_SELECTOR, "[alt='Scooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "[alt='Yandex']")

    FAQ_QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }

    FAQ_ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }

    EXPECTED_ANSWERS = {
        0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    }

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_ACCEPT_BUTTON)
        except:
            pass

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ORDER_BUTTON))
        if buttons:
            buttons[0].click()

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(lambda d: d.find_elements(*self.ORDER_BUTTON))
        buttons = self.driver.find_elements(*self.ORDER_BUTTON)
        if len(buttons) > 1:
            buttons[-1].click()

    @allure.step("Кликнуть на вопрос FAQ №{index}")
    def click_faq_question(self, index):
        locator = self.FAQ_QUESTIONS[index]
        # Прокручиваем к элементу
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Используем JavaScript для клика (обход перекрытия)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_faq_answer_text(self, index):
        locator = self.FAQ_ANSWERS[index]
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_samokat_logo(self):
        self.click_element(self.SAMOKAT_LOGO)

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текущее окно")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить все окна")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на окно по индексу")
    def switch_to_window(self, index):
        windows = self.get_window_handles()
        if len(windows) > index:
            self.driver.switch_to.window(windows[index])

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()
