from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import retrieve_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text() = "Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_number_field = (By.ID, 'phone')
    following_phone_number_button = (By.XPATH, '//button[@type="submit" and text() = "Siguiente"]')
    sms_code_field = (By.ID, 'code')
    confirm_phone_number_button = (By.XPATH, '//button[@type="submit" and text() = "Confirmar"]')
    add_payment_method_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_number_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number_field = (By.ID, 'number')
    card_code_number_field = (By.XPATH, '//input[@type="text" and @id = "code" and @name = "code"]')
    add_card_button = (By.XPATH, '//button[@type="submit" and text() = "Agregar"]')
    checked_button = (By.CSS_SELECTOR, '#card-1:checked')
    close_add_card_button = (By.XPATH, '//div[contains(@class, "payment-picker")]//button[contains(@class, "section-close")]')
    add_driver_message_field = (By.ID, 'comment')
    add_blanket_tissues_button = (By.CSS_SELECTOR, '.slider.round')
    add_blanket_tissues_button_checked =(By.CSS_SELECTOR, '.switch-input:checked')
    add_two_icecream_button = (By.XPATH, '//div[@class="counter-plus" and text() = "+"]')
    two_icecream_assert = (By.XPATH, '//div[@class="counter-value" and text() = "2"]')
    smart_button_request_taxi = (By.XPATH, '//div[contains(@class, "smart-button-wrapper")]//button[contains(@class, "smart-button")]')
    search_car_assert = (By.CSS_SELECTOR, '.order-header-title')
    info_driver_modal = (By.CSS_SELECTOR, '.order-btn-group')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
       self.wait.until(
           expected_conditions.visibility_of_element_located(self.from_field)
       ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def  get_request_taxi_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon (self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            expected_conditions.presence_of_element_located (self.comfort_icon_assert)
        )

    def reader_comfort_icon_assert(self):
        tariff = self.get_comfort_icon_assert().text
        return tariff

    def get_phone_number_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number_field(self, phone_number):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_phone_number_field(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_following_phone_number_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.following_phone_number_button)
        )

    def click_following_phone_number_button(self):
        self.get_following_phone_number_button().click()

    def set_sms_code_field (self):
        sms_code = retrieve_code.retrieve_phone_code(self.driver)
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.sms_code_field)
        ).send_keys(sms_code)

    def get_sms_code_field(self):
        return self.driver.find_element(*self.sms_code_field).get_property('value')

    def get_confirm_phone_number_button (self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.confirm_phone_number_button)
        )

    def click_confirm_phone_number_button(self):
        self.get_confirm_phone_number_button().click()

    def get_add_payment_method_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_payment_method_button)
        )

    def click_add_payment_method_button(self):
        self.get_add_payment_method_button().click()

    def get_add_card_number_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_card_number_button)
        )

    def click_add_card_number_button(self):
        self.get_add_card_number_button().click()

    def set_card_number_field(self, card_number):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def get_card_number_field(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def set_card_code_number_field (self, card_code):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.card_code_number_field)
        ).send_keys(card_code,Keys.TAB)

    def get_card_code_number_field(self):
        return self.driver.find_element(*self.card_code_number_field).get_property('value')

    def get_add_card_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def is_checked_button(self):
        checkbox = self.wait.until(
            expected_conditions.presence_of_element_located(self.checked_button)
        )
        return checkbox.is_enabled()

    def get_close_add_card_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.close_add_card_button)
        )
    def click_close_add_card_button(self):
        self.get_close_add_card_button().click()

    def set_add_driver_message_field(self,message_for_driver):
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.add_driver_message_field)
        ).send_keys(message_for_driver)

    def get_add_driver_message_field(self):
        return self.driver.find_element(*self.add_driver_message_field).get_property('value')

    def get_add_blanket_tissues_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_blanket_tissues_button)
        )
    def click_add_blanket_tissues_button(self):
        self.get_add_blanket_tissues_button().click()

    def is_add_blanket_tissues_button_checked(self):
        checked_add = self.wait.until(
            expected_conditions.presence_of_element_located(self.add_blanket_tissues_button_checked)
        )
        return checked_add.is_selected()

    def get_add_two_icecream_button(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.add_two_icecream_button)
        )
    def click_add_two_icecream_button(self):
        self.get_add_two_icecream_button().click()
        self.get_add_two_icecream_button().click()

    def is_two_icecream_assert(self):
        icecream_select = self.wait.until(
            expected_conditions.visibility_of_element_located(self.two_icecream_assert)
        )
        return icecream_select.text

    def get_smart_button_request_taxi(self):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(self.smart_button_request_taxi)
        )

    def click_smart_button_request_taxi(self):
        self.get_smart_button_request_taxi().click()

    def is_search_car_assert(self):
        search_car_select = self.wait.until(
            expected_conditions.visibility_of_element_located(self.search_car_assert)
        )
        return search_car_select.text

    def wait_info_driver_modal(self):
        long_wait = WebDriverWait(self.driver, 40)
        element_info = long_wait.until(
            expected_conditions.visibility_of_element_located(self.info_driver_modal)
        )
        return element_info.is_displayed()






