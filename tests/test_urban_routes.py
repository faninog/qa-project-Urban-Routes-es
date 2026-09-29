from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)


    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        assert self.routes_page.reader_comfort_icon_assert() == "Comfort"

    def test_3_add_phone_number(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_following_phone_number_button()
        self.routes_page.set_sms_code_field()
        self.routes_page.click_confirm_phone_number_button()
        assert self.routes_page.get_phone_number_field() == data.phone_number

    def test_4_add_payment_method(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_add_payment_method_button()
        self.routes_page.click_add_card_number_button()
        self.routes_page.set_card_number_field(data.card_number)
        self.routes_page.set_card_code_number_field(data.card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.is_checked_button() is True
        self.routes_page.click_close_add_card_button()

    def test_5_add_driver_message(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.set_add_driver_message_field(data.message_for_driver)
        assert self.routes_page.get_add_driver_message_field() == data.message_for_driver

    def test_6_add_blanket_tissues(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_add_blanket_tissues_button()
        assert self.routes_page.is_add_blanket_tissues_button_checked() is True

    def test_7_add_two_icecream(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_add_two_icecream_button()
        assert self.routes_page.is_two_icecream_assert() == "2"

    def test_8_modal_look_taxi(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_following_phone_number_button()
        self.routes_page.set_sms_code_field()
        self.routes_page.click_confirm_phone_number_button()
        self.routes_page.click_add_payment_method_button()
        self.routes_page.click_add_card_number_button()
        self.routes_page.set_card_number_field(data.card_number)
        self.routes_page.set_card_code_number_field(data.card_code)
        self.routes_page.click_add_card_button()
        self.routes_page.click_close_add_card_button()
        self.routes_page.set_add_driver_message_field(data.message_for_driver)
        self.routes_page.click_add_blanket_tissues_button()
        self.routes_page.click_add_two_icecream_button()
        self.routes_page.click_smart_button_request_taxi()
        assert self.routes_page.is_search_car_assert() == "Buscar automóvil"

    def test_9_wait_info_driver_modal(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_following_phone_number_button()
        self.routes_page.set_sms_code_field()
        self.routes_page.click_confirm_phone_number_button()
        self.routes_page.click_add_payment_method_button()
        self.routes_page.click_add_card_number_button()
        self.routes_page.set_card_number_field(data.card_number)
        self.routes_page.set_card_code_number_field(data.card_code)
        self.routes_page.click_add_card_button()
        self.routes_page.click_close_add_card_button()
        self.routes_page.set_add_driver_message_field(data.message_for_driver)
        self.routes_page.click_add_blanket_tissues_button()
        self.routes_page.click_add_two_icecream_button()
        self.routes_page.click_smart_button_request_taxi()
        assert self.routes_page.wait_info_driver_modal() is True

    def teardown_method(self):
        self.driver.quit()
