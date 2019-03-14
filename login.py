class Login:

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        username_box = self.driver.find_element_by_name('userName')
        password_box = self.driver.find_element_by_name('password')
        submit_button = self.driver.find_element_by_name('login')

        username_box.send_keys('test')
        password_box.send_keys('test')
        submit_button.click()
