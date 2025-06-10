from pages.base_page import BasePage
import allure
from constants import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import (
    QUESTION_BUTTON_0,
    QUESTION_BUTTON_1,
    QUESTION_BUTTON_2,
    QUESTION_BUTTON_3,
    QUESTION_BUTTON_4,
    QUESTION_BUTTON_5,
    QUESTION_BUTTON_6,
    QUESTION_BUTTON_7,
    ORDER_BUTTON,
    YANDEX_LOGO
)

class MainPageScooter(BasePage):
    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Кликаем по вопросу номер {button_number}")
    def click_question_button(self, button_number):
        question_buttons = [
            QUESTION_BUTTON_0,
            QUESTION_BUTTON_1,
            QUESTION_BUTTON_2,
            QUESTION_BUTTON_3,
            QUESTION_BUTTON_4,
            QUESTION_BUTTON_5,
            QUESTION_BUTTON_6,
            QUESTION_BUTTON_7
        ]
        try:
            self.click(question_buttons[button_number])
        except IndexError:
            raise ValueError("Invalid button number")
        
    @allure.step("Кликаем по кнопке 'Заказать'")
    def click_order_button(self):
        self.click(ORDER_BUTTON)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(YANDEX_LOGO)

    @allure.step("Получаем текст ответа на вопрос {question_index}")
    def get_answer_text(self, question_index):
        panel_id = f"accordion__panel-{question_index}"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, panel_id))
        )
        return self.driver.find_element(By.ID, panel_id).text
