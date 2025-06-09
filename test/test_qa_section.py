from pages.main_page import MainPageScooter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL
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

class TestQuestionsAndAnswers:
    def test_answer_0(self, driver):
        driver.get(BASE_URL)
        
        main_page = MainPageScooter(driver)
        main_page.click_question_button(0)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-0'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-0').text
        assert answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой.", "Ответ не совпадает"

    def test_answer_1(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(1)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-1'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-1').text
        assert answer == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.", "Ответ не совпадает"

    def test_answer_2(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(2)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-2'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-2').text
        assert answer == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.", "Ответ не совпадает"

    def test_answer_3(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-3'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-3').text
        assert answer == "Только начиная с завтрашнего дня. Но скоро станем расторопнее.", "Ответ не совпадает"

    def test_answer_4(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(4)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-4'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-4').text
        assert answer == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.", "Ответ не совпадает"

    def test_answer_5(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(5)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-5'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-5').text
        assert answer == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.", "Ответ не совпадает"

    def test_answer_6(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(6)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-6'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-6').text
        assert answer == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.", "Ответ не совпадает"
    
    def test_answer_7(self, driver):
        driver.get(BASE_URL)

        main_page = MainPageScooter(driver)
        main_page.click_question_button(7)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'accordion__panel-7'))
        )
        answer = driver.find_element(By.ID, 'accordion__panel-7').text
        assert answer == "Да, обязательно. Всем самокатов! И Москве, и Московской области.", "Ответ не совпадает"
        