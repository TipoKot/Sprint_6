from selenium.webdriver.common.by import By

# основные кнопки
ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

# кнопки вопросов в секции "Вопрос-ответ"
QUESTION_BUTTON_0 = (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']")
QUESTION_BUTTON_1 = (By.XPATH, "//div[@class='accordion__button' and text()='Хочу сразу несколько самокатов! Так можно?']")
QUESTION_BUTTON_2 = (By.XPATH, "//div[@class='accordion__button' and text()='Как рассчитывается время аренды?']")
QUESTION_BUTTON_3 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли заказать самокат прямо на сегодня?']")
QUESTION_BUTTON_4 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
QUESTION_BUTTON_5 = (By.XPATH, "//div[@class='accordion__button' and text()='Вы привозите зарядку вместе с самокатом?']")
QUESTION_BUTTON_6 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли отменить заказ?']")
QUESTION_BUTTON_7 = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")