from pages.order_page import OrderPage
from utils.path import PATH
import allure


class TestOrdersRedirect:
    @allure.title('Открытие Дзен по клику на логотип Яндекса в хэдере')
    @allure.description('Клик по лого Яндекса')
    def test_check_orders_page_to_yandex_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_yandex_logo()
        page.switch_to_new_tab(driver.window_handles[1])
        assert 'dzen' in driver.current_url

    @allure.title('Открытие главной страницы Самоката по клику на логотип Самоката в хэдере')
    @allure.description('Клик по лого Самоката')
    def test_check_orders_page_to_scooter_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_scooter_logo()
        assert driver.current_url == PATH.MAIN_PAGE_URL
