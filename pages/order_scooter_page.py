from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderScooterPage(BasePage):
    # Для кого самокат
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    CHOOSE_SUBWAY_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Про аренду
    CHOOSE_WHEN_TO_RECIEVE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CHOOSE_RENT_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    CHOOSE_SCOOTER_COLOR = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Цвет']")
    COURIERED_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")
    ORDER_CONFIRMATION_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='* Заказ оформлен']")
    
    # Попап подтверждения заказа
    CONFIRM_ORDER_POPUP = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем имя в форме заказа")
    def fill_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    @allure.step("Заполняем фамилию в форме заказа")
    def fill_surname(self, surname):
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполняем адрес в форме заказа")
    def fill_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
    
    @allure.step("Выбираем станцию метро в форме заказа")
    def choose_subway_station(self, station):
        self.driver.find_element(*self.CHOOSE_SUBWAY_STATION).click()
        self.driver.find_element(By.XPATH, f"//div[text()='{station}']").click()

    @allure.step("Заполняем телефон в форме заказа")
    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    @allure.step("Кликаем кнопку 'Далее' в форме заказа")
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step("Выбираем дату получения самоката")
    def choose_when_to_receive(self, date):
        self.driver.find_element(*self.CHOOSE_WHEN_TO_RECIEVE).send_keys(date)
        self.driver.find_element(*self.CHOOSE_WHEN_TO_RECIEVE).send_keys(Keys.ENTER)

    @allure.step("Выбираем период аренды самоката")
    def choose_rent_period(self, period):
        self.driver.find_element(*self.CHOOSE_RENT_PERIOD).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"))
        )
        self.driver.find_element(By.XPATH, f"//div[text()='{period}']").click()

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, color):
        self.driver.find_element(By.XPATH, f"//label[contains(text(), '{color}')]").click()

    @allure.step("Заполняем комментарий для курьера")
    def fill_couriered_comment(self, comment):
        self.driver.find_element(*self.COURIERED_COMMENT).send_keys(comment)

    @allure.step("Кликаем кнопку 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    @allure.step("Кликаем кнопку 'Да' в попапе подтверждения заказа")
    def click_yes_button(self):
        self.driver.find_element(*self.YES_BUTTON).click()

    @allure.step("Кликаем на логотип Самоката")
    def click_logo_scooter(self):
        self.driver.find_element(By.XPATH, "//img[@alt='Scooter']").click()
