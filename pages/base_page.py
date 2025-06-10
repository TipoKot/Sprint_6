from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator):
        element = self.wait_for_element(locator)
        self.scroll_to(element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
