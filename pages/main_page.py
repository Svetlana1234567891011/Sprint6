from pages.base_page import BasePage
from utils.locators import MainPageLocators
from utils.path import PATH
import allure


class MainPageService(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.driver.get(PATH.MAIN_PAGE_URL)
        self.wait_for_top_load(MainPageLocators.MAIN_PAGE_TOP)

    @allure.step('Загружаем')
    def wait_for_main_page(self):
        self.wait_for_top_load(MainPageLocators.MAIN_PAGE_TOP)

    @allure.step('Скролл до секции вопросов')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.SUBSECTION_TOP)

    @allure.step('Нажимаем кнопку "Кук"')
    def click_cook_button(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)

