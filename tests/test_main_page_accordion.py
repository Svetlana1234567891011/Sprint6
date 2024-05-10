import allure
import pytest

from utils.locators import MainPageLocators
from utils.questions_constants import AccordionQuestions
from utils.questions_constants import AccordionAnswers
from pages.main_page import MainPageService


class TestMainPageAccordion:
    @allure.title('Тест "Вопросы о важном"')
    @pytest.mark.parametrize('question, locator, answer, text_locator',
                             [
                                 (AccordionQuestions.ACCORDION_QUESTION_0_PRICE, MainPageLocators.ACCORDION_HEADER_0_PRICE,
                                  AccordionAnswers.ACCORDION_ANSWER_0_PRICE, MainPageLocators.ACCORDION_TEXT_0_PRICE),
                                 (AccordionQuestions.ACCORDION_QUESTION_1_QUANTITY, MainPageLocators.ACCORDION_HEADER_1_QUANTITY,
                                  AccordionAnswers.ACCORDION_ANSWER_1_QUANTITY, MainPageLocators.ACCORDION_TEXT_1_QUANTITY),
                                 (AccordionQuestions.ACCORDION_QUESTION_2_TIME, MainPageLocators.ACCORDION_HEADER_2_TIME,
                                  AccordionAnswers.ACCORDION_ANSWER_2_TIME, MainPageLocators.ACCORDION_TEXT_2_TIME),
                                 (AccordionQuestions.ACCORDION_QUESTION_3_DATE, MainPageLocators.ACCORDION_HEADER_3_DATE,
                                  AccordionAnswers.ACCORDION_ANSWER_3_DATE, MainPageLocators.ACCORDION_TEXT_3_DATE),
                                 (AccordionQuestions.ACCORDION_QUESTION_4_PERIOD, MainPageLocators.ACCORDION_HEADER_4_PERIOD,
                                  AccordionAnswers.ACCORDION_ANSWER_4_PERIOD, MainPageLocators.ACCORDION_TEXT_4_PERIOD),
                                 (AccordionQuestions.ACCORDION_QUESTION_5_ENERGY,
                                  MainPageLocators.ACCORDION_HEADER_5_CHARGE,
                                  AccordionAnswers.ACCORDION_ANSWER_5_ENERGY, MainPageLocators.ACCORDION_TEXT_5_CHARGE),
                                 (AccordionQuestions.ACCORDION_QUESTION_6_CLOSE,
                                  MainPageLocators.ACCORDION_HEADER_6_CANCEL,
                                  AccordionAnswers.ACCORDION_ANSWER_6_CLOSE, MainPageLocators.ACCORDION_TEXT_6_CANCEL),
                                 (AccordionQuestions.ACCORDION_QUESTION_7_PLACE,
                                  MainPageLocators.ACCORDION_HEADER_7_PLACE,
                                  AccordionAnswers.ACCORDION_ANSWER_7_PLACE, MainPageLocators.ACCORDION_TEXT_7_PLACE)
                             ]
                             )
    @allure.description('Проверяем соответствие вопроса ожидаемой формулировке, '
                        ' ответа на вопрос - ожидаемому ответу')
    def test_check_important_questions(self, driver, question, locator, answer, text_locator):
        page = MainPageService(driver)
        page.open_main_page()
        page.scroll_to_element_and_click(locator)
        question_present = page.get_text_by_locator(locator)
        answer_present = page.get_text_by_locator(text_locator)
        assert question_present == question and answer_present == answer
