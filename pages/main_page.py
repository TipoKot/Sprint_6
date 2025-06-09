from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    QUESTION_BUTTON_0,
    QUESTION_BUTTON_1,
    QUESTION_BUTTON_2,
    QUESTION_BUTTON_3,
    QUESTION_BUTTON_4,
    QUESTION_BUTTON_5,
    QUESTION_BUTTON_6,
    QUESTION_BUTTON_7
)

class MainPageScooter:
    def __init__(self, driver):
        self.driver = driver

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
            element = self.driver.find_element(*question_buttons[button_number])
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(question_buttons[button_number]))
            element.click()
        except IndexError:
            raise ValueError("Invalid button number")
        
    def click_order_button(self):
        order_button = self.driver.find_element(By.CLASS_NAME, "Button_Button__ra12g")
        order_button.click()

    def click_yandex_logo(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").click()
