import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrderFlow:
    @allure.title("Позитивный сценарий заказа")
    @pytest.mark.parametrize(
        "button_position, name, surname, address, metro, phone, date, color, comment",
        [
            ("top", "Роман", "Смирнов", "ул. Цветкова 5", "Сокольники", "+79397689043", "11.06.2026", "black", "Позвонить за 30 минут до приезда"),
            ("bottom", "Олег", "Воробьев", "пр. Садовая 35", "Лубянка", "+79658906543", "12.06.2026", "grey", "Позвонить за 15 минут до приезда"),
        ]
    )
    def test_order_success(self, driver, button_position, name, surname, address,
                           metro, phone, date, color, comment):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.accept_cookies()

        if button_position == "top":
            home_page.click_order_button_top()
        else:
            home_page.click_order_button_bottom()

        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.click_next()
        order_page.fill_second_form(date, color, comment)
        order_page.click_order()

        assert order_page.is_order_success(), "Заказ не оформлен"
