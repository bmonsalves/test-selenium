from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageIndex:
    def __init__(self, driver):
        self.driver = driver
        self.username_box = (By.NAME, 'userName')
        self.password_box = (By.NAME, 'password')
        self.submit_button = (By.NAME, 'login')
        self.regiter_link = (By.LINK_TEXT, 'REGISTER')

    def register(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.regiter_link).click()

    def login(self, username, password):
        self.driver.implicitly_wait(5)
        username_box = self.driver.find_element(*self.username_box)
        password_box = self.driver.find_element(*self.password_box)
        submit_button = self.driver.find_element(*self.submit_button)

        username_box.send_keys(username)
        password_box.send_keys(password)

        WebDriverWait(self.driver, 5) \
            .until(expected_conditions.element_to_be_clickable(self.submit_button))

        submit_button.click()
