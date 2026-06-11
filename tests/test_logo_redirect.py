import allure
from pages.home_page import HomePage
from constants import BASE_URL, DZEN_URL_PATTERN


@allure.feature("Логотипы")
class TestLogoRedirect:
    @allure.title("Редирект по логотипу Самоката")
    def test_samokat_logo_redirect_to_main_page(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.click_samokat_logo()
        assert home_page.get_current_url() == BASE_URL

    @allure.title("Редирект по логотипу Яндекса")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()

        original_window = home_page.get_current_window_handle()
        home_page.click_yandex_logo()

        # Ждём открытия новой вкладки
        home_page.wait.until(lambda d: len(home_page.get_window_handles()) > 1)
        
        # Переключаемся на новую вкладку
        home_page.switch_to_window(1)
        
        # Ждём загрузки страницы (URL не должен быть about:blank)
        home_page.wait.until(lambda d: home_page.get_current_url() != "about:blank")
        
        # Проверяем URL
        current_url = home_page.get_current_url()
        assert DZEN_URL_PATTERN in current_url, f"Ожидался '{DZEN_URL_PATTERN}' в URL, получен '{current_url}'"

        # Закрываем новую вкладку и возвращаемся
        home_page.close_current_window()
        home_page.switch_to_window(0)
