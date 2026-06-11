import allure
import pytest
from pages.home_page import HomePage


@allure.feature("Вопросы о важном")
class TestFAQ:
    @allure.title("Проверка ответа на вопрос №{question_index}")
    @pytest.mark.parametrize("question_index", range(8))
    def test_faq_answer_is_correct(self, driver, question_index):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        expected_answer = home_page.EXPECTED_ANSWERS[question_index]

        home_page.click_faq_question(question_index)
        actual_answer = home_page.get_faq_answer_text(question_index)

        assert actual_answer == expected_answer, f"Ошибка в вопросе {question_index}"
