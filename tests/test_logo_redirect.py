import allure
import time
from pages.home_page import HomePage


@allure.feature("Логотипы")
class TestLogoRedirect:
    @allure.title("Редирект по логотипу Самоката")
    def test_samokat_logo_redirect_to_main_page(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_samokat_logo()
        assert driver.current_url == "https://qa-scooter.education-services.ru/"

    @allure.title("Редирект по логотипу Яндекса")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()

        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        time.sleep(2)

        windows = driver.window_handles
        driver.switch_to.window(windows[1])

        current_url = driver.current_url
        assert "ya.ru" in current_url or "yandex" in current_url

        driver.close()
        driver.switch_to.window(original_window)
