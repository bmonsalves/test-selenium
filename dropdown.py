from selenium.webdriver.support.ui import Select


class Dropdown:

    def __init__(self, driver):
        self.driver = driver

    def test_dropdown(self):
        self.driver.find_element_by_link_text('REGISTER').click()
        country_dropdown = Select(self.driver.find_element_by_name('country'))
        country_dropdown.select_by_value('234')
        country_dropdown.select_by_index(3)
