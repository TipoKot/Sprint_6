import pytest
from constants import BASE_URL
from pages.main_page import MainPageScooter
from pages.order_scooter_page import OrderScooterPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Заказ самоката. Нужно проверить весь флоу позитивного сценария с двумя наборами данных. Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.
# Из чего состоит позитивный сценарий:
    # Нажать кнопку «Заказать». На странице две кнопки заказа.
    # Заполнить форму заказа.
    # Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
    # Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
    # Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
# Нужно написать тесты с разными данными: минимум два набора. Какие именно данные использовать — на твоё усмотрение. Сценарий общий, несмотря на разные точки входа: не нужно дважды тестировать каждую из них.

class TestScooterOrder:
    @pytest.mark.parametrize("name, surname, address, station, phone, date, period, color, comment", [
        ("Иван", "Иванов", "Москва, ул. Ленина, д. 1", "Смоленская", "+79161234567", "15.10.2023", "сутки", "чёрный жемчуг", "Пожалуйста, позвоните перед доставкой."),
        ("Анна", "Сидорова", "Санкт-Петербург, Невский пр. 100", "Сокольники", "+79270000000", "20.10.2023", "двое суток", "серая безысходность", "Не звоните — просто оставьте у двери."),
    ])
    def test_order_scooter(self, driver, name, surname, address, station, phone, date, period, color, comment):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "Order_Header__BZXOb"), "Для кого самокат")
        )

        scooter_order_page = OrderScooterPage(driver)
        scooter_order_page.fill_name(name)
        scooter_order_page.fill_surname(surname)
        scooter_order_page.fill_address(address)
        scooter_order_page.choose_subway_station(station)
        scooter_order_page.fill_phone(phone)
        scooter_order_page.click_next_button()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "Order_Header__BZXOb"), "Про аренду")
        )

        scooter_order_page.choose_when_to_receive(date)
        scooter_order_page.choose_rent_period(period)
        scooter_order_page.choose_scooter_color(color)
        scooter_order_page.fill_couriered_comment(comment)
        scooter_order_page.click_order_button()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='Order_Modal__YZ-d3']"))
        )

        scooter_order_page.click_yes_button()

        order_confirmation = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Order_ModalHeader__3FDaJ"))
        )
        assert "Заказ оформлен" in order_confirmation.text, "Заказ не оформлен"

    def test_scooter_button_leads_to_main_page(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_order_button()

        scooter_order_page = OrderScooterPage(driver)
        scooter_order_page.click_logo_scooter()

        assert driver.current_url == BASE_URL, "Логотип Самоката не ведёт на главную страницу"

    def test_yandex_logo_redirects_to_dzen(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_yandex_logo()

        # Проверяем, что открылось новое окно и URL соответствует главной странице Дзена
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("dzen")
        )

        assert "dzen.ru" in driver.current_url, "Логотип Яндекса не ведёт на главную страницу Дзена"
        