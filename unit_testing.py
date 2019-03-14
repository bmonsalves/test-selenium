import HtmlTestRunner
import unittest
import os
import datetime
from selenium import webdriver
from pages.page_index import PageIndex
from pages.flight_page import FlightPage


class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.driver.get('http://newtours.demoaut.com/')
        self.page_index = PageIndex(driver=self.driver)
        self.flight_page = FlightPage(driver=self.driver)
        self.path = 'screenshots/' + str(datetime.datetime.now()) + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path, 0o0755)

    def test_dropdown(self):
        self.page_index.register()
        country_dropdown = self.flight_page.select_country()
        self.driver.get_screenshot_as_file(self.path + 'select_country.png')
        self.assertEqual(country_dropdown.first_selected_option.text.strip(), 'ANDORRA')

    def test_login(self):
        self.page_index.login(username='test', password='test')

        link_registration_form = self.driver.find_element_by_link_text('registration form')
        self.driver.save_screenshot(self.path + 'login.png')
        self.assertEqual(link_registration_form.text, 'registration form')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
