import pytest
import allure
from pages.main_page import MainPageService
from pages.order_page import OrderPage
from utils.user_data import UserOrder1
from utils.user_data import UserOrder2
from utils.locators import MainPageLocators


class TestOrderScooterPage:
    @allure.title('Проверка флоу заказа')
    @pytest.mark.parametrize('button_position, user_data_set',
                             [
                                 (MainPageLocators.TOP_ORDER_BUTTON, UserOrder1),
                                 (MainPageLocators.BOTTOM_ORDER_BUTTON, UserOrder2)
                             ]
                             )
    @allure.description('Точка входа задается в параметре button_position')
    def test_order_scooter_positive(self, driver, button_position, user_data_set):
        page = MainPageService(driver)
        page.open_main_page()
        page.wait_for_main_page()
        page.click_cook_button()
        page.scroll_to_element_and_click(button_position)
        order_page = OrderPage(driver)
        order_page.fill_order_form(user_data_set.FIRST_NAME, user_data_set.LAST_NAME, user_data_set.ADDRESS,
                                   user_data_set.UNDER_STATION, user_data_set.PHONE)
        order_page.click_next_button()
        order_page.fill_rent_form(user_data_set.DATE, user_data_set.PERIOD, user_data_set.COLOR,
                                  user_data_set.COMMENT)
        order_page.click_submit_order_button()
        order_page.wait_for_modal_window()
        order_page.click_confirm_button()
        assert 'Заказ оформлен' in order_page.get_confirm()
