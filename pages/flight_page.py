from selenium.webdriver.support.ui import Select


class FlightPage:
    def __init__(self, driver):
        self.driver = driver

    def select_country(self):
        self.driver.implicitly_wait(5)
        country_dropdown = Select(self.driver.find_element_by_name('country'))
        country_dropdown.select_by_value('234')
        country_dropdown.select_by_index(3)
        return country_dropdown

